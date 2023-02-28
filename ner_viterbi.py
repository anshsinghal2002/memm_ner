"""Named Entity Recognition as a sequence tagging task.

Author: Kristina Striegnitz and Ansh Singhal

I affirm that I have carried out my academic endeavors with full
academic honesty. Ansh Singhal

Complete this file for part 2 of the project.
"""
from nltk.corpus import conll2002
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_fscore_support

import math
import numpy as np
# TODO (optional): Complete the class MEMM
from memm import MEMM

#################################
#
# Word classifier
#
#################################

def getfeats(word, o):
    """Take a word its offset with respect to the word we are trying to
    classify. Return a list of tuples of the form (feature_name,
    feature_value).
    """
    o = str(o)
    features = [
        (o + 'word', word),
        (o + 'is_cap',word[0].isupper()),
        (o + 'is_num', True in [i.isnumeric() for i in word])
    ]
    return features
    

def word2features(sent, i):
    """Generate all features for the word at position i in the
    sentence. The features are based on the word itself as well as
    neighboring words.
    """
    features = []
    # the window around the token
    for o in [-1,0,1]:
        if i+o >= 0 and i+o < len(sent):
            word = sent[i+o][0]
            featlist = getfeats(word, o)
            features.extend(featlist)
    return features


#################################
#
# Viterbi decoding
#
#################################

def viterbi(obs, memm, pretty_print=False):
    V = []
    V.append(memm.log_probs(obs[0], '<S>'))
    paths = np.array([[i] for i in range(len(memm.states))])

    # Run Viterbi for all of the subsequent steps/observations: t > 0.
    for t in range(1, len(obs)):
        trans_probs = V[t-1] + np.array([memm.log_probs(obs[t],i) for i in memm.states]).T
        V.append(np.max(trans_probs, axis=1))

        max_prev_states = np.argmax(trans_probs, axis=1)
        paths = np.insert(paths[max_prev_states], t, range(len(memm.states)), axis=1)

    if pretty_print:
        pretty_print_trellis(V)

    final_state = np.argmax(V[-1])
    return [memm.states[i] for i in paths[final_state]]


def pretty_print_trellis(V):
    """Prints out the Viterbi trellis formatted as a grid."""
    print("    ", end=" ")
    for i in range(len(V)):
        print("%7s" % ("%d" % i), end=" ")
    print()
 
    for y in V[0].keys():
        print("%.5s: " % y, end=" ")
        for t in range(len(V)):
            print("%.7s" % ("%f" % V[t][y]), end=" ")
        print()

if __name__ == "__main__":
    print("\nLoading the data ...")
    train_sents = list(conll2002.iob_sents('esp.train'))
    dev_sents = list(conll2002.iob_sents('esp.testa'))
    test_sents = list(conll2002.iob_sents('esp.testb'))

    print("\nTraining ...")
    train_feats = []
    train_labels = []

    for sent in train_sents:
        for i in range(len(sent)):
            feats = dict(word2features(sent, i))
            if i == 0:
                feats["-1tag"] = "<S>"
            else:
                feats["-1tag"] = sent[i - 1][2]

            train_feats.append(feats)
            train_labels.append(sent[i][-1])
    # The vectorizer turns our features into vectors of numbers.
    vectorizer = DictVectorizer()
    X_train = vectorizer.fit_transform(train_feats)
    # Not normalizing or scaling because the example feature is
    # binary, i.e. values are either 0 or 1.

    model = LogisticRegression(max_iter=400)
    model.fit(X_train, train_labels)
    memm = MEMM(model.classes_,vectorizer,model)
    print("\nTesting ...")
    # While developing use the dev_sents. In the very end, switch to
    # test_sents and run it one last time to produce the output file
    # results_memm.txt. That is the results_memm.txt you should hand
    # in. 
    y_pred = []
    for sent in dev_sents:
        # TODO: extract the feature representations for the words from
        # the sentence; use the viterbi algorithm to predict labels
        # for this sequence of words; add the result to y_pred.Use 
        # model.predict_log_proba(feature) which returns P(t_i | f(w_i))
        # where t is i'th tag and f(w_i) is features of i'th word
        # for all possible tags. For the first word in each sentence, 
        # assume that the tag ti−1 is <S>.
        # sent_features = []
        # for i in range(0,len(sent)):
            
        observations = [dict(word2features(sent, i)) for i in range(len(sent))]
        y_pred.extend(viterbi(observations, memm))

    print("Writing to results_memm.txt")
    # format is: word gold pred
    j = 0
    with open("results_memm.txt", "w") as out:
        for sent in dev_sents: 
            for i in range(len(sent)):
                word = sent[i][0]
                gold = sent[i][-1]
                pred = y_pred[j]
                j += 1
                out.write("{}\t{}\t{}\n".format(word,gold,pred))
        out.write("\n")

    print("Now run: python3 conlleval.py results_memm.txt")






