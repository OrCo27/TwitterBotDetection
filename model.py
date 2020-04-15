from tensorflow.keras import optimizers, regularizers
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.layers import Input, Embedding
from tensorflow.keras.layers import Conv1D, GlobalMaxPooling1D
from tensorflow.keras.layers import concatenate, Dot
from tensorflow.keras.models import Model

class RankingModel:
    def __init__(self, logger, max_text_len, addit_feat_len, embedding_matrix,
                 dropout_rate=0.25, no_conv_filters = 100):

        self.logger = logger
        self.max_text_len = max_text_len
        self.addit_feat_len = addit_feat_len
        self.dropout_rate = dropout_rate
        self.no_conv_filters = no_conv_filters
        self.embedding_matrix = embedding_matrix

    def _build_sentence_model(self, input_name):
        # add input layer as first
        input = Input(shape=(self.max_text_len,),
                      name=str.format(f'{input_name}_input'))

        # we will load embedding values from corpus here.
        embed = Embedding(input_dim=self.embedding_matrix.shape[0],
                          output_dim=self.embedding_matrix.shape[1],
                          input_length=self.max_text_len,
                          weights=[self.embedding_matrix],
                          name=str.format(f'{input_name}_embed'),
                          trainable=False)(input)

        # add convolutional layer
        conv = Conv1D(filters=self.no_conv_filters,
                      kernel_size=5,
                      strides=1,
                      padding='same',
                      activation='relu',
                      kernel_regularizer=regularizers.l2(1e-5),
                      name=str.format(f'{input_name}_conv'))(embed)

        # add some dropout rate for prevent overfitting
        conv = Dropout(self.dropout_rate)(conv)

        x_pool = GlobalMaxPooling1D(name=str.format(f'{input_name}_pool'))(conv)

        return input, x_pool

    def build_model(self):
        self.logger.write_log(f'Building Ranking short text model using CNN...')

        # Prepare layers for query input as sentence model
        q_input, q_pool = self._build_sentence_model('query')

        # Prepare layers for document input as sentence model
        d_input, d_pool = self._build_sentence_model('document')

        # Input additional features.
        input_addn_feat = Input(shape=(self.addit_feat_len,),
                                name='input_addn_feat')

        # Prepare similarity layer between queries and documents
        x_d = Dense(self.no_conv_filters,
                         use_bias=False,
                         kernel_regularizer=regularizers.l2(1e-4))(d_pool)

        sim = Dot(axes=-1)([q_pool, x_d])

        # Combine query, sim, document pooled outputs and additional input features
        join_layer = concatenate([q_pool, sim, d_pool, input_addn_feat])

        # Calculate numbers of hidden units
        hidden_units = self.no_conv_filters*2 + self.addit_feat_len + 1

        # TODO: maybe need adding relu here too?
        hidden_layer = Dense(hidden_units,
                             kernel_regularizer=regularizers.l2(1e-4))(join_layer)

        hidden_layer = Dropout(self.dropout_rate)(hidden_layer)

        # Final softmax layer
        softmax = Dense(1, activation='sigmoid')(hidden_layer)

        model = Model(inputs=[q_input, d_input, input_addn_feat],
                      outputs=softmax)
        # optimizers.Adadelta(rho=0.95, epsilon=1e-06)
        model.compile(optimizer='adam',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])

        self.logger.write_log(model.summary(), timestamp=False)

        return model