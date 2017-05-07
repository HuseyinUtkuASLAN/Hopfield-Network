import numpy as np



def treshhold(vector):
  
  tmp = vector
  for x in np.nditer(tmp, op_flags=['readwrite']):
    
    if x < 0:
      x[...] = -1
    else:
      x[...] = 1

  
  
  return tmp      


def numpyVectorInList(vector, list):

  value = False

  for v in list:
    if np.array_equal(vector,v):
      value = True
      break

  return value

def stabilityCheck(weight, vector, name, maxIteration):
  
  print ("")
  print ("")
  
  print ("stability check for ", name , " : ") 
  print ("original vector : ")
  print (vector)
  
  
  oldVector = vector
  
  newVector = np.dot(weight,oldVector)
  newVector = treshhold(newVector)
    
  lstVectors = []

  lstVectors.append(oldVector)

  numberOfIterations = 0

  stable = True

  while  numpyVectorInList(newVector,lstVectors) == False :

    #print "new vector : ", newVector
    tmp = newVector
    newVector = np.dot(weight,oldVector)
    oldVector = tmp
    newVector = treshhold(newVector)

    lstVectors.append(oldVector)

    if numberOfIterations >= maxIteration:
      stable = False
      break
    else:
      numberOfIterations += 1
  # compare oldVector and newVector. If they are equal stop. If new vector is equal with original vector, it is consistant, else not!
  #while ( newVector.tolist()==oldVector.tolist() )== False:
    
  #  print "new vector : ", newVector[0][0],newVector[1][0],newVector[2][0]
  #  tmp = newVector
  #  newVector = np.dot(weight,oldVector)
  #  oldVector = tmp
  #  newVector = treshhold(newVector)
    
  if stable:
    return newVector
  else:
    return None



def calculateWeight(vectors):
  size = 0
  size = len(vectors)
  #print ("Vector count : " , size)

  shape = 0

  for v in vectors:
    if shape == 0:
      shape = v.shape[0]
    elif v.shape[1] != 1 or shape != v.shape[0]:
        print ("Vector have different shape!!!")
        print ("Vector down bellow should have ", shape)
        
        print (v)

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

  maxIteration = 10
    
  v1 = np.array([[1], [1], [1]])
  v2 = np.array([[-1], [-1], [1]])
  

  v3 = np.array([[1], [1], [1]])
  #v4 = np.array([[-1], [1], [1], [1]])
  
  lstVector = []

  lstVector.append(v1)
  lstVector.append(v2)
  lstVector.append(v3)
  #lstVector.append(v4)
  print (lstVector)
  weight = calculateWeight(lstVector)
  
  print ("Weight is : ")
  print (weight)
  print ("")
  #print ("")
  
  count = 1
  for v in lstVector:
    name = "v" + str(count)
    stbTest = stabilityCheck( weight,v, name, maxIteration )
    count += 1

    if stbTest == None:
      print (name, "is not stable after" , maxIteration, " iteration !!!")
    elif np.array_equal(v,stbTest):
      print (name, "is stalbe. It is equal with vector.")
      print (stbTest)
    elif numpyVectorInList(v,lstVector):
      print (name, "is stable. It is same with another vector that is given.")
      print (stbTest)
      
    else:
      print (name, "is stable. It is not same with vector or another vector. During the test there was another vector during the test")
      print (stbTest)

###### MAIN FUNCTION ######

  