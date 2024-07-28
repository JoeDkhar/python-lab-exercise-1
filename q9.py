def extract_rear_elements(tuple_strings):

  return [string[-1] for string in tuple_strings]


my_tuple = ('python', 'learn', 'includehelp')
print(my_tuple)
result = extract_rear_elements(my_tuple)
print(result)
