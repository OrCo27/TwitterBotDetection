from build_nnet import ModelTrainer
from logger import Log
from utils_nnet import ModelCommon
from dataset_parser import DatasetConfig

# training part
model_train = ModelTrainer(embedding_file='data/glove.twitter.27B.200d.txt', epochs=3,
                           additional_feats_enabled=True, dataset_config=DatasetConfig.USER_STATE)
model_train.train_model()
model_train.save_model('model')