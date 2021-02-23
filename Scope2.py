def MyRange(start, end, step):
  global seq
  if step != 0:
    for i in range (start, end, step):
      seq = seq + str(i)
      
  else:
    seq = 'Error' 
    
    #reverse a number; 
    
def reverse(arg):
  global rn
  while (arg>0):
    rn = str(rn) + str(arg % 10)
    arg = arg // 10
  rn = int(rn)
  
rn = 0
reverse(arg)
print()

#turn table example 1x1 = 1 en 1x2 = 2 etc. 

def table(n,m):
  global final
  final = '' 
  for i in range(1, m + 1):
    final = final + str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n'
    
  
