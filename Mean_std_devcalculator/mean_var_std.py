import numpy as np

def calculate(list):

    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")

    calculations = {}                     # the dict to store calculations
    array = np.array(list).reshape(3,3)

    # Calculating Mean

    axis1 = np.mean(array, axis=0)
    axis2 = np.mean(array, axis=1)
    flattened = np.mean(array)
    calculations['mean'] = [axis1, axis2, flattened]

    # Calculating Variance

    axis1 = np.var(array, axis=0)
    axis2 = np.var(array, axis=1)
    flattened = np.var(array)
    calculations['variance'] = [axis1, axis2, flattened]

    # Calculating Standard Deviation

    axis1 = np.std(array, axis=0)
    axis2 = np.std(array, axis=1)
    flattened = np.std(array)
    calculations['standard deviation'] = [axis1, axis2, flattened]

    # Calculating Max

    axis1 = np.max(array, axis=0)
    axis2 = np.max(array, axis=1)
    flattened = np.max(array)
    calculations['max'] = [axis1, axis2, flattened]

    # Calculating Min

    axis1 = np.min(array, axis=0)
    axis2 = np.min(array, axis=1)
    flattened = np.min(array)
    calculations['min'] = [axis1, axis2, flattened]

    # Calculating Sum

    axis1 = np.sum(array, axis=0)
    axis2 = np.sum(array, axis=1)
    flattened = np.sum(array)
    calculations['sum'] = [axis1, axis2, flattened]

    return calculations



