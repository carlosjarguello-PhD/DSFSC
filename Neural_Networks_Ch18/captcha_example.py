#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 13:45:38 2017

@author: carlosjarguello

Following Grus' data science book - Ch 18, Neural networks
"""

import numpy as np
import random
from xor import feed_forward

def backpropagate(network, input_vector, targets):
    
    hidden_outputs, outputs = feed_forward(network, input_vector)
    
    output_deltas = [output*(1-output)*(output - target) for output, target in 
                     zip(outputs, targets)]
    
    for i, output_neuron in enumerate(network[-1]):
        for j, hidden_output in enumerate(hidden_outputs + [1]):
            output_neuron[j] -= output_deltas[i]*hidden_output
            
    hidden_deltas = [hidden_output * (1-hidden_output)*
                     np.dot(np.array(output_deltas), np.array([n[i] for n in output_layer]))
                     for i, hidden_output in enumerate(hidden_outputs)]
                     
    for i, hidden_neuron in enumerate(network[0]):
        for j, input_v in enumerate(input_vector + [1]):
            hidden_neuron[j] -= hidden_deltas[i] * input_v
            
#######

inputs = [[] for _ in range(10)] 
inputs[0] = [1,1,1,1,1,
             1,0,0,0,1,
             1,0,0,0,1,
             1,0,0,0,1,
             1,1,1,1,1]
inputs[1] = [0,0,1,0,0,
             0,0,1,0,0,
             0,0,1,0,0,
             0,0,1,0,0,
             0,0,1,0,0]
inputs[2] = [1,1,1,1,1,
             0,0,0,0,1,
             1,1,1,1,1,
             1,0,0,0,0,
             1,1,1,1,1]
inputs[3] = [1,1,1,1,1,
             0,0,0,0,1,
             1,1,1,1,1,
             0,0,0,0,1,
             1,1,1,1,1]
inputs[4] = [1,0,0,0,1,
             1,0,0,0,1,
             1,1,1,1,1,
             0,0,0,0,1,
             0,0,0,0,1]
inputs[5] = [1,1,1,1,1,
             1,0,0,0,0,
             1,1,1,1,1,
             0,0,0,0,1,
             1,1,1,1,1]
inputs[6] = [1,1,1,1,1,
             1,0,0,0,0,
             1,1,1,1,1,
             1,0,0,0,1,
             1,1,1,1,1]
inputs[7] = [1,1,1,1,1,
             0,0,0,0,1,
             0,0,0,0,1,
             0,0,0,0,1,
             0,0,0,0,1]
inputs[8] = [1,1,1,1,1,
             1,0,0,0,1,
             1,1,1,1,1,
             1,0,0,0,1,
             1,1,1,1,1]
inputs[9] = [1,1,1,1,1,
             1,0,0,0,1,
             1,1,1,1,1,
             0,0,0,0,1,
             1,1,1,1,1]

             
targets = [[1 if i==j else 0 for i in range(10)] for j in range(10)] 

random.seed(0)
input_size = 25
num_hidden = 5 #5 neurons in the hidden layer
output_size = 10 #10 outputs per input

hidden_layer = [[random.random() for _ in range(input_size + 1)] for _ in 
                 range(num_hidden)]

output_layer = [[random.random() for _ in range(num_hidden + 1)] for _ in 
                 range(output_size)]

network = [hidden_layer, output_layer]

for _ in range(10000):
    for input_vector, target_vector in zip(inputs, targets):
        backpropagate(network, input_vector, target_vector)

def predict(input_v):
    return feed_forward(network, input_v)[-1]