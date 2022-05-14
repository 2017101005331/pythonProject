list1=[1,4,2,2,3,76,7,8]
 def reverse(numbers):
  if(len(numbers)==1):
    return numbers
  return reverse(numbers[1:])+numbers[0:1]
print(reverse(list1))
