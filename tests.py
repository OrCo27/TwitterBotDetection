from build_nnet import ModelTrainer
from logger import Log
from utils_nnet import ModelCommon
from dataset_parser import DatasetConfig
from run_nnet import SinglePredictor, MultiPredictor

# training part
# model_train = ModelTrainer(embedding_file='data/glove.twitter.27B.200d.txt', epochs=5,
#                            additional_feats_enabled=True, dataset_config=DatasetConfig.USER_STATE)
# model_train.train_model()
# model_train.save_model('model')

bot_tweet1 = 'RT @seasolshades: @StylishRentals Thank you for following. Merry Christmas https://t.co/y60wJ6iOLV'
bot_tweet2 = 'Think holiday shopping with the December 2 Remember Giveaway Hop! #Dec2Remember #giveaway #Christmas #holidays https://t.co/x0mleSpexN'
bot_tweet3 = 'Enter to win a $50 etsy giftcard! Perfect for your holiday handmade shoping! #giveaway thanx @gardendreamsdcr https://t.co/mp8H6c9KVX'
human_tweet = 'RT @__ 489_: Do not allow my soul to extinguish Lord, I am used to my glow.'

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
multi_pred = MultiPredictor('model_user')
multi_pred.load_model()
multi_pred.load_file_content(tweet_file='data/COVID.csv', ignore_header=True)
multi_pred.predict(take_random_tweets=5)
multi_pred.classify_by_threshold(threshold=0.7)
bots_part = multi_pred.get_bots_distribution()