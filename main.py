from addition import Adittion

class Calculator:
    def __init__(self):
        self.run()

    def run(self):
        print("Select Operation")
        print("1. Addition")
        choice=input("Enter Choice (1/2/3/4) ")
        if choice in ('1','2','3','4'):
            num1=float(input("Enter First Number: "))
            num2=float(input("Enter Second Number: "))
            if choice=='1':
                print("Result",Adittion.add(num1,num2))
        else:
            print("Invalid Input")
    

if __name__=="__main__":
    Calculator()