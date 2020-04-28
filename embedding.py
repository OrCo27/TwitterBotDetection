import time
import pickle
import numpy as np
import os
from os import path
import os.path


class Embedding:
    def __init__(self, logger, embedding_file):
        self.logger = logger
        self.embedding_file = embedding_file
        self.embedding_dim = None
        self.embeddings_matrix = None
        self.embeddings_index = {}

    def _load_embeddings_index_file(self):
        self.logger.write_log(f'Loading embedding file: \'{self.embedding_file}\'')
        start = time.time()
        with open(self.embedding_file, 'r', encoding='utf-8') as f:
            # get the dimension of embedding vector
            first_line = f.readline()
            _, coefs = self._extract_line(first_line)
            self.embedding_dim = coefs.shape[0]

            # seek to the first line
            f.seek(0, 0)

            # extract all embedding vectors from embedding file
            for line in f:
                word, coefs = self._extract_line(line)
                self.embeddings_index[word] = coefs

        self.logger.write_log(f'Loaded in {time.time() - start} seconds')
        self.logger.write_log(f'Found {len(self.embeddings_index)} word vectors.')
        self.logger.write_log(f'Embedding Dimension: {self.embedding_dim}')

    def _extract_line(self, line):
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        return word, coefs

    def _create_embeddings_matrix(self, vocabulary):
        try:
            self.logger.write_log(f'Creating embedding matrix, dim: {len(vocabulary) + 1} x {self.embedding_dim}')
            self.embeddings_matrix = np.random.rand(len(vocabulary) + 1, self.embedding_dim)
            words_not_found = 0

        except Exception as e:
            print(e)

        for i, word in vocabulary.items():
            embedding_vector = self.embeddings_index.get(word)
            if embedding_vector is not None:
                self.embeddings_matrix[i] = embedding_vector
            else:
                words_not_found += 1

        self.logger.write_log(f'Number of words not in trained embedding: {words_not_found}')

    def load_embedding_matrix(self, vocabulary):
        embedding_index_file = os.path.splitext(self.embedding_file)[0] + '.pickle'

        if path.exists(embedding_index_file):
            self.logger.write_log('Trying to load embedding index from npy dump.')
            with open(embedding_index_file, 'rb') as f:
                self.embeddings_index, self.embedding_dim = pickle.load(f)
        else:
            self.logger.write_log('Load from dump failed, reading from embedding file.')
            # load embedding vectors and create embedding matrix
            self._load_embeddings_index_file()
            with open(embedding_index_file, 'wb') as f:
                pickle.dump([self.embeddings_index, self.embedding_dim], f)

        # load embedding vectors and create embedding matrix
        self._create_embeddings_matrix(vocabulary)

        return self.embeddings_matrix