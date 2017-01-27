#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 12:54:28 2017

@author: carlosjarguello
Following Grus' book neural networks chapter. 
Xor funxtion with neural networks
"""

import numpy as np


def neuron_output(weights, inputs):
    return np.arctan(np.dot(np.array(weights), np.array(inputs)))/np.pi+0.5

def feed_forward(neural_network, input_vector):
    outputs = []
    
    for layer in neural_network:
        input_with_bias = input_vector + [1]
        output = [neuron_output(neuron, input_with_bias) for neuron in layer]
        outputs.append(output)
        input_vector = output
    
    return outputs

xor_network = [[[20, 20, -30], [20,20,-10]], [[-60, 60, -30]]]

def test():
    for x in [0,1]:
        for y in [0,1]:
            print x, y, feed_forward(xor_network, [x,y])[-1]