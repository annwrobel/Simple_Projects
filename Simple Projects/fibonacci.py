
a,b = 0,1

for i in range(0,10):
 a,b = b, a+b
 print(a)


 def f(n):
     if n==0:
         return 0
     elif n==1:
         return 1
     else:
         return (f(n-1)+f(n-2))

f(20)