'''list1='mahesh'
def reverse(numbers):
  if (len(numbers)==1):
    return numbers
  return reverse(numbers[1:])+numbers[0:1]
print(reverse(list1))
'''
'''
def fact(n):
  if(n==0):
    return 1
  return n*fact(n-1)
a=fact(8)
print(a)
'''
'''

def fib(n):
  a=0
  b=1
  print(a)
  print(b)
  for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c)
fib(8)'''
'''
n=int(input('enter the number'))
for i in range(2,n):
  if(n%i==0):
    print('not a prime')
else:
    print('prime')'''
'''
n=int(input('enter the number'))
sum=0
temp=n
while(temp>0):
  digit=temp%10
  sum=sum+digit**3
  temp=temp//10
if(n==sum):
  print('is armstrong')
else:
  print('its  not armstrong')
  '''
import pandas as pd
info={
'c':['a','b'],
'b':[12,13],
}
p=pd.DataFrame(info)
print(p)
