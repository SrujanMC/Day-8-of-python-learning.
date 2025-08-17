# import webbrowser

# webbrowser.open("template/index.html")   # change path to your file
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html", username="Srujan")

# if __name__ == "__main__":
#     app.run(debug=True)

# my_info = {
#     "name": "Srujan",
#     "age": 15,
#     "city": "Bangalore",
#     "hobbies": ["Coding", "Music", "Gaming", "Reading"],
#     "skills": ["Python", "HTML", "CSS", "Sports"],
#     "education": "10th Grade",
#     "favorite_subject": "Computer Science",
#     "favorite_cs_language": "Python",
# }

# print("My Informations:")
# for key, value in my_info.items():
#     print(f"{key.replace('_', ' ').title()}: {value}")


# #Day 1
# Myname="Srujan"
# length=5
# width=6
# w=width
# l=length
# N=Myname
# print("My name is:",N)
# print("Perimeter of rectangle is:",2*(w+l))
# print("area of rectangle:",l*w)


# #Day 2
# a=8
# b=10
# c=True
# d=False
# e=None
# print("sum is:",a+b)
# print("Difference is:",a-b)
# print("multiplication is:",a*b)
# print("division is:",a/b)
# print("power is:",a**b)
# print("reminder is:",a%b)
# print(type(a))
# print(type(N))
# print(type(b))
# print(type(c))
# print(type(e))


# #Day 3
# A=10
# B=5
# print(A==B)
# print(A>B)
# print("Square of A and B is:", A**B)
# print("AND True or false:",(A==B) and (B+A))
# print("AND True or false:",(A>B) and (B<A))
# print("OR True of false:", A>B or B<A)
# print("OR True of false:", A<B or B>A)
# print("NOT True or false:", not(A==B))
# print("NOT True or false:", not(A!=B))
# A += B
# print(A)
# A**=B
# print(A)
# A/=B
# print(A)
# A%=B
# print(A)


# #Day 4
# x=5
# y=int("10")
# print("y is:",y)
# Name=input("Enter your name:")
# Age=int(input("Enter your age:"))
# City=str(input("Enter your city:"))
# print("Welcome your name enterd is:", Name)
# print("Your age is:", Age)
# print("Your city is:", City)

# #Practice questions
# #QN1
# Number1=int(input("Enter first number:"))
# Number2=int(input("Enter second number:"))
# print("Sum of two numbers is:", Number1 + Number2)

# #QN 2
# SideSquare=int(input("Enter side of square:"))
# print("Area of Square=:",SideSquare**2)


# # Day5

# #QN 3
# P=int(input("Enter Principal amount:"))
# R=float(input("Enter Rate of interest:"))
# T=int(input("Enter Time in years:"))
# print("Interest is:", (P * R * T) / 100)
# #QN 4
# Tem=float(input("Enter temperature in Celsius:"))
# print("Temperatur in Farenheit is:", (Tem * 9/5) + 32)

# #QN 5
# SS=float(input("Enter marks of Social:"))
# MA=float(input("Enter marks of Maths:"))
# EN=float(input("Enter marks of English:"))
# Sci=float(input("Enter marks of Science:"))
# Com=float(input("Enter marks of Computer:"))
# Hin=float(input("Enter marks of Hindi:"))
# Kan=float(input("Enter marks of Kannada:"))
# Totalmarks= SS + MA + EN + Sci + Com + Hin + Kan
# print("Total Marks Are:",Totalmarks)
# print("Percentage is:", (Totalmarks)/175*100)
# print("Avg is:",(Totalmarks)/7)

# #Lno-Stringand Conditionals
# Str1="Hello"
# Str2="Srujan"
# Str3=(Str1+" "+Str2)
# print(Str3)
# print("Length of string is:", len(Str3))
# print(Str3[-4:-2])
# print(Str3[4:12])

# #String functions
# str="i am srujan"
# print(str.capitalize())
# print(str.endswith("srujan"))
# print(str.startswith("sru"))
# print(str.find("sru"))
# print(str.count("j"))


# #Day6
# Usr=str(input("Users First Name:"))
# SecUsr=str(input("Users Second Name:"))
# print("Length of Users First and Second name:",len(Usr+SecUsr))
# print("Occurance of $ in First name:",Usr.count("$"))
# print("Occurance of $ in Second name:",SecUsr.count("$"))

# #practice question To Find The Discounted Price 6
# D=int(input("Discount Given For the Produce:%"))
# if(D<=100):
#     print("Entered Percentage is Valid")
# elif(D>=100): 
#     print("Entered Percentage is INValid") 
# elif(D<=0): 
#     print("Entered Percentage is INValid") 
# else:
#     (D==0)    
#     print("Its in Valid")
# V=int(input("Price of The Produce:"))
# GST=(5/100)*V
# print("GST is:",GST)
# D=(D/100)*V
# print("Discounted Value is:",D)
# V=V-D
# print("Total Bill is:",V+GST)

# #practice question 7
# M = int(input("Marks are: "))
# if M >= 90:
#     Grade = "A"
# elif M >= 80:
#     Grade = "B"
# elif M >= 65:
#     Grade = "C"
# elif M >= 50:
#     Grade = "D"
# else:
#     Grade = "E"
# print("Grade of the student is:", Grade)

# #Practice Qustion 8
# evodd=int(input("Enter a number: "))
# if evodd%2==0:
#         print("The number is even")
# else:
#         print("The number is odd")

# #Practice Question 9
# num = int(input("Enter a number: "))
# if (num%7)==0:
#     print("The number is divisible by 7")
# else:
#     print("The number is not divisible by 7")

# #Practice Question 10  
# A=int(input("A=")) 
# B=int(input("B="))
# C=int(input("C="))
# if A>C and A>B:
#     print("A is Greatest")
# elif B>A and B>C:
#     print("B is the Greatest")    
# else:
#      print("C is the Greatest")


# #Day 7
# Movies=[]
# Mov1=str(input("Movie 1 Name:"))
# Mov2=str(input("Movie 2 Name:"))
# Mov3=str(input("Movie 3 Name:"))
# Movies.append(Mov1)
# Movies.append(Mov2)
# Movies.append(Mov3)
# print(Movies)

# #Practice Question 11 !!
# Pal1 = input("Enter a string: ")
# reverse_Pal1 = Pal1[::-1]
# if Pal1 == reverse_Pal1:
#     print("It is a Palindrome")
# else:
#     print("It is not a Palindrome")

# # Practice Question 12
# Grade=["A","B","D","D","A","C","B","A","C","D"]
# Grade.sort()
# print("Sorted Grades:", Grade)


#Day 8
FA1=[]
SS1=float(input("Enter marks of Social:"))
MA1=float(input("Enter marks of Maths:"))
EN1=float(input("Enter marks of English:"))
Sci1=float(input("Enter marks of Science:"))
Com1=float(input("Enter marks of Computer:"))
Hin1=float(input("Enter marks of Hindi:"))
Kan1=float(input("Enter marks of Kannada:"))
FA1.append(SS1)
FA1.append(MA1)
FA1.append(EN1)
FA1.append(Sci1)
FA1.append(Com1)
FA1.append(Hin1)
FA1.append(Kan1)
Totalmarks1= SS1 + MA1 + EN1 + Sci1 + Com1 + Hin1 + Kan1
if Totalmarks1>=175:
    print("Entered Wrong Marks")
else:
    print("Graet Job! Let Me Calculate...")    
print("Total Marks Are:",Totalmarks1)
Percentage1=(Totalmarks1)/175*100
print("Percentage is%:",Percentage1 )
Avg1=(Totalmarks1)/7
print("Avg is:",Avg1)
print("List of FA-1 Marks:",FA1)

print()

FA2=[]
SS2=float(input("Enter marks of Social:"))
MA2=float(input("Enter marks of Maths:"))
EN2=float(input("Enter marks of English:"))
Sci2=float(input("Enter marks of Science:"))
Com2=float(input("Enter marks of Computer:"))
Hin2=float(input("Enter marks of Hindi:"))
Kan2=float(input("Enter marks of Kannada:"))
FA2.append(SS2)
FA2.append(MA2)
FA2.append(EN2)
FA2.append(Sci2)
FA2.append(Com2)
FA2.append(Hin2)
FA2.append(Kan2)
Totalmarks2= SS2 + MA2 + EN2 + Sci2 + Com2 + Hin2 + Kan2
if Totalmarks2>=175:
    print("Entered Wrong Marks")
else:
    print("Graet Job! Let Me Calculate...")
print("Total Marks Are:",Totalmarks2)
Percentage2=(Totalmarks2)/175*100
print("Percentage is%:",Percentage2 )
Avg2=(Totalmarks2)/7
print("Avg is:",Avg2)
print("List of FA-2 Marks:",FA2)

print()

print("Copmarision of FA's")
Compa_Mark=Totalmarks2-Totalmarks1
print("Apprician or Deperisitation is:",Compa_Mark)
Compa_Per=Percentage2-Percentage1
print("Percentage Difference is:",Compa_Per)
Comp_Avg=Avg2-Avg1
print("Comparision of Avg Marks:",Comp_Avg)
print("Comparision of Marks of FA1:",FA1)
print("Comparision of Marks of FA2:",FA2)
