from build_nnet import ModelTrainer
from logger import Log

# training part
model_train = ModelTrainer(embedding_file='data/wiki-news-300d-1M.vec', epochs=3 ,additional_feats_enabled=True)
model_train.train_model()
model_train.save_model('model_with_feats_without_validation')