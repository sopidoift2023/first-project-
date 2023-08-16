import math
a = int(input('a :' ))
b = int(input('b : '))
c = int(input('c :' ))
d = (b**2) - 4*a*c
if d > 0 :
    p = math.sqrt(d)
    f = (-b + p) / 2*a
    g = (-b - p) / 2*a
    print(f'the roots are x1=  {f} and x2 = {g}')
elif d == 0 :
    p = math.sqrt(d)
    g = (-b - p) / 2*a
    print(f'the equation has equal roots x1 = x2 = {g}')
elif d < 0 :
     print(f'the equation has imaginary roots')  
     
 
 
 
 


     
     
   
 
    
    
    
    