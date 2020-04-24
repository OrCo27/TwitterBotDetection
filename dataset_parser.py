from utils_nnet import ModelCommon as utils
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
import random


# enum for possible dataset configuration
class DatasetConfig:
    RANDOM_STATE = [0, 'random']  # select random pairs from the whole dataset
    USER_STATE = [1, 'user']      # select pairs from each user


class DatasetBuilder:
    def __init__(self, logger, dataset_config=DatasetConfig.USER_STATE):
        self.tokenizer = Tokenizer()
        self.logger = logger
        self.config_id, self.config_name = dataset_config
        self.max_text_len = 0
        self.addit_feat_len = 1
        self.query_list = []
        self.doc_list = []
        self.overlap_feats = []
        self.labels_list = []

    def perform_build(self, query_file_path, doc_file_path, additional_feats_enabled):
        self.logger.write_log('Starting building datasets from files...', title='training')

        # load all datasets from files
        query_list = self._load_file(query_file_path)
        doc_list = self._load_file(doc_file_path)

        # build final triples by users resolution
        if self.config_id == DatasetConfig.USER_STATE[0]:
            users_dict = self._build_users_dict(query_list)
            final_bots, final_docs, final_labels = self._generate_dataset_users(users_dict, query_list, doc_list)
        # build final triples by random state
        else:
            final_bots, final_docs, final_labels = self._generate_dataset_random(query_list, doc_list)

        # build the vocabulary based on query-doc lists
        self.max_text_len = self._build_vocab_docs(final_bots, final_docs)

        # generate additional feature list only if needed
        self._generate_additional_feats(final_bots, final_docs, additional_feats_enabled)

        self.query_list = final_bots
        self.doc_list = final_docs
        self.labels_list = np.array(final_labels).astype('int32')

        self.logger.write_log(f'Datasets completed with ({len(query_list)}) lines')

    def _load_file(self, file_name):
        self.logger.write_log(f'Loading file: \'{file_name}\'')
        with open(file_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return lines

    def _get_maxlen(self, text_list):
        return max(map(lambda x: len(x), text_list))

    # build the vocabulary based on all queries and documents
    def _build_vocab_docs(self, query_list, doc_list):
        self.logger.write_log(f'Building the vocabulary based on queries and documents')

        # insert all docs to vocab
        docs = query_list + doc_list
        self.tokenizer.fit_on_texts(docs)
        max_len = self._get_maxlen(docs)
        self.logger.write_log(f'founded {len(self.tokenizer.word_index)} words, max len: {max_len}')

        return max_len

    # query_file is list of queries before pre-processing
    def _build_users_dict(self, query_file):
        self.logger.write_log(f'Building dictionary of each user and its tweets')

        curr_user = None
        users_dict = {}  # dictionary of lists
        for line in query_file:
            user = utils.get_user_from_tweet(line)

            if user is not None:  # found tweet with username
                curr_user = user

            if curr_user is not None:
                if curr_user not in users_dict:  # it's the first tweet of this user, add it
                    users_dict[curr_user] = [line]
                else:
                    users_dict[curr_user].append(line)
                # elif line not in users_dict[curr_user]:  # append to exists user only if not exists
                #     users_dict[curr_user].append(line)

        return users_dict

    # performing pre-processing and return if there length are valid
    def _perform_pre_processing(self, bot_tweet, doc_tweet, length_valid=3):
        bot_tweet = utils.preprocess_tweet(bot_tweet)
        doc_tweet = utils.preprocess_tweet(doc_tweet)
        length_valid = True \
            if (len(bot_tweet) >= length_valid and len(doc_tweet) >= length_valid) \
            else False

        return bot_tweet, doc_tweet, length_valid

    # build queries and docs pairs by user resolution
    def _generate_dataset_users(self, users_dict, bot_lines, human_lines):
        self.logger.write_log(f'Generating final dataset with appropriate candidates...')

        final_bots = []
        final_docs = []
        final_labels = []

        for user in users_dict:
            items_count = len(users_dict[user])
            # current user have only one tweet, pair to random human tweet
            if items_count == 1:
                bot_tweet = users_dict[user][0]
                doc_tweet = random.choice(human_lines)

                bot_tweet, doc_tweet, length_valid = self._perform_pre_processing(bot_tweet, doc_tweet)

                if length_valid:
                    final_bots.append(bot_tweet)
                    final_docs.append(doc_tweet)
                    final_labels.append(0)
            else:  # user have more than one tweet, iterate them and random choose from bot or human source
                list_items = list(range(0, items_count))
                for i in range(items_count):
                    curr_tweet = users_dict[user][i]

                    # remove current index, so it will not select again
                    if i in list_items:
                        list_items.remove(i)

                    if len(list_items) == 0:  # select from human source
                        doc_tweet = random.choice(human_lines)
                        label = 0
                    else:  # select from bot user list
                        candidate_random_index = random.choice(list_items)
                        doc_tweet = users_dict[user][candidate_random_index]
                        # remove selected index that it will not select again
                        list_items.remove(candidate_random_index)

                        # if pairs are not equals, select from own list
                        if doc_tweet != curr_tweet:
                            label = 1
                        else:  # pairs are equals, choose from humans tweets
                            doc_tweet = random.choice(human_lines)
                            label = 0

                    curr_tweet, doc_tweet, length_valid = self._perform_pre_processing(curr_tweet, doc_tweet)
                    if length_valid:
                        final_bots.append(curr_tweet)
                        final_docs.append(doc_tweet)
                        final_labels.append(label)

        return final_bots, final_docs, final_labels

    def _generate_additional_feats(self, query_list, doc_list, additional_feats_enabled):
        if additional_feats_enabled:
            self.logger.write_log(f'Building additional features between queries and documents')
            self.overlap_feats = utils.compute_overlap_features(query_list, doc_list)
        else:
            self.logger.write_log(f'Additional features disabled - building not needed')
            self.overlap_feats = np.zeros(len(query_list))

        # determine max feat len
        if self.overlap_feats.ndim > 1:
            self.addit_feat_len = self.overlap_feats.shape[1]

    # generate docs pairs from the whole bots source
    def _generate_dataset_random(self, query_list, doc_list):
        self.logger.write_log(f'Generating final dataset with appropriate candidates...')

        # create temporary labels for each list
        query_labels = [1] * len(query_list)
        doc_labels = [0] * len(doc_list)

        # create pairs of (text, label)
        query_labels_pairs = list(zip(query_list, query_labels))
        doc_labels_pairs = list(zip(doc_list, doc_labels))

        # concrate two lists and shuffle them
        pairs_mixed = query_labels_pairs + doc_labels_pairs
        # random.shuffle(pairs_mixed)

        # find for each original query an element from pairs_shuffle
        # so if it will be from the same query collection it will get label=1 (similar)
        # and else it will get label=0 (different)
        final_bots, final_docs, final_labels = [], [], []
        for i in range(len(query_list)):
            # select a random pair from the collection
            rand_doc = random.choice(pairs_mixed)
            doc_tweet, label = rand_doc
            bot_tweet = query_list[i]

            bot_tweet, doc_tweet, length_valid = self._perform_pre_processing(bot_tweet, doc_tweet)
            if length_valid:
                final_bots.append(bot_tweet)
                final_docs.append(doc_tweet)
                final_labels.append(label)

        return final_bots, final_docs, final_labels
