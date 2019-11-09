'''4.Write a recursive program which accept number from user and return
summation of its digits.
Input : 879
Output : 24'''
def Sum(no):
    global sum
    if no!=0:
        sum+=(no%10)
        Sum(no//10)
    return sum;
        

def main():
    no=int(input("Enter the number = "))
    print("output:")
    add=Sum(no)
    print("summation of digits {} is =".format(no),add)
    
sum=0
if __name__=="__main__":
    main()
    