from utils_nnet import ModelCommon as utils
from tensorflow.keras.models import load_model
import numpy as np
import os
import pickle


class ModelPredicter:
    def __init__(self, model_name):
        self.model_name = model_name

    def predict(self, tweet_pred):
        # load model parameters
        model, x_bot_list, bot_list, tokenizer, max_text_len = self._load_model()

        # perform pre-processing
        clean_tweet_pred = utils.preprocess_tweet(tweet_pred)

        # build doc list by duplicate tweet prediction foreach line in bot list
        tweet_pred_list = [clean_tweet_pred] * len(bot_list)

        # convert tweet predicted to sequence
        temp_pred_list = [clean_tweet_pred]
        x_temp_pred_list = utils.convert_text_to_sequences(tokenizer, temp_pred_list, max_text_len)

        # duplicate sequence to the length of bot size list
        x_doc_list = [x_temp_pred_list[0]] * len(bot_list)
        x_doc_list = np.array(x_doc_list)

        # calculate word overlapping additional feature
        additional_feat = utils.compute_overlap_features(bot_list, tweet_pred_list)

        predict_list = model.predict([x_bot_list, x_doc_list, additional_feat], verbose=1)

        bot_similarity_score = len(list(filter(lambda x: x > 0.5, predict_list)))/len(predict_list)

        return bot_similarity_score

    def _load_model(self):
        full_path = os.path.join('output', self.model_name)
        model_path = full_path + '.h5'
        pickle_path = full_path + '.pickle'

        model = load_model(model_path)
        with open(pickle_path, 'rb') as f:
            x_bot_list, bot_list, tokenizer, max_text_len = pickle.load(f)

        return model, x_bot_list, bot_list, tokenizer, max_text_len
