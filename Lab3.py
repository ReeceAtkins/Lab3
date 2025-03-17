import argparse
import csv
import random

def splitData(dataset):
    """
    Splits the dataset sequentially into 80% training and 20% testing.
    """
    # Calculate the index to split the data
    split_index = int(0.8 * len(dataset))
    
    # Split the dataset
    train_data = dataset[:split_index]
    test_data = dataset[split_index:]
    
    return train_data, test_data

def splitDataRandom(dataset):
    """
    Splits the dataset randomly into 80% training and 20% testing.
    """
    # Randomly shuffle the dataset
    random.shuffle(dataset)
    
    # Calculate the index to split the data
    split_index = int(0.8 * len(dataset))
    
    # Split the dataset
    train_data = dataset[:split_index]
    test_data = dataset[split_index:]
    
    return train_data, test_data

def read_csv(file_path):
    """
    Reads a CSV file and returns its contents as a list of lists.
    """
    dataset = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next()
    except:
        print("Error reading CSV file")
