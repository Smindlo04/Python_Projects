print("BMI Calculator")

print("1.Weight in kilograms, height in meters")

print("2.Weight in pounds, height in inches")

choice1_or_2=int(input("Please input your choice between 1 and 2: "))

# If the user uses option number 1
if choice1_or_2==1 :
   weight=float(input("Please input your weight in kilograms: "))
   height=float(input("Please input your height in meters: "))
   BMI=round(weight/height**2,2)

# If the user used option number 1 and the BMI is larger or equal to 35
if BMI>=35 :
   label="Severly obese"

# If the user used option number 1 and the BMI is between 35 and 30
elif (BMI>=30 and BMI<35) :
   label="Obese"

# If user used option number 1 and the BMI is between 30 and 25
elif (BMI>=25 and BMI<30) :
   label="Overweight"

# If the user used option number 1 and the BMI is between 25 and 18.5
elif (BMI>=18.5 and BMI<25) :
   label="Healthy"

# If the user used option number 1 and the BMI is smaller then 18.5
elif (BMI<18.5) :
   label="Underweight"

print("BMI Report")
print("Weight: ",weight,"kg")
print("Height: ",height,"m")
print("BMI: ",BMI)
print("Status: ",label)
print("Press enter to quit the program |")



# If the user uses option number 2
if choice1_or_2==2 :
     weight= float(input("Please input your weight in kilograms: "))
     height= float(input("Please input your height in meters: "))
     BMI= round((weight/height**2 * 703),2)

# If the user used option number 2 and the BMI is larger or equals to 35)
if BMI>=35 :
     label="Severly obese"

# If the user used option number 2 and the BMI is between 35 and 30
elif (BMI>=30 and BMI<35) :
     label="Obese"

# If the user used option number 2 and the BMI is between 30 and 25
elif (BMI>=25 and BMI<30) :
     label="Overweight"

# If the user used option number 2 and the BMI is between 25 and 18.5
elif (BMI>=18.5 and BMI<25) :
     label="Healthy"

# If the user used option number 2 and the BMI is smaller than 18.5
elif (BMI<=18.5) :
     label="Underweight"

print("BMI Report")
print("Weight: ",weight,"lb")
print("Height: ",height,"in")
print("BMI: ",BMI)
print("Status: ",label)
print("Press enter to quit the program |")
