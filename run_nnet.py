from utils_nnet import ModelCommon as utils
from tensorflow.keras.models import load_model
import numpy as np
import os
import pickle
import csv
import random

class SinglePredictor:
    def __init__(self, model_name):
        self.model_name = model_name
        # load model parameters
        self.model = None
        self.tokenizer = None
        self.max_text_len = None
        self.x_bot_list = []
        self.bot_list = []

    # predict bot similarity score on a single tweet
    def predict(self, tweet_pred):
        # perform pre-processing
        clean_tweet_pred = utils.preprocess_tweet(tweet_pred)

        # build doc list by duplicate tweet prediction foreach line in bot list
        tweet_pred_list = [clean_tweet_pred] * len(self.bot_list)

        # convert tweet predicted to sequence
        temp_pred_list = [clean_tweet_pred]
        x_temp_pred_list = utils.convert_text_to_sequences(self.tokenizer, temp_pred_list, self.max_text_len)

        # duplicate sequence to the length of bot size list
        x_doc_list = [x_temp_pred_list[0]] * len(self.bot_list)
        x_doc_list = np.array(x_doc_list)

        # calculate word overlapping additional feature
        additional_feat = utils.compute_overlap_features(self.bot_list, tweet_pred_list)

        predict_list = self.model.predict([self.x_bot_list, x_doc_list, additional_feat], verbose=1)

        bot_similarity_score = len(list(filter(lambda x: x > 0.5, predict_list)))/len(predict_list)

        return bot_similarity_score

    def load_model(self):
        full_path = os.path.join('output', self.model_name)
        model_path = full_path + '.h5'
        pickle_path = full_path + '.pickle'

        model = load_model(model_path)
        with open(pickle_path, 'rb') as f:
            x_bot_list, bot_list, tokenizer, max_text_len = pickle.load(f)

        self.model = model
        self.x_bot_list = x_bot_list
        self.bot_list = bot_list
        self.tokenizer = tokenizer
        self.max_text_len = max_text_len


class MultiPredictor(SinglePredictor):
    def __init__(self, model_name):
        super().__init__(model_name)
        self.tweets_text_list = [] # original tweets text
        self.tweets_preds_list = [] # predicts score for each tweet
        self.tweets_bot_class = [] # 1 for bot, 0 for human

    # loads txt and csv file
    # NOTE: csv file must include only one column with tweet content
    def load_file_content(self, tweet_file, ignore_header=False):
        tweets_list = []

        if tweet_file.endswith('.txt'):
            with open(tweet_file, 'r', encoding='utf-8') as f:
                tweets_list = f.readlines()

        elif tweet_file.endswith('.csv'):
            with open(tweet_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    tweets_list.append(row[0])

        if ignore_header:
            tweets_list.remove(tweets_list[0])

        self.tweets_text_list = tweets_list

    # predict multiple tweets from specific file
    def predict(self, take_random_tweets=150):
        if len(self.tweets_text_list) > take_random_tweets:
            self.tweets_text_list = random.sample(self.tweets_text_list, take_random_tweets)

        for tweet in self.tweets_text_list:
            sim_bot_score = super().predict(tweet)
            self.tweets_preds_list.append(sim_bot_score)

    def _check_if_bot(self, score, threshold):
        return 1 if (score >= threshold) else 0

    # create the classification of bots based on threshold
    def classify_by_threshold(self, threshold=0.5):
        self.tweets_bot_class = [self._check_if_bot(x, threshold) for x in self.tweets_preds_list]

    # get the bots distribution in decimal
    def get_bots_distribution(self):
        bot_distribution = len(list(filter(lambda x: x == 1, self.tweets_bot_class))) / len(self.tweets_bot_class)
        return bot_distribution
