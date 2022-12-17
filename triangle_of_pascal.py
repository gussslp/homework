from math import factorial 
x = 50
replace = True
for i in range(x):
    for b in range(x-i+1):
        print(end=" ")
    for b in range(i+1):
        c = factorial(i)//(factorial(b)*factorial(i-b))
        if replace == True:
         g = str(c)
         if c % 2 == 0:
          c = g.replace(g,"0")
         else:
          c = g.replace(g,"1")
        print(c,end=" ")
    print(" ")