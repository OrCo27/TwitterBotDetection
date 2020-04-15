from utils_nnet import ModelCommon
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import random


class DatasetBuilder:
    def __init__(self, logger):
        self.tokenizer = Tokenizer()
        self.utils = ModelCommon()
        self.logger = logger
        self.max_text_len = 0
        self.addit_feat_len = 1
        self.query_list = []
        self.doc_list = []
        self.overlap_feats = []
        self.labels_list = []

    def _load_file(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return lines

    def _perform_pre_processing(self, text_list):
        pre_list = list(map(self.utils.preprocess_tweet, text_list))
        return list(filter(lambda x: len(x) > 2, pre_list))  # filter only texts with len>2

    def _get_maxlen(self, text_list):
        return max(map(lambda x: len(x), text_list))

    def _build_vocab_docs(self, query_list, doc_list):
        self.logger.write_log(f'Building the vocabulary based on queries and documents')

        # insert all docs to vocab
        docs = query_list + doc_list
        self.tokenizer.fit_on_texts(docs)
        self.max_text_len = self._get_maxlen(docs)

        self.logger.write_log(f'founded {len(self.tokenizer.word_index)} words, max len: {self.max_text_len}')

    def _convert_text_to_sequences(self, text_list, max_text_len):
        x_text = self.tokenizer.texts_to_sequences(text_list)
        return pad_sequences(x_text, maxlen=max_text_len, padding='post', truncating='post')

    def _generate_final_docs_and_labels(self, x_query, x_doc):
        self.logger.write_log(f'Generating final dataset with appropriate candidates...')

        # create temporary labels for each list
        query_labels = [1] * len(x_query)
        doc_labels = [0] * len(x_doc)

        # create pairs of (text, label)
        query_labels_pairs = list(zip(x_query, query_labels))
        doc_labels_pairs = list(zip(x_doc, doc_labels))

        # concrate two lists and shuffle them
        pairs_mixed = query_labels_pairs + doc_labels_pairs
        # random.shuffle(pairs_mixed)

        # find for each original query an element from pairs_shuffle
        # so if it will be from the same query collection it will get label=1 (similar)
        # and else it will get label=0 (different)
        final_docs, final_labels = [], []
        for i in range(len(x_query)):
            # select a random pair from the collection
            rand = random.choice(pairs_mixed)
            text, label = rand
            final_docs.append(text)
            final_labels.append(label)

        return final_docs, final_labels

    def _prepare_datasets_files(self, query_file_path, doc_file_path):
        # load all datasets from files
        self.logger.write_log(f'Loading query file: \'{query_file_path}\'')
        query_list = self._load_file(query_file_path)

        self.logger.write_log(f'Loading document file: \'{doc_file_path}\'')
        doc_list = self._load_file(doc_file_path)

        # perform pre-processing
        self.logger.write_log(f'Performing pre-processing on queries...')
        query_list = self._perform_pre_processing(query_list)

        self.logger.write_log(f'Performing pre-processing on documents...')
        doc_list = self._perform_pre_processing(doc_list)

        return query_list, doc_list

    def _generate_additional_feats(self, query_list, doc_list, additional_feats_enabled):
        if additional_feats_enabled:
            self.logger.write_log(f'Building additional features between queries and documents')
            self.overlap_feats = self.utils.compute_overlap_features(query_list, doc_list)
        else:
            self.logger.write_log(f'Additional features disabled - building not needed')
            self.overlap_feats = np.zeros(len(query_list))

        # determine max feat len
        if self.overlap_feats.ndim > 1:
            self.addit_feat_len = self.overlap_feats.shape[1]

    def perform_build(self, query_file_path, doc_file_path, additional_feats_enabled):
        self.logger.write_log('Starting building datasets from files...', title='training')
        
        # load datasets including performing pre-processing
        query_list, doc_list = self._prepare_datasets_files(query_file_path, doc_file_path)

        # build the vocabulary based on query-doc lists
        self._build_vocab_docs(query_list, doc_list)

        # re-build the docs and labels
        final_docs, final_labels = self._generate_final_docs_and_labels(query_list, doc_list)

        # generate additional feature list only if needed
        self._generate_additional_feats(query_list, final_docs, additional_feats_enabled)

        # convert texts to sequences
        x_query_list = self._convert_text_to_sequences(query_list, self.max_text_len)
        x_doc_list = self._convert_text_to_sequences(final_docs, self.max_text_len)

        self.query_list = x_query_list
        self.doc_list = x_doc_list
        self.labels_list = np.array(final_labels).astype('int32')

        self.logger.write_log(f'Datasets completed with ({len(query_list)}) lines')