a=int(input("write a number: "))
b=int(input("inserisci il numero b: "))


def MCD(a,b):
    if b==0:
        print("l'MCD è ",a)
    else:
        while b>1:
            r=a%b
            
            if r==0:
                print("l'MCD è ",b)
                break
            else:
                a=b
                b=r
        else:
            print("l'MCD è 1")

MCD(a,b)

                










            
            
    








    
    
    
        
    

        

              
