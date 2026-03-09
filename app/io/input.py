import pandas as pd

def input_from_console():
    """Allows user to input from console."""
    return input("Введіть дані: ")

def read_from_file_builtin(file_path):
    """Reads data from a file using built-in tools"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def read_from_file_pandas(file_path):
    """Reads data from a file via pandas"""
    data = pd.read_csv(file_path)
    return data.to_string()