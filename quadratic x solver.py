found =0
a = input('Input a:')
b = input('Input b:')
c = input('Input c:')
x = 1
y = 1
 
if a <= 1:
 while found ==0 :
    
   y =float(c/x)
   ans = x + y
   if x + y == b:
     if x > 1:
      print '( x +', x,')'
     elif x < 1:
      print '( x', x,')'
     if y > 1:
      print '( x +', y,')'
     elif y < 1:
      print '( x', y,')'  
     found = found + 1
   else:
    print 'attempt1','x =', x, 'y =', y
    x = x * -1
    y = float(c/x)
    ans = x + y
    print 'ans =',ans
    if ans == b:
        if x > 1:
          print '( x +', x,')'
        elif x < 1:
          print '( x', x,')'
        if y > 1:
          print '( x +', y,')'
        elif y < 1:
          print '( x', y,')'  
        found = found + 1
    else:
     x = abs(x) 
     x = x + 1
     print 'x value increased' 
     print 'attempt2','x =', x, 'y =', y
elif a > 1 :
 c = a * c
 while found == 0:
  print 'c is ',c
  y =float(c/x)
  ans = x + y
  if x + y == b:
   print 'x =', x, 'y =', y
   found = found + 1
  else:
   print 'attempt1','x =', x, 'y =', y
   x = x * -1
   y = float(c/x)
   ans = x + y
   print 'ans =',ans
   if ans == b:
    print 'x =', x, 'y =', y
    found = found + 1
   else:
    x = abs(x) 
    x = x + 1
    print 'x value increased' 
    print 'attempt2','x =', x, 'y =', y
raw_input()     
     
   
 
