import argparse
import csv
import random

def splitDataThreeWay(dataset):
    """
    Splits the dataset into 70% training, 15% validation, and 15% testing.
    """

    # Calcualte index on which to split the data
    train_index = int(0.7 * len(dataset))
    val_index = int(0.85 * len(dataset))

    # Split the dataset three ways
    train_data = dataset[:train_index]
    validate_data = dataset[train_index : val_index]
    test_data = dataset[val_index:]

    return train_data, validate_data, test_data


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
            header = next(reader)
            dataset = list(reader)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    
    return dataset
