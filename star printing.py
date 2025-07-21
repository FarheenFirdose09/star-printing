    #full square star pattern
n=5                                           #n=5
for i in range(n):                  #or       #print('*'*n)
    for j in range(n):
        print('*',end=' ')
    print()

     #decreasing triangle pattern
n=5
for i in range(n):
    for j in range(i,n):
        print('*',end=' ')
    print()  

      staircase pattern
rows=6                             #n=5
for i in range(1,rows+1):          #for i in range(n):
    print(" * "*i)                    #for j in range(i+n):
    print('*',end=' ')
    print()

     #right sided traingle pattern
#n=5
#for i in range(n):
    #for j in range(i,n):
        #print(' ',end=' ')
    #for j in range(i+1):
        #print('*',end=' ')
    #print()

     #left traingale pattern
#n=5
#for i in range(n):
    #for j in range(i+1):
        #print(' ',end=' ')
    #for j in range(i,n):
            #print('*',end=' ')
    #print()

     #hill pattern
#n=5
#for i in range(n):
      
    #for j in range(i,n):
      #print(' ',end=' ')
    #for j in range(i):
      #print('*',end=' ')
    #for j in range(i+1):
      #print('*',end=' ')
    #print()  


    #reverse pattern
#n=5
#for i in range(n):
      
    #for j in range(i+1):
      #print(' ',end=' ')
    #for j in range(i,n):
      #print('*',end=' ')
    #for j in range(i,n):
      #print('*',end=' ')
    #print()  

    #diamond pattern
n=5
for i in range(n):
      
    for j in range(i,n):
      print(' ',end=' ')
    for j in range(i):
      print('*',end=' ')
    for j in range(i+1):
      print('*',end=' ')
    print()  
for i in range(n):
      
    for j in range(i+1):
      print(' ',end=' ')
    for j in range(i,n):
      print('*',end=' ')
    for j in range(i,n):
      print('*',end=' ')
    print()  
