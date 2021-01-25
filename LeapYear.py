def IsDivisible(param, number):
  if param % number = 0:
    return True
  return False
  
def isLeap(param):
    check1 = isDivisble(param, 4)
    check2 = isDivisible(param, 400)
    check3 = isDivisble(param, 100)
    
    if check1 and not check3 or check2:
        return True
    return False
    
  
