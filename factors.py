
def factors(num):
    print("The factors of",num,"are:")
    for i in range(1, num + 1):
        while(num % i == 0):
            print(i)
            if(i%2==0):
                print('even')
            else:
                print('odd')
            break       
factors(8)           
           
           
 