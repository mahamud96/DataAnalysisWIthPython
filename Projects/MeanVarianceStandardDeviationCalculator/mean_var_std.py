import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(list).reshape(3, 3)

    calculations = {}

    
    calculations['mean'] = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()]
    calculations['variance'] =  [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()]
    calculations['standard deviation'] = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()]
    calculations['max'] = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()]
    calculations['min'] = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()]
    calculations['sum'] = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]

    return calculations