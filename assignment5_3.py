'''3.Write a recursive program which display below pattern.
Input : 5
Output : 5 4 3 2 1'''
def Dis(no):
    if no!=0:
        print(no,end=" ")
        Dis(no-1)
        
def main():
    no=int(input("Enter the number = "))
    print("output:")
    Dis(no)
    
if __name__=="__main__":
    main()