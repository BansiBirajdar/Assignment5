'''5. Write a recursive program which accept number from user and return its
factorial.
Input : 5
Output : 120'''
def Factorial(no):
    '''global fact
    global i
    if no!=0:
        i+=1
        fact*=i
        Factorial(no-1)
    return fact'''
    if no==1:
        return no
    else:
        return no*Factorial(no-1)
    

def main():
    no=int(input("Enter the number = "))
    if no==0:
        print("factorial is 1")
    else:   
        ans=Factorial(no)
        print("factorial is =",ans)
    
fact=1
i=0  
if __name__=="__main__":
    main()