#Lab Assingment 1
#Yaseen Nur
#ID:20101218
#Section:09

#Task1
def shiftLeft(source,kPos):
  inx=kPos
  jnx=len(source)-kPos
  while(inx<len(source)):
    source[inx-kPos]=source[inx]
    inx+=1
  while(jnx<len(source)):
    source[jnx]=0
    jnx+=1

a=[0,1,2,3,4,5]
shiftLeft(a,3)
print(a)

#Task2
def shiftLeft(source,kPos):
  copySource=list(source)
  inx=kPos
  jnx=len(source)-kPos
  while(inx<len(source)):
    source[inx-kPos]=source[inx]
    inx+=1
  while(jnx<len(source)):
    source[jnx]=copySource[jnx-kPos]
    jnx+=1

a=[0,1,2,3,4,5]
shiftLeft(a,3)
print(a)

#Task3
def remove (source, size, inx):
    
    i=inx+1

    while(i<=size):                           
        source[i-1]=source[i]
        i+=1
    print(source)

source=[10,20,30,40,50,0,0]
remove(source,5,2)

#Task4
def removeAll (source,size,elmnt):
  for (i,val) in enumerate(source):
    if source[i]==elmnt:
      source[i]=0
  for i in range (0, size,1):                  

        if source[i]==0:

            for k in range(i+1,size):          
                if source[k]!=0:               

                    temp=source[i]
                    source[i]=source[k]
                    source[k]=temp

                if source[i]!=0:                 
                    break
  print(source)
            
d=[10,2,30,2,50,2,2,0,0]
removeAll(d,7,2)

#Task4 Alternative method
def removeAll(source,size,gval): 
  
  zeroList=[]
  nonZerolist=[]
  
  for i,val in enumerate(source):
    if val==gval:
      source[i]=0
      
  for val in source:
    if val==0:
      zeroList.append(val)
    else:
      nonZerolist.append(val)
      
  source[:]=nonZerolist+zeroList
  
d=[10,2,30,2,50,2,2,0,0]
removeAll(d,7,2)
print(d)

#Task5
A=[10,3, 1, 2, 10]
Status=False
sum1=0
sum2=0

for i in range (len(A)):
    
    for j in range(0,i,1):
        sum1+=A[j]                   
        
    for k in range(i,len(A),1):       
        sum2+=A[k]
        
    if sum1==sum2:
        Status=True    
    else:
        sum1=0
        sum2=0
    i=i+1
    
print(Status)

#Task5 Alternative Method
def sum(nums):
  total=0
  for ind in range(0,len(nums)):
    total=total+nums[ind]
  return total

def balanceWeights(weights):
  state=False
  for inx,val in enumerate(weights):
    if sum(weights[:inx])==sum(weights[inx:]):
      state=True
  print(state)

balanceWeights([10,3,1,2,10])


    
#Task6
def arraySeries(n):
  
  finalList=[]

  for i in range(n):
    
    count=0
    countInv=n-i-1
    vallue=0
    
    for m in range(n):
      
      if count==0:
        print(countInv,i,m)
        
        if countInv!=0:
          finalList+=[vallue]
          countInv-=1
        
        else:
          count+=1
          vallue=i+1
          while(vallue>0):
            finalList+=[vallue]
            vallue-=1
                 
        
  print(finalList)        
    
arraySeries(4)


#  Task 7
def bunch(source):
    
    bunch1=0
    bunch2=0
   
    for i in range(len(source)):          
        for j in range(i,len(source)):       
            if source[i]==source[j]:        
                bunch1+=1
                
            else:
                break
        
        if bunch1>bunch2:      
            
            bunch2=bunch1      
            bunch1=0
            
        else:
            bunch1=0
            
    print(bunch2)
    
# source=[1, 2, 2, 3, 4, 4, 4]
source=[1,1,2, 2, 1, 1,1,1]
bunch(source)

# task8
def repetition(source):
    status=False
    
    counter = [0] * len(source)
    emp=[]
    
    for i in source:                  
        counter[i] = counter[i] + 1             
        
    for j in counter:                      
        if j>1:
          emp+=[j]
    
    for (i,val) in enumerate(emp):
      for k in range(i+1,len(emp)):
        if val==emp[k]:
          status=True
     
    print(status)          
            
source=(4,5,6,6,4,3,6,4)
# source=[3,4,6,3,4,7,4,6,8,6,6]
repetition(source)


# Circular Arrays
# Task1
def palindrome(arr,start,size):
  check=round(size/2)
  count=0
  index=start
  lastIndex=(start+size-1)%len(arr)
  i=0
  while(i<round(size/2)):
    if arr[index]==arr[lastIndex]:
      count+=1
      i+=1
      index+=1
      lastIndex-=1
    else:
      i+=1
      index+=1
      lastIndex-=1
  
  if (count==check):
    print("True")
  else:
    print('False')
        
palindrome([20,10,0,0,0,10,20,30],5,5)
palindrome([10,20,0,0,0,10,20,30],5,5)

#Task2
def intersection(arr1,arr2,a1size,a2size,a1Start,a2Start):
  lastinx1=(a1Start+a1size-1)%len(arr1)
  emp=[]
  final=[]
  for i in range(a1size):
    lastinx2=(a2Start+a2size-1)%len(arr2)
    for j in range(a2size):
      if arr1[lastinx1]==arr2[lastinx2]:
        emp+=[arr1[lastinx1]]
        lastinx2-=1
      else:
        lastinx2-=1
    lastinx1-=1
    
  for i in range(len(emp)-1,-1,-1):
    final+=[emp[i]]
  print(final)    

intersection([40,50,0,0,0,10,20,30],[10,20,5,0,0,0,0,0,5,40,15,25],5,7,5,8 )

# Task2 Alternative
def intersection(arr1,arr2,a1size,a2size,a1Start,a2Start):
    
    inx=a1Start
    linear=[]
    
    for i in range(a1size):           #i=0 sz1= 5
        
        inx=(inx)%len(arr1)           
        
        if arr1[inx] in arr2:          #a1=5 in a2

            linear+=[arr1[inx]]
        inx+=1
        
    print(linear)

intersection([40,50,0,0,0,10,20,30],[10,20,5,0,0,0,0,0,5,40,15,25],5,7,5,8 )

# task3
import random

def clockwise(arr):
  lastPlayer=arr[len(arr)-1]
  lastInx=len(arr)-1
  while(lastInx>0):
    arr[lastInx]=arr[lastInx-1]
    lastInx-=1
  arr[0]=lastPlayer

def musicalChair(players):
  while(len(players)!=1):
    z=random.randint(0,3)
    if z!=1:
      clockwise(players)
      
    else:
      players.pop(round(len(players)/2))
      print(f'Remaining players are: {players}')
      
  print(f'Winner!: {players[0]}')
  
musicalChair(['Eren','Mikasa','Armin','Levi','Erwin','Reiner','Jean'])

