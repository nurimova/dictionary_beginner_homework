def sum_float_values(data: dict) -> float:
    '''
    Return the sum of all float values in dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        float: The sum of all float values in the dictionary.
    '''
    count=0
    for item in data.values():
        if type(item)==float:
            count+=item
    return count
data = {
    'a': 1, 
    'b' : 2.5, 
    'c': 3.0
  }
print(sum_float_values(data))