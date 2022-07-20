print("Python Calculator ")
print()

a = int(input("Enter the First Number : "))
b = int(input("Enter the Second Number : "))
print("Now Choose The Operation: (+ , - , * , /) ")
choice = input()
if choice== '+':
    print(a+b)
elif choice == '-':
    print(a-b)
elif choice=='*':
    print(a*b)
elif choice=='/':
    print(a/b)
elif choice=='%':
    print(a%b)
else:
    print("Please select valid opertaion...!!")


