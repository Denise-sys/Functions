#Change numbers in symbols;

s=''
def line(number, symbol):
  global s
  for i in range(0,number):
      s = s + symbol 
      
line(5,@)
s = @@@@@

#This function uses the line function(shape) iteratively to complete the required shape;

input shape(4,'*')
s='' 
def line(number,symbol):
  global s
  for i in range(0,number):
  s = s + symbol 

#Another shape, new rows;

s='' 
line(5,'a')
def shape(m,c):
global s 
  for i in range(1,m+1):
line(i,c)
s = s + '\n' 

c = '*' 
m = 4
