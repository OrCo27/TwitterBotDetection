import string
import re
import numpy as np

class ModelCommon:
    def compute_overlap_features(self, input1, input2):
        feats_overlap = []
        for question, answer in zip(input1, input2):
            q_set = set(question)
            a_set = set(answer)

            word_overlap = q_set.intersection(a_set)

            overlap = float(len(word_overlap)) / (len(q_set) + len(a_set))

            # TODO: adding TF-IDF scoring to addit_feature vector and check if get higher accuracy?
            feats_overlap.append(np.array([overlap]))

        return np.array(feats_overlap)

    def preprocess_tweet(self, text):
        # convert text to lower-case
        nopunc = text.lower()

        # # remove prefixes
        # nopunc = re.sub('^rt', '', nopunc)
        #
        # # remove URLs
        # nopunc = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))', '', nopunc)
        # nopunc = re.sub(r'http\S+', '', nopunc)
        #
        # # replace all digits to zero
        # nopunc = re.sub('(\d+)', '0', nopunc)
        #
        # # remove duplicate spaces
        # nopunc = re.sub('(\s+)', ' ', nopunc)

        # Check characters to see if they are in punctuation
        nopunc = [char for char in nopunc.strip() if char not in string.punctuation]
        # Join the characters again to form the string.
        nopunc = ''.join(nopunc)

        return nopunc.split()