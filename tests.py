from build_nnet import ModelTrainer
from logger import Log
from utils_nnet import ModelCommon
from dataset_parser import DatasetConfig
from run_nnet import SinglePredictor, MultiPredictor

# training part
# model_train = ModelTrainer(embedding_file='data/glove.twitter.27B.200d.txt', epochs=15,
#                            additional_feats_enabled=True, dataset_config=DatasetConfig.USER_STATE)
# model_train.train_model()
# model_train.save_model('model')

# bot_tweet1 = 'RT @seasolshades: @StylishRentals Thank you for following. Merry Christmas https://t.co/y60wJ6iOLV'
# bot_tweet2 = 'Think holiday shopping with the December 2 Remember Giveaway Hop! #Dec2Remember #giveaway #Christmas #holidays https://t.co/x0mleSpexN'
# bot_tweet3 = 'Enter to win a $50 etsy giftcard! Perfect for your holiday handmade shoping! #giveaway thanx @gardendreamsdcr https://t.co/mp8H6c9KVX'
# human_tweet = 'RT @__ 489_: Do not allow my soul to extinguish Lord, I am used to my glow.'

# single tweet test
# input = bot_tweet3
# pred = SinglePredictor('model_user')
# pred.load_model()
# bot_score = pred.predict(input)
#
# print()
# print('Tweet for predict:')
# print(input)
# print()
# print(f'Similarity bot score: {bot_score:.2f}')
# print(f'Similarity human score: {1-bot_score:.2f}')

# muiltiple tweets test
# multi_pred = MultiPredictor('model_user')
# multi_pred.load_model()
# multi_pred.load_file_content(tweet_file='data/COVID.csv', ignore_header=True)
# multi_pred.predict(take_random_tweets=5)
# multi_pred.classify_by_threshold(threshold=0.5)
# bots_part = multi_pred.get_bots_distribution()

import pandas as pd
import numpy as np

def write_to_excel():
    tweets_texts = ['Tweet #1', 'Tweet #2', 'Tweet #3', 'Tweet #4', 'Tweet #5', 'Tweet #6', 'Tweet #7', 'Tweet #8',
                    'Tweet #9', 'Tweet #10', 'Tweet #11', 'Tweet #12']

    bots_scores = [0.1, 0.66, 0.44, 0.32, 0.98, 0.21, 0.88, 0.34, 0.2, 0.3, 0.5, 0.78]
    threshold = 0.5

    # Create a Pandas dataframe from some data.
    df = pd.DataFrame(
        {'Tweet Text': tweets_texts,
         'Bot Score': bots_scores})

    df['Predict'] = ''

    start_row = 2
    for i in range(len(df['Predict'].array)):
        df['Predict'].array[i] = f'=IF(results!C{start_row} >= threshold!A$2, 1, 0)'
        start_row += 1

    df_threshold = pd.DataFrame({'Threshold': [threshold]})

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('C:\\temp\\predict_results.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='results')
    df_threshold.to_excel(writer, sheet_name='threshold', index=False)

    # Access the XlsxWriter workbook and worksheet objects from the dataframe.
    workbook = writer.book

    header_fmt = workbook.add_format({'bold': True})
    writer.sheets['results'].set_row(0, None, header_fmt)
    writer.sheets['threshold'].set_row(0, None, header_fmt)

    #######################################################################
    #
    # Create an area chart with user defined segment colors.
    #

    # Create a new Chart object.
    area_chart = workbook.add_chart({'type': 'area'})

    hist_val, hist_index = np.histogram(bots_scores, range=(0, 1))
    hist_index = hist_index[:-1]

    df_hist = pd.DataFrame({'Scores': hist_index,
                            'Frequency': hist_val})
    df_hist.to_excel(writer, sheet_name='histogram', index=False)

    # Configure the chart.
    area_chart.add_series({'categories': f'=histogram!$A$2:$A${len(hist_index)+1}',
                      'values': f'=histogram!$B$2:$B${len(hist_index)+1}'})

    # Add a chart title and some axis labels.
    area_chart.set_title({'name': 'Histogram of Bot Scores'})
    area_chart.set_x_axis({'name': 'Score'})
    area_chart.set_y_axis({'name': 'Tweets Frequency'})

    # Set an Excel chart style.
    area_chart.set_style(11)

    # Insert the chart into the worksheet (with an offset).
    writer.sheets['histogram'].insert_chart('D1', area_chart, {'x_offset': 25, 'y_offset': 10})

    #######################################################################
    #
    # Create a Pie chart with user defined segment colors.
    #

    df_pie = pd.DataFrame({'Bot': [f'=ROUND(SUM(results!$D$2:$D${len(bots_scores)+1})/{len(bots_scores)} * 100, 0)'],
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

    # Insert the chart into the worksheet (with an offset).
    writer.sheets['pie'].insert_chart('D1', pie_chart, {'x_offset': 25, 'y_offset': 10})

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()


write_to_excel()