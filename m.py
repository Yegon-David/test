

values = [1,2,3,4,5,6,7,8,9]

def odd_even(*args):
  even=[]
  odd=[]
  for i in args:
    if i%2 == 0:
      even.append(i)
    else:
      odd.append(i)
  print(odd)       
  print(even)       

odd_even(*values)  