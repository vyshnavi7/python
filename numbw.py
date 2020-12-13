def find_num(c=0):
    for i in range(1001,3000):
        if(i%2==1):
            print(i)
            c=c+1
    print('number of odd numbers in between 1000 & 3000 are:',c)            
find_num()            
                    