class ispal():
    s=input()
    def palindrom(s):
    #s=input()
        s=str(s)
        for i in range(0,int(len(s)/2)):
            if(s[i] !=s[len(s)-i-1]):
                return False
        return True
                
    if(palindrom(s)==True):
        print(s,'is palindrom')
    else:
        print(s,'is not a palindrom')    
c=ispal()            
c.palindrom()            