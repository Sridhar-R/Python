def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b


if __name__ == '__main__':
        a= input("Enter the 1st number:")
        b= input("Enter the 2nd number:")

        print ("select option:")
        print ("1.Add:")
        print ("2.Sub:")
        print ("3.Multiply:")
        print ("4.Divide:")

        option = input()

        if option ==1:
                print("The addition of two numbers is :"), add(a,b)
        elif option ==2:
                print("The subraction of two numbers is :"), sub(a,b)
        elif option ==3:
                print("The multiplication of two numbers is :"), mul(a,b)
        elif option ==4:
                print("The division of two numbers is :"), div(a,b)
        else:
                print("Invalid option")
