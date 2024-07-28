A = ['abc', 'xyz', 'aba', '1221']

for i, string in enumerate(A):
  if string[0] == string[-1]:
    print(f"String: {string}, Index: {i}")
