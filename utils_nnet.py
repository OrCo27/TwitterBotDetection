import string
import re
import numpy as np

class ModelCommon:
    @staticmethod
    def compute_overlap_features(input1, input2):
        feats_overlap = []
        for question, answer in zip(input1, input2):
            q_set = set(question)
            a_set = set(answer)

            word_overlap = q_set.intersection(a_set)

            overlap = float(len(word_overlap)) / (len(q_set) + len(a_set))

            # TODO: adding TF-IDF scoring to addit_feature vector and check if get higher accuracy?
            feats_overlap.append(np.array([overlap]))

        return np.array(feats_overlap)

    @staticmethod
    def get_user_from_tweet(tweet):
        user = None
        re_user = re.search('^RT @\s*(?P<user>.+?):', tweet, re.IGNORECASE)
        if re_user:
            user = re_user.group('user')
        return user

    @staticmethod
    def preprocess_tweet(text):
        # convert text to lower-case
        nopunc = text.lower().strip()

        # remove prefixes and users tags
        nopunc = re.sub('^RT @\s*(.+?)(:|\b)|@(.+?)\b', '', nopunc, flags=re.IGNORECASE)

        # remove enojies
        nopunc = nopunc.encode('ascii', 'ignore').decode('ascii')

        # remove URLs
        nopunc = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))', '', nopunc, flags=re.IGNORECASE)
        nopunc = re.sub(r'http\S+', '', nopunc, flags=re.IGNORECASE)

        # remove all digits
        nopunc = re.sub('(\d+)', '', nopunc)

        # remove duplicate spaces
        nopunc = re.sub('(\s+)', ' ', nopunc)

        # Check characters to see if they are in punctuation
        nopunc = [char for char in nopunc.strip() if char not in string.punctuation]
        # Join the characters again to form the string.
        nopunc = ''.join(nopunc)

        return nopunc.split()
