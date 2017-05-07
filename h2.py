import numpy as np



def treshhold(vector):
  
  tmp = vector
  for x in np.nditer(tmp, op_flags=['readwrite']):
    
    if x < 0:
      x[...] = -1
    else:
      x[...] = 1

  
  
  return tmp      

def stabilityCheck(weight, vector, name):
  
  print ""
  print ""
  
  print "stability check for ", name , " : " 
  print "original vector : "
  print vector
  
  
  oldVector = vector
  
  newVector = np.dot(weight,oldVector)
  newVector = treshhold(newVector)
      
  # compare oldVector and newVector. If they are equal stop. If new vector is equal with original vector, it is consistant, else not!
  while ( newVector.tolist()==oldVector.tolist() )== False:
    
    print "new vector : ", newVector[0][0],newVector[1][0],newVector[2][0]
    tmp = newVector
    newVector = np.dot(weight,oldVector)
    oldVector = tmp
    newVector = treshhold(newVector)
    
    
    
  print "last vector : "
  print newVector
  print ""
  print ""
  
  print "stability result : "
  if newVector.tolist() == vector.tolist():
    print name, " is stable"
  else:
    print name, " is not stable"




def calculateWeight(vectors):
  size = 0
  size = len(vectors)
  print "Vector count : " , size

  shape = 0

  for v in vectors:
    if shape == 0:
      shape = v.shape[0]
    elif v.shape[1] != 1 or shape != v.shape[0]:
        print "Vector have different shape!!!"
        print "Vector down bellow should have ", shape
        
        print v

        return 0

  

  weight = np.zeros([shape,shape])
  
  for x in range(0, shape - 1):
    
    for y in range (x+1,shape): 
      
      w = 0.0
      
      for v in vectors:
        w += v[x][0]  *  v[y][0]
      
      weight[x,y] = w / size
      weight[y,x] = w / size
  
  return weight
  
  
def Debug():
    
  v1 = np.array([[1], [-1], [1]])
  v2 = np.array([[1], [1], [1]])
  v3 = np.array([[-1], [-1], [1]])
  
  weight = calculateWeight([v1, v2, v3])
  
  print "Weight is : "
  for x in range(0, 3):
    print weight[x]
  print ""
  print ""
  
  stabilityCheck(weight, v1,"v1")
  
  stabilityCheck(weight, v2,"v2")
  
  stabilityCheck(weight, v3,"v3")



###### MAIN FUNCTION ######
debug = True
if debug:
  Debug()
  
else:
  
  while True:
    
    pick = raw_input("'D' for debuging, 'M' manuel input, 'F' for file input, 'Q' for quiting  >>>> ")
    
    if pick == "D":
      Debug()
    elif pick == "M":
      sizeOfVector = raw_input("Enter size of the vector >>>> ")
    elif pick == "F":
      path = raw_input("Enter file path >>>> ")
    elif pick == "Q":
      break
    else:
      print "wrong input"
    
    print ""
  