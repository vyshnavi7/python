def find_na():
    digi=let=0
    st=input()
    for i in range(0,int(len(st))):
        if(st[i].isdigit()):
            digi=digi+1
        elif(st[i].isalnum()):
            let=let+1
        else:
            pass    
    print('digits',digi)
    print('letters',let)
find_na()    
        
    