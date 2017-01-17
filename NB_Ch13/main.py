#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 22:20:52 2017

@author: carlosjarguello
"""

import glob, re
import NB_Classifier_CH13 as nb_class
from collections import Counter

data = []
path = r'*/*'

for fn in glob.glob(path):
    is_spam = 'ham' not in fn
    with open(fn,'r') as file:
        for line in file:
            if line.startswith('Subject:'):
                subject = re.sub(r'^Subject: ', '', line).strip()
                data.append((subject, is_spam))
                
import random

random.seed(0)
random.shuffle(data)
train_data, test_data = data[:int(len(data)*0.75)], data[int(len(data)*0.75):]

classifier = nb_class.NBClassifier()
classifier.train(train_data)
classified = [(subject, is_spam, classifier.classifier(subject)) for 
              subject, is_spam in test_data]

counts =  Counter((is_spam, spam_probability > 0.5) for _, is_spam, 
                  spam_probability in classified)

print counts
classified.sort(key = lambda row: row[2])

spammiest_hams = filter(lambda row: not row[1], classified)[-5:]
hammiest_spams = filter(lambda row: row[1], classified)[:5]

print spammiest_hams
print hammiest_spams

def p_spam_given_word(word_prob):
    
    word, prob_if_spam, prob_if_not_spam = word_prob
    return prob_if_spam/(prob_if_spam + prob_if_not_spam)

words = sorted(classifier.word_probs, key = p_spam_given_word)

spammiest_words = words[-5:]
hammiest_words = words[:5]

print hammiest_words
print spammiest_words
    