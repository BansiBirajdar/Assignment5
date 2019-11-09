'''2. Write a recursive program which display below pattern.
Input : 5
Output : 1 2 3 4 5'''
def Dis(no):
    global i
    if no!=0:
        i+=1
        print(i,end=" ")
        Dis(no-1)
        
def main():
    no=int(input("Enter the number = "))
    print("output:")
    Dis(no)
i=0
if __name__=="__main__":
    main()