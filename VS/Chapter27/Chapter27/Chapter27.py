import time



#introduction part
name = input(" Hello user i am the income calculator what is your name? : ")
print("")
time.sleep(1.5)
print("Alright {} lets work out your income for this week ".format(name))
print("")
time.sleep(1.5)



#Reading tempo
reading_tempo_determination = int(input("How fast would you like the tempo to be from 1 (very fast) - 10 (very slow)? : "))
print("")

reading_tempo = 0

if(reading_tempo_determination == 1):
    reading_tempo += 1

if(reading_tempo_determination == 2):
    reading_tempo += 2

if(reading_tempo_determination == 3):
    reading_tempo += 3

if(reading_tempo_determination == 4):
    reading_tempo += 4

if(reading_tempo_determination == 5):
    reading_tempo += 5

if(reading_tempo_determination == 6):
    reading_tempo += 6

if(reading_tempo_determination == 7):
    reading_tempo += 7

if(reading_tempo_determination == 8):
    reading_tempo += 8

if(reading_tempo_determination == 9):
    reading_tempo += 9

if(reading_tempo_determination == 10):
    reading_tempo += 10



time.sleep(reading_tempo)



#Income determination

Income = int(input("What is your income {}? ".format(name)))

time.sleep(reading_tempo)



#Hours worked in the week
hours_worked_monday = int(input("How Many Hours have you Worked on Monday?: "))
print("")

hours_worked_tuesday = int(input("How Many Hours have you Worked on Tuesday?: "))
print("")

hours_worked_wednesday = int(input("How Many Hours have you Worked on Wednesday?: "))
print("")

hours_worked_thursday = int(input("How Many Hours have you Worked on Thursday?: "))
print("")

hours_worked_friday = int(input("How Many Hours have you Worked on Friday?: "))
print("")

hours_worked_saturday = int(input("How Many Hours have you Worked on Saturday?: "))
print("")

hours_worked_sunday = int(input("How Many Hours have you Worked on Sunday?: "))
print("")

time.sleep(reading_tempo)



#Total Income of each Day
total_income_mon = hours_worked_monday * Income

total_income_tue = hours_worked_tuesday * Income

total_income_wed = hours_worked_wednesday * Income

total_income_thu = hours_worked_thursday * Income

total_income_fri = hours_worked_friday * Income

total_income_sat = hours_worked_saturday * Income

total_income_sun = hours_worked_sunday * Income

total_income_week = total_income_mon + total_income_tue + total_income_wed + total_income_thu + total_income_fri + total_income_sat + total_income_sun



#Print Statements
print("Alright {} lets look at what you earned this week".format(name))
print("")

time.sleep(reading_tempo)

print("Your income on monday was:{}$".format(total_income_mon))
print("")

time.sleep(reading_tempo)

print("Your income on Tuesday was:{}$".format(total_income_tue))
print("")

time.sleep(reading_tempo)

print("Your income on Wednesday was:{}$".format(total_income_wed))
print("")

time.sleep(reading_tempo)

print("Your income on Thursday was:{}$".format(total_income_thu))
print("")

time.sleep(reading_tempo)

print("Your income on Friday was:{}$".format(total_income_fri))
print("")

time.sleep(reading_tempo)

print("Your income on Saturday was:{}$".format(total_income_sat))
print("")

time.sleep(reading_tempo)

print("Your income on Sunday was:{}$".format(total_income_sun))
print("")

time.sleep(reading_tempo)

print("Your income this week without taxes was:{}$".format(total_income_week))
print("")

time.sleep(reading_tempo)



#Taxes
taxes_percentage = int(input("what percentage of your income goes into taxes? : "))
taxes_calculation = (taxes_percentage / 100)
taxes_decimal = taxes_calculation * total_income_week 
income_after_taxes = total_income_week - taxes_decimal



#Income after Taxes printed
print("your income this week after taxes was:{}$".format(income_after_taxes))



#Ending program
print("Thats it, Thanks you {} using the income calculator!")