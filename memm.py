"""Named Entity Recognition as a classification task.

Author: Kristina Striegnitz and Ansh Singhal

I affirm that I have carried out my academic endeavors with full
academic honesty. Ansh Singhal


Complete this file for part 2 of the project.
"""


class MEMM:
    def __init__(self, states, vectorizer, classifier,vocabulary={}):
        """Save the components that define a Maximum Entropy Markov Model: set of
        states, vocabulary, and the classifier information.
        """
        self.states = states
        self.vectorizer = vectorizer
        self.clf = classifier

    def log_probs(self, features, tag_last):
        features['-1tag'] = tag_last
        # Fit to vectorizer
        feature_vector = self.vectorizer.transform(features)
        #  method predict log proba, which given a feature vector, returns a vector 
        #  containing probabilities for all possible class labels.
        return self.clf.predict_log_proba(feature_vector)[0]
        