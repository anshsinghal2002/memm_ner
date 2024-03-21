# Named Entity Recognition for Spanish Corpora

## Author
Ansh Singhal  
Union College  
singhala@union.edu

## Abstract
This project aims to create and evaluate two types of named entity recognizers for a Spanish corpus. One approach treats assigning tags to words as a classification task, while the other employs a Maximum Entropy Markov Model to consider the tag associated with the previous word when predicting the next tag in a sentence.

## Introduction
Named Entity Recognition (NER) is a Natural Language Processing task that involves finding and classifying named entities in text. This project develops two NER models for Spanish text: one based on classification and the other on sequence tagging using a Maximum Entropy Markov Model.

## NER as a Classification Task
The first NER model extracts features from each word in a sentence and uses a Logistic Regression classifier to assign tags. The selected features for each word include the word itself, whether the first letter is capitalized, and whether the word contains any numbers. The performance of this model is evaluated based on precision, recall, and F-score.

## NER as a Sequence Tagging Task
The second NER model extends the first by considering the tag of the previous word in addition to the word features. A Maximum Entropy Markov Model is used to calculate the probability of each label given the word features and the previous tag. The Viterbi algorithm is employed to predict the most probable sequence of tags. The performance of this model is also evaluated based on precision, recall, and F-score.

## Results
The sequence tagging approach using the Maximum Entropy Markov Model demonstrated improved performance over the classification-based approach, with higher precision, recall, and F-score values on both the development and test sets.

## Conclusion
This project successfully developed and evaluated two NER models for Spanish text, demonstrating the effectiveness of incorporating sequential information through a Maximum Entropy Markov Model in improving NER performance.
