def sum_dict_values(data: dict) -> int:
    '''
    Return the sum of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all values in the dictionary
    '''
    count=0
    for item in data.values():
        count+=item
    return count
data = {
    'a': 1, 
    'b': 2, 
    'c': 3
  } 
data = {
    1: 23, 
    2: 3.5, 
    4: 1, 
    6: 7, 
    5: 2, 
    7: 3
  }
print(sum_dict_values(data))