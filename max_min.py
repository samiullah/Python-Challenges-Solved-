def max_finder(seq):
  max = seq[0]
  min = seq[0]
  for num in seq:
    if num>max:
      max = num
    elif num<min:
      min = num
  return max,min


print(max_finder([1,2,4,6,7]))
