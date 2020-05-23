from utils_nnet import ModelCommon as Utils
from tensorflow.keras.models import load_model
from PyQt5.QtCore import QThread
import pandas as pd
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


class AbstractMultiPredictor(SinglePredictor):
    def __init__(self, model_name, callback_predict, total_tweets):
        super().__init__(model_name, callback_predict)
        self.tweets_text_list = [] # original tweets text
        self.tweets_scores_list = [] # predicts score for each tweet
        self.tweets_class_list = [] # predict classification: 1 for bot, 0 for human
        self.stopped = False
        self.total_tweets = total_tweets

    def need_stop(self):
        self.stopped = True

    def _build_result_sheet(self):
        # Create a Pandas dataframe from some data.
        df_result = pd.DataFrame({'Tweet Text': self.tweets_text_list,
                                  'Bot Score': self.tweets_scores_list,
                                  'Predict': ''})

        start_row = 2
        for i in range(len(df_result['Predict'].array)):
            df_result['Predict'].array[i] = f'=IF(results!C{start_row} >= threshold!A$2, 1, 0)'
            start_row += 1

        return df_result

    def _build_charts_sheets(self, writer):
        pass

    def export_to_excel(self, threshold, file_path):
        # create sheets in excel workbook
        df_result = self._build_result_sheet()
        df_threshold = pd.DataFrame({'Threshold': [threshold]})

        # create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(file_path, engine='xlsxwriter')

        # convert the dataframe to an XlsxWriter Excel object.
        df_result.to_excel(writer, sheet_name='results')
        df_threshold.to_excel(writer, sheet_name='threshold', index=False)

        # Access the XlsxWriter workbook and worksheet objects from the dataframe.
        workbook = writer.book

        # bold the first row on each sheet
        header_fmt = workbook.add_format({'bold': True})
        writer.sheets['results'].set_row(0, None, header_fmt)
        writer.sheets['threshold'].set_row(0, None, header_fmt)

        # build charts on workbook
        self._build_charts_sheets(writer)

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()

    def _load_file_content(self):
        pass

    # predict multiple tweets
    def predict(self):
        # load tweets file
        self._load_file_content()

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
            self.tweets_scores_list.append(sim_bot_score)

    def _check_if_bot(self, score, threshold):
        return 1 if (score >= threshold) else 0

    # create the classification of bots based on threshold
    def classify_by_threshold(self, threshold=0.5):
        self.tweets_class_list = [self._check_if_bot(x, threshold) for x in self.tweets_scores_list]


class MultiPredictor(AbstractMultiPredictor):
    def __init__(self, model_name, callback_predict, tweet_file, ignore_header=False, take_random_tweets=150):
        super().__init__(model_name, callback_predict, take_random_tweets)
        self.tweet_file = tweet_file
        self.ignore_header = ignore_header

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

        # check for overflowing
        if len(tweets_list) >= self.total_tweets:
            self.tweets_text_list = random.sample(tweets_list, self.total_tweets)
        else:
            raise Exception('The Random Tweets you Choose is Bigger Than Number of Tweets in File!')

    def get_hist_values(self):
        hist_val, hist_index = np.histogram(self.tweets_scores_list, range=(0, 1))
        hist_index = hist_index[:-1]
        return hist_val, hist_index

    def _build_charts_sheets(self, writer):
        workbook = writer.book

        # create histogram chart
        area_chart = self._create_histogram_chart(workbook, writer)
        pie_chart = self._create_pie_chart(workbook, writer)

        # Insert the charts into the worksheet (with an offset).
        writer.sheets['histogram'].insert_chart('D1', area_chart, {'x_offset': 25, 'y_offset': 10})
        writer.sheets['pie'].insert_chart('D1', pie_chart, {'x_offset': 25, 'y_offset': 10})

    def _create_histogram_chart(self, workbook, writer):
        # Create a new Chart object.
        area_chart = workbook.add_chart({'type': 'area'})

        hist_val, hist_index = self.get_hist_values()

        df_hist = pd.DataFrame({'Scores': hist_index,
                                'Frequency': hist_val})
        df_hist.to_excel(writer, sheet_name='histogram', index=False)

        # Configure the chart.
        area_chart.add_series({'categories': f'=histogram!$A$2:$A${len(hist_index) + 1}',
                               'values': f'=histogram!$B$2:$B${len(hist_index) + 1}'})

        # Add a chart title and some axis labels.
        area_chart.set_title({'name': 'Histogram of Bot Scores'})
        area_chart.set_x_axis({'name': 'Score'})
        area_chart.set_y_axis({'name': 'Tweets Frequency'})

        # Set an Excel chart style.
        area_chart.set_style(11)

        return area_chart

    def _create_pie_chart(self, workbook, writer):
        df_pie = pd.DataFrame(
            {'Bot': [
                f'=ROUND(SUM(results!$D$2:$D${len(self.tweets_scores_list) + 1})/{len(self.tweets_scores_list)}*100, 0)'],
             'Human': [f'=100-pie!A2']})

        df_pie.to_excel(writer, sheet_name='pie', index=False)

        # Create an example Pie chart like above.
        pie_chart = workbook.add_chart({'type': 'pie'})

        # Configure the series and add user defined segment colors.
        pie_chart.add_series({
            'categories': '=pie!$A$1:$B$1',
            'values': '=pie!$A$2:$B$2',
            'points': [
                {'fill': {'color': '#3498db'}},
                {'fill': {'color': '#a8e6cf'}},
            ],
        })

        # Add a title.
        pie_chart.set_title({'name': 'Prediction Distribution'})

        return pie_chart

    # get the bots distribution in decimal
    def get_bots_distribution(self):
        bot_distribution = len(list(filter(lambda x: x == 1, self.tweets_class_list))) / len(self.tweets_class_list)
        return bot_distribution


class ModelTestPredictor(AbstractMultiPredictor):
    def __init__(self, model_name, callback_predict, bot_file, human_file, bot_total_tweets, human_total_tweets):
        super().__init__(model_name, callback_predict, bot_total_tweets+human_total_tweets)
        self.bot_file = bot_file
        self.human_file = human_file
        self.bot_total_tweets = bot_total_tweets
        self.human_total_tweets = human_total_tweets
        self.tweets_labeled_list = []
        self.part_bot_text_list = []
        self.part_human_text_list = []

    def _load_file_content(self):
        # read all files
        with open(self.bot_file, 'r', encoding='utf-8') as f:
            bot_list = f.readlines()

        with open(self.human_file, 'r', encoding='utf-8') as f:
            human_list = f.readlines()

        # take only part of the bigger list
        if len(bot_list) >= self.bot_total_tweets:
            self.part_bot_text_list = random.sample(bot_list, self.bot_total_tweets)
        else:
            raise Exception('The Random Bot Tweets you Choose is Bigger Than Number of Tweets in File!')

        if len(human_list) >= self.human_total_tweets:
            self.part_human_text_list = random.sample(human_list, self.human_total_tweets)
        else:
            raise Exception('The Random Human Tweets you Choose is Bigger Than Number of Tweets in File!')

        # concatenate two lists into one list
        self.tweets_text_list = self.part_bot_text_list + self.part_human_text_list

        part_bot_labeled = ([1] * self.bot_total_tweets)
        part_human_labeled = ([0] * self.human_total_tweets)

        self.tweets_labeled_list = part_bot_labeled + part_human_labeled

    def _get_accuracy_of_list(self, labeled_list, predict_list):
        matched_cnt = len(list(filter(lambda x: x[0] == x[1], zip(labeled_list, predict_list))))
        matched_score = matched_cnt / len(labeled_list)
        return matched_score

    def get_accuracy_bot_human(self):
        correct_bot_score = self._get_accuracy_of_list(self.tweets_labeled_list[:self.bot_total_tweets],
                                                       self.tweets_class_list[:self.bot_total_tweets])

        correct_human_score = self._get_accuracy_of_list(self.tweets_labeled_list[self.bot_total_tweets:],
                                                         self.tweets_class_list[self.bot_total_tweets:])
        return correct_bot_score, correct_human_score

    def get_accuracy_model(self):
        correct_score = self._get_accuracy_of_list(self.tweets_labeled_list, self.tweets_class_list)
        return correct_score

    def _build_result_sheet(self):
        df_result = super()._build_result_sheet()
        df_result.insert(2, 'Label', self.tweets_labeled_list, True)

        df_result['Matched'] = ''
        start_row = 2
        for i in range(len(df_result['Matched'].array)):
            df_result['Matched'].array[i] = f'=IF(results!D{start_row} >= results!E{start_row}, 1, 0)'
            start_row += 1

        return df_result

    def _build_charts_sheets(self, writer):
        workbook = writer.book

        # create histogram chart
        bar_chart = self._create_bar_chart(workbook, writer)

        # Insert the charts into the worksheet (with an offset).
        writer.sheets['barchart'].insert_chart('D1', bar_chart, {'x_offset': 25, 'y_offset': 10})

    def _create_bar_chart(self, workbook, writer):
        # Create a new Chart object.
        bar_chart = workbook.add_chart({'type': 'column'})

        index = ['Total Tweets', 'Correct Tweets', 'Wrong Tweets', 'Correct Percentage', 'Wrong Percentage']

        # prepare bot column
        bot_col = []
        bot_col.append(self.bot_total_tweets)
        bot_col.append('=COUNTIFS(results!$F$2:$F$26, "=1", results!$D$2:$D$26, "=1")')
        bot_col.append('=summary!$B$2-summary!$B$3')
        bot_col.append('=ROUND(summary!$B$3/summary!$B$2*100, 0)')
        bot_col.append('=100-summary!$B$5')

        # prepare human column
        human_col = []
        human_col.append(self.human_total_tweets)
        human_col.append('=COUNTIFS(results!$F$2:$F$26, "=1", results!$D$2:$D$26, "=0")')
        human_col.append('=summary!$C$2-summary!$C$3')
        human_col.append('=ROUND(summary!$C$3/summary!$C$2*100, 0)')
        human_col.append('=100-summary!$C$5')

        df_col = pd.DataFrame({'Bot': bot_col,
                               'Human': human_col})

        df_col.set_index(index)
        df_col.to_excel(writer, sheet_name='summary', index=True)

        # Configure the first series.
        bar_chart.add_series({
            'name': 'Correct Prediction',
            'categories': '=summary!$B$1:$C$1',
            'values': '=summary!$B$5:$C$5',
            'fill': {'color': '#29ec1e'},
        })

        # Configure the second series.
        bar_chart.add_series({
            'name': 'Wrong Prediction',
            'categories': '=summary!$B$1:$C$1',
            'values': '=summary!$B$6:$C$6',
            'fill': {'color': '#ED213A'},
        })

        # Add a chart title and some axis labels.
        bar_chart.set_title({'name': 'Prediction Result'})
        bar_chart.set_y_axis({'name': 'Percentage (%)'})
        bar_chart.set_legend({'position': 'bottom'})

        # Set an Excel chart style.
        bar_chart.set_style(11)

        return bar_chart


class ExportExcelThread(QThread):
    def __init__(self, predictor, threshold, excel_path, parent=None):
        QThread.__init__(self, parent)
        self.predictor = predictor
        self.threshold = threshold
        self.excel_path = excel_path
        self.error = None

    def is_success(self):
        return self.error is None

    def run(self):
        try:
            self.predictor.export_to_excel(self.threshold, self.excel_path)
        except Exception as ex:
            self.error = ex.args[0]

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
