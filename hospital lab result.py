# value = input("What is the value" )

# print("What is the test type")
# print("GLUCOSE")
# print("CHOLESTEROL")
# testtype = input("choose one")

# print("Which direction of conversion are you using?")
# print("mmol/L to mg/dL")
# print("mg/dL to mmol/L")
# unittype = input("choose one")

# if testtype == "GLUCOSE" and unittype== "mmol/L to mg/dl":
#     value = value * 18.0
#     print ("The value is" ,value)

# elif testtype  == "GLUCOSE" and unittype== "mg/dl to mmol/L":
#     value = value * 0.0555
#     print ("The value is" ,value)

# elif  testtype== "GLUCOSE" and unittype== "mmol/L to mg/dl":
#     value = value * 18.0
#     print ("The value is" ,value)

# elif testtype  == "CHOLESTEROL" and unittype== "mg/dl to mmol/L":
#     value = value * 0.02586
#     print ("The value is" ,value)

# elif  testtype== "CHOLESTEROL" and unittype== "mmol/L to mg/dl ":
#     value = value * 38.67
#     print ("The value is" ,value)

# else :
#     print("ERROR")

# Task2

temp1 = float(input("What is the first temperature: "))
temp2 = float(input("What is the second temperature: "))
temp3 = float(input("What is the third temperature: "))

average = (temp1 + temp2 + temp3) / 3 

if average > 100.4 :
    print(f"You have a fever, Your average is {average:.2f}")

else :
    print(f"You are ok, Your average is {average:.2f}")












