# n = int(input("Enter the number: "))
# n1 = int(input("Enter the number: "))
# n2 = int(input("Enter the number: "))
# n3 = int(input("Enter the number: "))

# if n > n1 and n > n2 and n > n3:
#     print(n)
# elif n1 > n and n1 > n2 and n1 > n3:
#     print(n1)
# elif n2 > n and n2 > n1 and n2 > n3:
#     print(n2)
# else:
# mark1 = int(input("Enter the mark"))
# mark2 = int(input("Enter the mark"))
# total_percentage = (mark1+mark2)/200
# if( mark1>40 or total_percentage>33):
#     print("You are passed")
# else:
#     print("You are failed")

# list = ["S1","S2","S3","S4"]
# names = input("Enter the names")
# if(names in list):
#     print("Its there in list")
# else:
#     print("Its not in there")    
marks = int(input("Enter the marks"))
grade = (marks*100)/100
if((grade > 90 and 100)):
    print("Excellent")
elif(grade > 80 and 90):
    print("A Grade")
elif(grade > 70 and 80):
    print("B Grade")
elif(grade > 60 and 70):
    print("C Grade")
elif(grade > 50 and 60):
    print("D Grade")
else:
    print("F grade")                