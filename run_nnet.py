from utils_nnet import ModelCommon as Utils
from tensorflow.keras.models import load_model
from PyQt5.QtCore import QThread
import numpy as np
import os
import pickle
import csv
import random
import glob

class SinglePredictor:
    def __init__(self, model_name, callback_predict, tweet_pred=None):
        self.model_name = model_name
        self.callback_predict = callback_predict
        # load model parameters
        self.model = None
        self.tokenizer = None
        self.max_text_len = None
        self.x_bot_list = []
        self.bot_list = []
        self.additional_feats_enabled = True
        self.tweet_pred = tweet_pred
        self.bot_similarity_score = 0

    def set_single_tweet(self, tweet_pred):
        self.tweet_pred = tweet_pred

    def get_similarity_score(self):
        return self.bot_similarity_score

    # predict bot similarity score on a single tweet
    def predict(self):
        if self.tweet_pred is None:
            raise Exception('Can not Start Predicting without any Prediction Tweet!')

        # perform pre-processing
        clean_tweet_pred = Utils.preprocess_tweet(self.tweet_pred)

        # build doc list by duplicate tweet prediction foreach line in bot list
        tweet_pred_list = [clean_tweet_pred] * len(self.bot_list)

        # convert tweet predicted to sequence
        temp_pred_list = [clean_tweet_pred]
        x_temp_pred_list = Utils.convert_text_to_sequences(self.tokenizer, temp_pred_list, self.max_text_len)

        # duplicate sequence to the length of bot size list
        x_doc_list = [x_temp_pred_list[0]] * len(self.bot_list)
        x_doc_list = np.array(x_doc_list)

        # calculate word overlapping additional feature
        if self.additional_feats_enabled:
            additional_feat = Utils.compute_overlap_features(self.bot_list, tweet_pred_list)
        else:
            additional_feat = np.zeros(len(self.bot_list))

        # perform the prediction operation
        predict_list = self.model.predict([self.x_bot_list, x_doc_list, additional_feat],
                                          verbose=1, callbacks=[self.callback_predict])

        # calculate and save the how much current tweet similar to training bots list
        self.bot_similarity_score = len(list(filter(lambda x: x > 0.5, predict_list))) / len(predict_list)

    @staticmethod
    def get_models_names():
        model_files = glob.glob('output/*.h5')
        fixed_files = list(map(lambda x: os.path.basename(x).split('.')[0], model_files))
        return fixed_files

    def load_model(self):
        full_path = os.path.join('output', self.model_name)
        model_path = full_path + '.h5'
        pickle_path = full_path + '.pickle'

        model = load_model(model_path)
        with open(pickle_path, 'rb') as f:
            x_bot_list, bot_list, tokenizer, max_text_len, additional_feats_enabled = pickle.load(f)

        self.model = model
        self.x_bot_list = x_bot_list
        self.bot_list = bot_list
        self.tokenizer = tokenizer
        self.max_text_len = max_text_len
        self.additional_feats_enabled = additional_feats_enabled


class MultiPredictor(SinglePredictor):
    def __init__(self, model_name, callback_predict, tweet_file, ignore_header=False, take_random_tweets=150):
        super().__init__(model_name, callback_predict)
        self.tweets_text_list = [] # original tweets text
        self.tweets_preds_list = [] # predicts score for each tweet
        self.tweets_bot_class = [] # 1 for bot, 0 for human
        self.tweet_file = tweet_file
        self.ignore_header = ignore_header
        self.take_random_tweets = take_random_tweets
        self.stopped = False

    def need_stop(self):
        self.stopped = True

    # loads txt and csv file
    # NOTE: csv file must include in the first column the tweet content
    def _load_file_content(self):
        tweets_list = []

        # case for txt file - read directly all lines
        if self.tweet_file.endswith('.txt'):
            with open(self.tweet_file, 'r', encoding='utf-8') as f:
                tweets_list = f.readlines()

        # case for csv file - read the first column as tweet content
        elif self.tweet_file.endswith('.csv'):
            with open(self.tweet_file, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    tweets_list.append(row[0])

        if self.ignore_header:
            tweets_list.remove(tweets_list[0])

        self.tweets_text_list = tweets_list

    # predict multiple tweets from specific file
    def predict(self):
        # load tweets file
        self._load_file_content()

        # check for overflowing
        if len(self.tweets_text_list) > self.take_random_tweets:
            self.tweets_text_list = random.sample(self.tweets_text_list, self.take_random_tweets)
        else:
            raise Exception('The Random Tweets you Choose is Bigger Than Number of Tweets in File!')

        # pass for each tweet in the file and perform predicting
        for tweet in self.tweets_text_list:
            if self.stopped:
                break

            # set current tweet text for prediction
            super().set_single_tweet(tweet)
            # perform a single prediction for current tweet
            super().predict()
            # get the similarity score for current tweet
            sim_bot_score = super().get_similarity_score()
            # add the score to predictions list
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


class ModelPredictorThread(QThread):
    def __init__(self, predictor, parent=None):
        QThread.__init__(self, parent)
        self.predictor = predictor
        self.error = None

    def is_success(self):
        return self.error is None

    def run(self):
        try:
            self.predictor.load_model()
            self.predictor.predict()
        except Exception as ex:
            self.error = ex.args[0]
