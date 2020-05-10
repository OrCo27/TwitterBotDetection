from utils_nnet import ModelCommon as utils
from model import RankingModel
from dataset_parser import DatasetBuilder, DatasetConfig
from logger import Log
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from threading import Thread
import os.path
import numpy as np
import os
import pickle
from os import path
from embedding import Embedding
from callbacks_nnet import CallBackTrainNNet
import sys


class ModelTrainer:
    def __init__(self, logger=Log(print), embedding_file='data/wiki-news-300d-1M.vec',
                 bots_file='data/bots_tweets.txt', human_file='data/human_tweets.txt',
                 validation_split=0.2, test_split=0.2, batch_size=50, epochs=25,
                 additional_feats_enabled=True, config_controller=None,
                 early_stopping=5, dataset_config=DatasetConfig.USER_STATE):

        self.config_controller = config_controller
        self.dataset = DatasetBuilder(logger, self.check_exit_breakpoint, dataset_config)
        _,self.dataset_config_name = dataset_config
        self.logger = logger
        self.embedding = Embedding(logger, embedding_file)
        self.model = None  # initialize later
        self.additional_feats_enabled = additional_feats_enabled
        self.batch_size = batch_size
        self.epochs = epochs
        self.early_stopping = early_stopping
        self.validation_split = validation_split
        self.test_split = test_split
        self.bots_file = bots_file
        self.human_file = human_file
        self.x_bot_tweets = []
        self.bot_tweets = []
        self.bot_test_tweets = []
        self.doc_test_tweets = []
        self.labels_test = []

    def train_model(self):
        # load exists dataset or create a new one if not exists
        #self._load_datset()

        # build dataset for training
        self.dataset.perform_build(self.bots_file, self.human_file, self.additional_feats_enabled)

        # stopping break - if there is a request - exit
        self.check_exit_breakpoint()

        self.logger.write_log('Splitting datasets into train and test sets')

        data_train, data_test = self._split_train_test_sets()
        q_train, d_train, addn_feat_train, y_train = data_train
        q_test, d_test, addn_feat_test, y_test = data_test

        # stopping break - if there is a request - exit
        self.check_exit_breakpoint()

        self.logger.write_log(f'trains samples: {len(q_train)}')
        self.logger.write_log(f'test samples: {len(q_test)}')

        # extract some parameters that uses for our model
        vocabulary = self.dataset.tokenizer.index_word
        max_text_len = self.dataset.max_text_len
        addit_feat_len = self.dataset.addit_feat_len
        tokenizer = self.dataset.tokenizer

        # convert texts to sequences
        self.logger.write_log('convert texts to sequences')
        x_q_train = utils.convert_text_to_sequences(tokenizer, q_train, max_text_len)
        x_d_train = utils.convert_text_to_sequences(tokenizer, d_train, max_text_len)
        x_q_test = utils.convert_text_to_sequences(tokenizer, q_test, max_text_len)
        x_d_test = utils.convert_text_to_sequences(tokenizer, d_test, max_text_len)

        # stopping break - if there is a request - exit
        self.check_exit_breakpoint()

        # prepare data for predicting
        self.bot_tweets = self._get_unique_matches(q_train, y_train)
        self.x_bot_tweets = utils.convert_text_to_sequences(tokenizer, self.bot_tweets, max_text_len)

        self.bot_test_tweets = q_test
        self.doc_test_tweets = d_test
        self.labels_test = y_test

        # create our model with embedding matrix
        self.model = self._create_model(vocabulary, max_text_len, addit_feat_len)

        self.logger.write_log(f'Start training process..')

        # stopping break - if there is a request - exit
        self.check_exit_breakpoint()

        # start fitting model
        history = self.model.fit([np.array(x_q_train), np.array(x_d_train), np.array(addn_feat_train)],
                                 np.array(y_train),
                                 epochs=self.epochs,
                                 batch_size=self.batch_size,
                                 verbose=1,
                                 validation_split=self.validation_split,
                                 callbacks=self._get_callbacks())

        # stopping break - if there is a request - exit
        self.check_exit_breakpoint()

        # self.logger.write_log(f'Start evaluating our model on test set', 'evaluate')
        #
        # # evaluate the model with test-set
        # result = self.model.evaluate([np.array(x_q_test), np.array(x_d_test), np.array(addn_feat_test)],
        #                              np.array(y_test), verbose=1)
        #
        # self.logger.write_log(f'test loss={result[0]:.4f}, test accuracy={result[1]:.4f}', 'evaluate')

        self.logger.write_log('Training Process Completed Successfully!')

        self.config_controller.change_widgets_disabled(False)
        self.config_controller.ui.btn_save.setDisabled(False)

    # stopping break - if there is a request - exit
    def check_exit_breakpoint(self, exit_process=lambda: sys.exit()):
        if self.config_controller.is_stopped():
            self.logger.enable_log()
            self.logger.write_log('Stopped Process Done Successfully!')
            self.config_controller.change_widgets_disabled(False)
            exit_process()

    def _get_unique_matches(self, query_train, label_train):
        lst = list(zip(query_train, label_train))
        lst_matches = list(filter(lambda x: x[1] == 1, lst))
        bot_matches, _ = list(map(list, zip(*lst_matches)))
        unique_matches = utils.remove_duplicates(bot_matches)
        return unique_matches

    def _split_train_test_sets(self):
        # make triples from query, doc, and overlap features
        x = list(map(list, zip(self.dataset.query_list, self.dataset.doc_list, self.dataset.overlap_feats)))
        y = self.dataset.labels_list

        # split all data into train, test sets
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=self.test_split)
        q_train, d_train, addn_feat_train = list(map(list, zip(*x_train)))
        q_test, d_test, addn_feat_test = list(map(list, zip(*x_test)))

        return [q_train, d_train, addn_feat_train, y_train], [q_test, d_test, addn_feat_test, y_test]

    def _get_callbacks(self):
        """
        callbacks to use when training model.
        - Early stopping to stop training if it's going to be overfitting and restore best weights.
        """
        early_stop = EarlyStopping(monitor='val_loss',
                                   min_delta=.01,
                                   patience=self.early_stopping,
                                   verbose=1,
                                   mode='auto',
                                   restore_best_weights=True)

        custom_callback = CallBackTrainNNet(self.logger, self.config_controller, self.check_exit_breakpoint)

        return [early_stop, custom_callback]

    def _create_model(self, vocabulary, max_text_len, addit_feat_len):
        # load embedding matrix
        embedding_matrix = self.embedding.load_embedding_matrix(vocabulary)

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
        model_path = f'{model_name}.h5'
        pickle_path = f'{model_name}.pickle'

        self.model.save(model_path)

        # saving all variables for next uses
        with open(pickle_path, 'wb') as f:
            pickle.dump([self.x_bot_tweets, self.bot_tweets, self.dataset.tokenizer,
                         self.dataset.max_text_len, self.additional_feats_enabled], f)

        self.logger.write_log('Model Saved Successfully')


class ModelTrainerThread(Thread):
    def __init__(self, model_train):
        super().__init__()
        self.model_train = model_train

    def run(self):
        self.model_train.train_model()
