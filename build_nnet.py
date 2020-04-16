from model import RankingModel
from dataset_parser import DatasetBuilder, DatasetConfig
from logger import Log
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
import os.path
import numpy as np
import time
import os
import pickle
from os import path


class ModelTrainer:
    def __init__(self, logger=Log(print), embedding_file='data/wiki-news-300d-1M.vec',
                 bots_file='data/bots_tweets.txt', human_file='data/human_tweets.txt',
                 validation_split=0.2, test_split=0.2, batch_size=50, epochs=25, embedding_dim=200,
                 additional_feats_enabled=True, dataset_config=DatasetConfig.USER_STATE):

        self.dataset = DatasetBuilder(logger, dataset_config)
        _,self.dataset_config_name = dataset_config
        self.logger = logger
        self.model = None  # initialize later
        self.additional_feats_enabled = additional_feats_enabled
        self.embedding_file = embedding_file
        self.embedding_dim = embedding_dim
        self.batch_size = batch_size
        self.epochs = epochs
        self.validation_split = validation_split
        self.test_split = test_split
        self.bots_file = bots_file
        self.human_file = human_file

    def train_model(self):
        # load exists dataset or create a new one if not exists
        self._load_datset()

        # extract some parameters that uses for our model
        vocabulary = self.dataset.tokenizer.index_word
        max_text_len = self.dataset.max_text_len
        addit_feat_len = self.dataset.addit_feat_len

        self.logger.write_log('Splitting datasets into train and test sets', title='training')

        # make triples from query, doc, and overlap features
        x = list(map(list, zip(self.dataset.query_list, self.dataset.doc_list, self.dataset.overlap_feats)))
        y = self.dataset.labels_list

        # split all data into train, test sets
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=self.test_split)
        q_train, d_train, addn_feat_train = list(map(list, zip(*x_train)))
        q_test, d_test, addn_feat_test = list(map(list, zip(*x_test)))

        self.logger.write_log(f'trains samples: {len(q_train)}', title='training')
        self.logger.write_log(f'test samples: {len(q_test)}', title='training')

        # create our model with embedding matrix
        self.model = self._create_model(vocabulary, max_text_len, addit_feat_len)

        self.logger.write_log(f'Start training process..', title='training')

        # start fitting model
        history = self.model.fit([np.array(q_train), np.array(d_train), np.array(addn_feat_train)],
                                 np.array(y_train),
                                 epochs=self.epochs,
                                 batch_size=self.batch_size,
                                 verbose=1,
                                 validation_split=self.validation_split,
                                 callbacks=self._get_callbacks())

        self.logger.write_log(f'Start evaluating our model on test set', 'evaluate')

        # evaluate the model with test-set
        result = self.model.evaluate([np.array(q_test), np.array(d_test), np.array(addn_feat_test)], np.array(y_test),
                                     verbose=0)

        self.logger.write_log(f'test loss={result[0]:.4f}, test accuracy={result[1]:.4f}', 'evaluate')

    def _load_embeddings_file(self):
        embeddings_index = {}
        self.logger.write_log(f'Loading embedding file: \'{self.embedding_file}\'')
        start = time.time()
        with open(self.embedding_file, 'r', encoding='utf-8') as f:
            for line in f:
                values = line.split()
                word = values[0]
                coefs = np.asarray(values[1:], dtype='float32')
                embeddings_index[word] = coefs

        self.logger.write_log(f'Loaded in {time.time() - start} seconds')
        self.logger.write_log(f'Found {len(embeddings_index)} word vectors.')
        return embeddings_index

    def _create_embeddings_matrix(self, embeddings_index, vocabulary):
        try:
            self.logger.write_log(f'Creating embedding matrix, dim: {len(vocabulary) + 1} x {self.embedding_dim}')
            embeddings_matrix = np.random.rand(len(vocabulary) + 1, self.embedding_dim)
            words_not_found = 0

        except Exception as e:
            print(e)

        for i, word in vocabulary.items():
            embedding_vector = embeddings_index.get(word)
            if embedding_vector is not None:
                embeddings_matrix[i] = embedding_vector
            else:
                words_not_found += 1

        self.logger.write_log(f'Number of words not in trained embedding: {words_not_found}')
        return embeddings_matrix

    def _get_callbacks(self):
        """
        callbacks to use when training model.
        - Early stopping to stop training if it's going to be overfitting and restore best weights.
        """
        early_stop = EarlyStopping(monitor='val_loss',
                                   min_delta=.01,
                                   patience=5,
                                   verbose=1,
                                   mode='auto',
                                   baseline=None,
                                   restore_best_weights=True)

        return [early_stop]

    def _load_embedding_matrix(self, vocabulary):
        embedding_index_file = os.path.splitext(self.embedding_file)[0] + '.pickle'
        if path.exists(embedding_index_file):
            self.logger.write_log('Trying to load embedding index from npy dump.')
            with open(embedding_index_file, 'rb') as f:
                embedding_index = pickle.load(f)
        else:
            self.logger.write_log('Load from dump failed, reading from embedding file.')
            # load embedding vectors and create embedding matrix
            embedding_index = self._load_embeddings_file()
            with open(embedding_index_file, 'wb') as f:
                pickle.dump(embedding_index, f)

        # load embedding vectors and create embedding matrix
        embedding_matrix = self._create_embeddings_matrix(embedding_index, vocabulary)

        return embedding_matrix

    def _create_model(self, vocabulary, max_text_len, addit_feat_len):
        # load embedding matrix
        embedding_matrix = self._load_embedding_matrix(vocabulary)

        # create our model
        model = RankingModel(self.logger, max_text_len, addit_feat_len, embedding_matrix)
        cnn_model = model.build_model()

        return cnn_model

    def _load_datset(self):
        model_file = f'data/dataset_{self.dataset.config_name}.pickle'
        self.logger.write_log(f'Try to load exists dataset with config: {self.dataset.config_name}')

        if path.exists(model_file):
            with open(model_file, 'rb') as f:
                self.dataset = pickle.load(f)
        else:
            self.logger.write_log(f'Load fail, create a new dataset for training')
            # build dataset for training
            self.dataset.perform_build(self.bots_file, self.human_file, self.additional_feats_enabled)
            with open(model_file, 'wb') as f:
                pickle.dump(self.dataset, f)

    def save_model(self, model_name):
        # saving the complete model including it's weights
        full_path = os.path.join('output', model_name + f'_{self.dataset_config_name}.h5')
        self.model.save(full_path)

        # saving all variables for next uses
        # TODO: when starting to implement predict-side, check which variables are needed for saving?
