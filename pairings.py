def find_pairs(num_string):
  # Write your solution here!/
  # split each items in string/
  # convert elemnt to num/
  # find a pairs:
  nums = []
  for num in num_string.split():
    num = int(num)
    nums.append(num)
  
  pairs = set()
  
  for num in nums:
    for j in nums:
      if num < j:
        pairs.add((num, j))
  return pairs
  

# print(find_pairs("7 3 99"))

# Test cases
assert find_pairs("7 3 99") == {(7, 99), (3, 7), (3, 99)}
assert find_pairs("2 1") == {(1, 2)}
assert find_pairs("24 7 365 94") == {(7, 94), (24, 94), (94, 365), (7, 365), (24, 365), (7, 24)}
assert find_pairs("94") == set()

print("All tests passed!")
print("Finished early? Discuss time & space complexity")