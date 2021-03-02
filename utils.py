import math

def read_data(data):
    with open(data) as f:
        lines = f.readlines()
    columns = ['ID', 'f1', 'f2', 'f3','f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10','f11', 'class']
    data = []
    for line in lines:
        line = line.split(',')
        dictionary = {}
        for key,values in  zip(columns,line):
            dictionary[key] = float(values)
        data.append(dictionary)
    return data








