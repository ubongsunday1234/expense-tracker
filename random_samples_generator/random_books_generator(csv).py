#open a file and write thsi header ID|DATE|CATEGORY|DESCRIPTION|AMOUNT|
#ID COUNTS PROGRESSIVELY EACH TIME
#RANDOM DATE GENERATED
#PASTE THE CATEGORY NAME AS DESCRIPTION
#generate random amount 
#aranage them ID|DATE|CATEGORY|DESCRIPTION|AMOUNT|
import csv
import random
import calendar
from datetime import date, time, datetime, timezone, timedelta 


'''header into file'''
with open("csvrandom_books.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ID","DATE","CATEGORY","DESCRIPTION","AMOUNT"])


'''ID'''
ID = 0

'''''YEAR'''
rand_year = random.randint(2000,3000) #RANDOM YEAR

'''RANDOM DATE'''
def generate_date():    
    rand_month = random.randint(1,12) #RANDOM MONTH
    #ASSIGN APPROPRIATE DAYS TO EACH MONTH WITH RANDOM DAYS
    if rand_month ==9 or rand_month==4 or rand_month == 6 or rand_month == 11:
        rand_day = random.randint(1,30)
    elif rand_month==2:
        if calendar.isleap(rand_year):
            rand_day= random.randint(1,29)
            print("it's a leap year")
        else:
            rand_day= random.randint(1,28)
    else:
        rand_day = random.randint(1,31)
    random_date = date(rand_year,rand_month,rand_day)
    return random_date


'''RANDOM CATEGORY'''
def generate_category():
    #LIST ALL CATEGORIES
    random_category = random.choice([
        "groceries", "elctricity_bills", 
        "fuel","entertainment","water_bills", 
        "clothes", "transportation", "internet",
        "savings","gifts_and_donations", "tithes", 
        "offering","TV", "children", 
        "others"
                ])
    return random_category


'''RANDOM AMMOUNT'''
def generate_amount(): #GENERATE AMOUNT
    random_amount = random.randint(1000,10000000)
    return random_amount

content =[["ID","DATE","CATEGORY","DESCRIPTION","AMOUNT"]]
for i in range(1,201):
        random_amount = generate_amount()
        random_category = generate_category()
        random_date = generate_date()
        ID +=1
        content.append([ID,random_date.strftime("%Y-%m-%d"),random_category,random_category,random_amount])

'''ARRANGE CONTENT BY DATE'''
content1=[]
content_ =[]
content2=[]
entered_date=[]
arranged_expenses = [["ID","DATE","CATEGORY","DESCRIPTION","AMOUNT"]]
ID=0#read each line and split by |
for expense in content[1:]: #remove the IDs
    content_.append(expense[1:5])
for expense in content_:#create a list for each date using loop
    entered_date.append(datetime.strptime(expense[0],"%Y-%m-%d").date())
dict_date_expense = dict(zip(entered_date, content_)) #make a dictionary with it using the date as the key and each vlaue in the first readlines
entered_date.sort() #sort the date from earliest to  latest 
for sorted_date in entered_date:#using the arranged date as key make a new list of lines arranged
        ID+=1
        with open("csvrandom_books.csv", "a", newline="") as file : #append the list into the file
             file=csv.writer(file)
             file.writerow([ID,dict_date_expense[sorted_date][0],dict_date_expense[sorted_date][1],dict_date_expense[sorted_date][2],dict_date_expense[sorted_date][3]])
print("done")



