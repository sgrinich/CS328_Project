import os
import sys
import random
import csv
"""Module for working with the object-feature dataset.
"""

def load_name_data(filename):
    '''
    Loads a file with object names or features.
    Returns the results as a list.
    Parameters:
    filename: name of the file where the object names/features are stored
    '''
    names = []
    f = open(filename)
    for line in f:
        names.append(line.strip())
    f.close()
    return names
    
def load_object_feature_data(filename):
    '''
    Loads a file with a binary matrix of object-feature pairs.
    Each row represents one object, and each column represents one feature.
    Returns a 2-dimensional list where each inner list is one row in the
    original matrix
    Parameters:
    filename: name of the file where the matrix is stored
    '''
    matrix = []
    f = open(filename)
    for line in f:
        features = []
        split_line = line.split()
        for item in split_line:
            features.append(int(item.strip()))
        matrix.append(features)
    f.close()
    return matrix
    
def load_google_form_csv(filename):
    names = []
    f = open(filename)
    for line in f:
        names.append(line.strip())
    f.close()
    return names
        
