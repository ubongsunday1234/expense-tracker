'''EXPENSE TRACKER VERSION 1.0'''
import csv
from datetime import date, time, datetime, timedelta, timezone


'''CLASSES'''
#FOR ADD BY CATEGORY
class total_category : #1. CREATE A CLASS THAT READS THE MATRIX AND ASSIGNS AN ATTRIBUTE TO THE CATEGORY AND AMOUNT
    def __init__(self, attrcategory_, attramount_):
        self.category_ = attrcategory_
        self.amount_ = attramount_
    def __repr__(self):
         return f"{self.category_}: {self.amount_}"


    '''FUNCTIONS'''
#INPUT EXPENSE DATA
def add_expense():
    print("enter the appropriate number from the category to input it's expense\n1 for groceries\t|\t2 for elctricity_bills\n3 for fuel\t|\t4 for entertainment\n5 for water_bills\t|\t6 for clothes\n7 for transportation\t|\t8 for internet\n9 for savings\t|\t10 for gifts_and_donations\n11 for tithe\t|\t12 for offering\n13 for TV\t|\t14 for children\n15 for others")
    input_ = input("enter the category:\n").strip()
    while True:
        if input_.isdigit():
            break
        else:
            print("input a valid number")
            input_ = input("enter the category:\n").strip()
    while int(input_)<0 or int(input_)>15 :
        print("input a valid number from the categories:")
        input_ = input("enter the category\n").strip()
    input_ = int(input_) #convert string to integer
    category_ = categories[input_]
    descriptions = input(f"input a description of the {category_}:\n") #description of the expenses
    amount = input("input an amount: ") #input for amount
    while True:
        if amount.replace(".","").isdigit():
            break
        else:
            print("!!!input a valid number!!!")
            amount = input("amount: ")
    date_ = date.today() # date of entry
    with open("CSVbooks.csv", "a", newline="") as file:
        content = csv.writer(file)
        content.writerow([int(ID)+1,date_.strftime("%Y-%m-%d"),category_,descriptions,amount])
    print(f"{category_} expense added successfully")


    #TOTAL EXPENSES
def total_expenses ():
    with open("CSVbooks.csv", "r", newline="") as file:
        content1 = csv.reader(file)
        content=[]
        for row in content1:
             content.append(row)
    sums = 0
    x=0
    y=len(content)-1 #number of expenses
    while True:
        if x<y:
            content1 = content[x+1][4]
            sums+= float(content1)
            x+=1
        else: 
            break
    print(f"Alright {name.upper()}, from {y} expenses your total expenses was____ ({sums})")



#TO SUM EXPENSES FOR ANY CATEGORY
def sum_category():
    with open("CSVbooks.csv", "r", newline="") as file: #2. WE READ TGE WHOLE FILE
         content1 = csv.reader(file)
         content=[]
         for row in content1:
             content.append(row) 
    category_amount = [] 
    for category in content: # 3. WE CREATE A LOOP THAT READS THE FILE LIST AND APPENDS TO AN EMPTY LIST The attributes of the class total_category
            category_amount.append(total_category(category[2],category[4]))
    print("enter the appropriate number from the category to input it's expense\n1 for groceries\t|\t2 for elctricity_bills\n3 for fuel\t|\t4 for entertainment\n5 for water_bills\t|\t6 for clothes\n7 for transportation\t|\t8 for internet\n9 for savings\t|\t10 for gifts_and_donations\n11 for tithe\t|\t12 for offering\n13 for TV\t|\t14 for children\n15 for others")
#USER INPUT ON WHICH CATEGORY TO ADD
    input_ = input("enter the category:\n").strip()
    while True:
        if input_.isdigit():
            break
        else:
            print("input a valid number")
            input_ = input("enter the category:\n").strip()
        
    while int(input_)<0 or int(input_)>15 :
        print("input a valid number from the categories:")
        input_ = input("enter the category:\n").strip() #convert string to integer
    input_ = int(input_)
    category_ = categories[input_]
    total_amount=0
    for obj in category_amount: # 4. ANOTHER LOOP THAT SUMS THE AMOUNT IF ITS HAS AN OBJECT THAT MATCHES THE ARGUMENT PASSED
        if obj.category_ == category_:
            total_amount+= float(obj.amount_)
    print(f"total_amount spent on {category_} is {total_amount}")


#TO PRINT  THE TOTAL EXPENSES FOR EACH CATEGORY
def all_categorysums() : 
    with open("CSVbooks.csv", "r", newline='') as file: #2. WE READ TGE WHOLE FILE
        content1 = csv.reader(file)
        content=[]
        for row in content1:
             content.append(row) 
    category_amount = []
    category_category = []
    amount_amount =[]
     
    for category in content: # 3. WE CREATE A LOOP THAT READS THE FILE LIST AND APPENDS TO AN EMPTY LIST The attributes of the class total_category
        category_amount.append(total_category(category[2],category[4]))#1. READ THE FILE
    for i in range(1,16): #4. RUN A FOR LOOP BETWEEN TGE RANGE OF CATEGORIES
        input_ = i
        category1 = categories[input_]
        total_amount=0
        for obj in category_amount: # 4. ANOTHER LOOP THAT SUMS THE AMOUNT IF the category from the range matches 
                if obj.category_ == category1:
                    total_amount+= float(obj.amount_)
        category_category.append(category1) # list of all category that  has gone through the loop
        amount_amount.append(total_amount) # list of all total that was given for each category
    temporary_category_amount = dict(zip(category_category, amount_amount)) #dictionary formed from the two list
    category_sums = sorted(temporary_category_amount.items(), key = lambda item:item[1], reverse = True) #sort tthrough the dictionary and arranged from highest to lowest
    for item in category_sums:
         print(f"{item[0]} = {item[1]}")



#TO GET THE EXPENSE FOR ANY DAY
def check_expense_by_date():
        with open("CSVbooks.csv", "r", newline="") as file: #read the file
             content = csv.reader(file)
             content1=[]
             for row in content:
                  content1.append(row)
        content1=content1[1:]
        all_date=[] 
        for expense in content1:
            all_date.append(datetime.strptime(expense[1], "%Y-%m-%d").date()) #make a date list from the converted date in each list
        datetime_expense = list(tuple(zip(all_date, content1))) #make a tuple with each date zipped to each line of the splited file and together for a list
        date_ = input("enter date of expense in this format\n(year-month-daye.g 2026-2-26: )") #get the date from user
        while True:
            try:
                datetime.strptime(date_, "%Y-%m-%d").date()
                break
            except ValueError:
                print("!!!!!INVALID DATE!!!!!")
                date_ = input("enter date of expense in this format\nyear-month-day (e.g 2026-2-26): ") #get the date from user
        date_ = datetime.strptime(date_, "%Y-%m-%d").date()
        total=0
        for row in datetime_expense: #print all data that matches that date
            if date_ == row[0]:
                row_ = row[1][1:5]
                print(f"date:{row_[0]},  bill:{row_[1]},  description:{row_[2]},  amount:{row_[3]}")
                total += float(row_[3]) #add the amount and print a message
        if date_ not in all_date:   
                print(f"No expense on {date_}")
        print(f"your total expense is {total} on {date_}")  


#TO GET EXPENSES FOR ANY MONTH
def monthly_expenses():
        with open("CSVbooks.csv", "r", newline='') as file:  # read the file
            content = csv.reader(file)
            content1=[]
            for row in content:
                 content1.append(row)
        content1=content1[1:]
        all_date = []
        all_date_truncated = []
        for expense in content1:
            # make a date list from the converted date in each list
            all_date.append(datetime.strptime(expense[1], "%Y-%m-%d").date())
        for date_ in all_date: #convert the time to just year and month
             date1 = date_.strftime('%Y-%m')
             date1 = datetime.strptime(date1, "%Y-%m").date()
             all_date_truncated.append(date1)
        # make a tuple with each all_truncate_date zipped to each line of the splited file and together for a list
        datetime_expense = list(tuple(zip(all_date_truncated, content1)))
        # get the date from user
        date_ = input("enter only year and month in this format year-month e.g 2026-07 or 2020-11: ")
        while True:
             try:
                datetime.strptime(date_, "%Y-%m").date()
                break
             except ValueError:
                print("!!!!!INVALID DATE!!!!!")
                date_ = input("enter date of expense in this format\nyear-month-day (e.g 2026-2-26): ") #get the date from user
        date_ = datetime.strptime(date_, "%Y-%m").date()
        total=0
        for row in datetime_expense: #print all data that matches that date
            if date_ == row[0]:
                row_ = row[1][1:5]
                print(f"date:{row_[0]},  bill:{row_[1]},  description:{row_[2]},  amount:{row_[3]}")
                total += float(row_[3]) #add the amount and print a message
        if date_ not in all_date_truncated:   
            print(f"No expense on {date_}")
        print(f"\n\nyour total expense is {total} for {date_.strftime("%B")}")


#DELETE EXPENSES BY ID
def delete_expenses_ID():
        with open("CSVbooks.csv", "r", newline="") as file:  # read the file
             content0 = csv.reader(file)
             content=[]
             for row in content0:
                  content.append(row)
        content1 = content[1:]
        ID_UPDATE=[]
        for expense in content1:
            # make a date list from the ID in each list
            ID_UPDATE.append(expense[0])
        # make a DICTIONARY with each ID zipped to each line of the splited file and together for a list
        ID_EXPENSE = dict(zip(ID_UPDATE, content1))
        # get the date from user
        ID_ = input("ENTER ID OF EXPENSE TO BE DELETED: ").strip()
        while True:
            if ID_.isdigit():
                 break
            else:
                print("input a valid number")
                ID_ = input("ENTER ID OF EXPENSE TO BE DELETED: ").strip()
        while int(ID_)<0 or int(ID_)>len(ID_EXPENSE) :
                print("input a valid number from the categories:")
                ID_ = input("ENTER ID OF EXPENSE TO BE DELETED: ").strip() #get the date from user
        ID_ = str(ID_)
        del ID_EXPENSE[ID_]
        ID = 0
        with open("CSVbooks.csv", "w", newline="") as file:
             file=csv.writer(file)
             file.writerow(["ID","DATE","CATEGORY","DESCRIPTION","AMOUNT"])
        for key, expense in ID_EXPENSE.items():
            ID+=1
            with open("CSVbooks.csv", "a", newline="") as file:
                 file=csv.writer(file)
                 file.writerow([ID,expense[1],expense[2],expense[3],expense[4]])
        print("DELETED")



def delete_expenses_DATE():
        with open("CSVbooks.csv", "r", newline="") as file:  # read the file
             content0 = csv.reader(file)
             content=[]
             for row in content0:
                  content.append(row)
        content1 = content[1:]
        all_date = []
        for expense in content1:
            # make a date list from the converted date in each list
            all_date.append(datetime.strptime(expense[1], "%Y-%m-%d").date())
        # make a tuple with each date zipped to each line of the splited file and together for a list
        datetime_expense = list(zip(all_date, content1))
        # get the date from user
        date_ = input("enter the year and month and in this format year-month- day e.g 2026-07-01 or 2020-11-16 : ")
        while True:
             try:
                datetime.strptime(date_, "%Y-%m-%d").date()
                break
             except ValueError:
                print("!!!!!INVALID DATE!!!!!")
                date_ = input("enter date of expense in this format\nyear-month-day (e.g 2026-2-26): ") #get the date from user
        date_ = datetime.strptime(date_, "%Y-%m-%d").date()
        with open("CSVbooks.csv", "w", newline="") as file:
            file=csv.writer(file)
            file.writerow(["ID","DATE","CATEGORY","DESCRIPTION","AMOUNT"])
        for expense in datetime_expense:
                ID=0
                if date_ not in expense:
                    ID+=1
                    with open("CSVbooks.csv", "a", newline="") as file:
                        file=csv.writer(file)
                        file.writerow(expense[1])
                else:
                     print("DELETED")
        if date_ not in datetime_expense:
             print(f"no expense found on {date_}") 
                                    



#TO DELETE ALL EXPENSES
def blank_expenses():
        with open("CSVbooks.csv", "r", newline="") as file:  # read the file
            content0 = csv.reader(file)
            content=[]
            for row in content0:
                 content.append(row)
        header = content.pop(0)
        with open("CSVbooks.csv", "w", newline="") as file:
            file=csv.writer(file)
            file.writerow(header)        
            print("expenses ALL CLEARED") 


#CHECK IF MONTHLY BUDGET HAS BEEN SURPASSED
def monthly_budget():
        with open("CSVbooks.csv", "r", newline='') as file:  # read the file
            content = csv.reader(file)
            content1=[]
            for row in content:
                 content1.append(row)
        content1=content1[1:]            
        all_date = []
        all_date_truncated = []
        for expense in content1:
            # make a date list from the converted date in each list
            all_date.append(datetime.strptime(expense[1], "%Y-%m-%d").date())
        for date_ in all_date: #convert the time to just year and month
             date1 = date_.strftime('%Y-%m')
             date1 = datetime.strptime(date1, "%Y-%m").date()
             all_date_truncated.append(date1)
        # make a tuple with each all_truncate_date zipped to each line of the splited file and together for a list
        datetime_expense = list(tuple(zip(all_date_truncated, content1)))
        # get the date from user
        budget = input ("whats your budget for this month: ").strip()
        while True:
             if budget.isdigit():
                  break
             else:
                  print("!!!INVALID number!!!")
                  budget = (input ("whats your budget for this month: ").strip())
        budget=float(budget)
        total = 0
        i=0
        for month in datetime_expense:
            if month[0]== datetime_expense[-1][0]:
                 total += float(month[1][4])
                 i+=1
        print(f"amount expended so far is {total}")
        if budget>total:
             print(f"\nGood job!!!, you have not exceeded your monthly budget of {budget}")
        elif budget==total:
             print("you have reached the limit of your budget ({budget})")
        else:
             print(f"\nyou have exceeded your budget of {budget}")


#DAILY LIMIT CHECK
def daily_limit():
        with open("CSVbooks.csv", "r", newline="") as file:  # read the file
            content = csv.reader(file)
            content1=[]
            for row in content:
                 content1.append(row)
        content1=content1[1:]
        all_date = []
        for expense in content1:
            # make a date list from the converted date in each list
            all_date.append(datetime.strptime(expense[1], "%Y-%m-%d").date())
        # make a tuple with each all_date zipped to each line of the splited file and together for a list
        datetime_expense = list(tuple(zip(all_date, content1)))
        # get the date from user
        budget = input ("whats your daily limit for this today: ").strip()
        while True:
             if budget.isdigit():
                  break
             else:
                  print("!!!INVALID number!!!")
                  budget = (input ("whats your budget for today: ").strip())
        budget=float(budget)
        total = 0
        i=0
        for date_ in datetime_expense:
            if date_[0]== date.today():
                 total += float(date_[1][4])
                 i+=1
        print(f"amount expended so far is {total}")
        if budget>total:
             print(f"\nGood job!!!! {name} you have not exceeded your daily limit of {budget}")
        elif budget==total:
             print("!!!WARNING: you have reached the limit of your budget ({budget})")
        else:
             print(f"\n!!!ALERT!!!ALERT!!!\nyou have exceeded your daily budget of {budget}")



#PRINT AND EXPORT MONTHLY REPORT
def monthly_report_year():
        with open("CSVbooks.csv", "r", newline="") as file:  # read the file
            content = csv.reader(file)
            content1=[]
            for row in content:
                 content1.append(row)
        content1=content1[1:]
        all_date = []
        results1 =""
        all_date_truncated = []
        for expense in content1:
            # make a date list from the converted date in each list
            all_date.append(datetime.strptime(expense[1], "%Y-%m-%d").date())
        for date_ in all_date: #convert the time to just year and month
             date1 = date_.strftime('%Y-%m')
             date1 = datetime.strptime(date1, "%Y-%m").date()
             all_date_truncated.append(date1)
        # make a tuple with each all_truncate_date zipped to each line of the splited file and together for a list
        datetime_expense = list(tuple(zip(all_date_truncated, content1)))
        yearlst_ = datetime_expense[-1][1]
        yearlst_ = datetime.strptime(yearlst_[1], "%Y-%m-%d")
        yearlst_= yearlst_.year
        date_ = datetime_expense[1][0]
        date_=date_.replace(year=yearlst_)
        total=0
        for i in range (1,13):
             date_ = date_.replace(month=i)
             for row in datetime_expense: #print all data that matches that date
                  if date_ == row[0]:
                        row_ = row[1][1:5]
                        total += float(row_[3]) #add the amount and print a message
             print (f"{date_.strftime("%Y-%B")}: {total}")
             results1+= (f"{date_.strftime("%Y-%B")}: {total}\n")
        return results1


#PRINT AND EXPORT CATEGORY EXPENSE FOR CURRENT YEAR
def all_categorysums_year() : 
    with open("CSVbooks.csv", "r",newline='') as file: #2. WE READ TGE WHOLE FILE
            content = csv.reader(file)
            content1=[]
            for row in content:
                 content1.append(row)
    content1=content1[1:]
    content_year=[]
    all_date_truncated=[]
    all_date = []
    results = ""
    for expense in content1:
                # make a date list from the converted date in each list
                all_date.append(datetime.strptime(expense[1], "%Y-%m-%d").date())
    for expense in content1:
                # make a date list from the converted date in each list
                all_date.append(datetime.strptime(expense[1], "%Y-%m-%d").date())
    for date_ in all_date: #convert the time to just year and month
        date1 = date_.strftime('%Y-%m')
        date1 = datetime.strptime(date1, "%Y-%m").date()
        all_date_truncated.append(date1)
            # make a tuple with each all_truncate_date zipped to each line of the splited file and together for a list
    datetime_expense = list(tuple(zip(all_date_truncated, content1)))
    yearlst_ = datetime_expense[-1][1]
    yearlst_ = datetime.strptime(yearlst_[1], "%Y-%m-%d").date()
    yearlst_= yearlst_.year
    date_ = datetime_expense[1][0]
    date_=date_.replace(year=yearlst_)
    for date1 in datetime_expense:
          if date_==date1[0]:
               content_year.append(date1[1])
    category_amount = []
    category_amount_ = {}
    category_category = []
    amount_amount =[]
    for category in content_year: # 3. WE CREATE A LOOP THAT READS THE FILE LIST AND APPENDS TO AN EMPTY LIST The attributes of the class total_category
        category_amount.append(total_category(category[2],category[4]))#1. READ THE FILE
    for i in range(1,16): #4. RUN A FOR LOOP BETWEEN TGE RANGE OF CATEGORIES
        input_ = i
        category1 = categories[input_]
        total_amount=0
        for obj in category_amount: # 4. ANOTHER LOOP THAT SUMS THE AMOUNT IF the category from the range matches 
                if obj.category_ == category1:
                    total_amount+= float(obj.amount_)
        category_category.append(category1) # list of all category that  has gone through the loop
        amount_amount.append(total_amount) # list of all total that was given for each category
    temporary_category_amount = dict(zip(category_category, amount_amount)) #dictionary formed from the two list
    category_sums = sorted(temporary_category_amount.items(), key = lambda item:item[1], reverse = True) #sort tthrough the dictionary and arranged from highest to lowest
    for item in category_sums:
        results+= (f"{item[0]}={item[1]}\n")
        print(f"{item[0]} = {item[1]}")
    return results
    
                        

# #CREATE REPORT
def report_():
    results = all_categorysums_year()
    results1 = monthly_report_year()
    results2 =smallest_largest_expense()
    results3=Average_amount()
    with open("CSVreport.txt", "w") as file:
         file.write(f"{"=" * 10}MONTHLY REPORT{"="*10}\n{results1}\n{"=" * 10}CATEGORY REPORT{"="*10}\n{results}\n{"=" * 10}SMALLEST AND LARGEST EXPENSE{"=" * 10}\n{results2}\n{"=" * 10}AVERAGE EXPENSE{"=" * 10}\n{results3}") 
    print(f"{"=" * 10}MONTHLY REPORT{"="*10}")
    monthly_report_year()
    print("\n\n\n")
    print(f"{"=" * 10}CATEGORY REPORT{"="*10}")
    all_categorysums_year()
    print("\n\n\n")
    print(f"{"=" * 10}SMALLEST AND LARGEST EXPENSE{"="*10}")    
    print("\n\n\n")
    print(f"{"=" * 10}AVERAGE EXPENSE{"=" * 10}")
    print("\n\nTHIS HAS BEEN SAVED IN A FILE CALLED report.txt open you local files to access it")



#AVERAGE AMOUNT SPENT
def smallest_largest_expense():
        with open("CSVbooks.csv", "r", newline="") as file:  # read the file
            content = csv.reader(file)
            content1=[]
            for row in content:
                 content1.append(row)
        content1=content1[1:]
        amount_list = []
        all_date_truncated = []
        for expense in content1:
            all_date_truncated.append(expense[1:])
            # make a date list from the converted date in each list
            amount_list.append(expense[4]) 
        amount_content = dict(zip(amount_list,all_date_truncated))
        amount_list.sort()
        largest=amount_list[-1]
        smallest=amount_list[0]
        return f"The largest expense made is {(amount_content[amount_list[-1]][3]).replace("\n","")}, on {(amount_content[amount_list[-1]][0])} for {(amount_content[amount_list[-1]][1])}\nThe smallest expense is {(amount_content[amount_list[0]][3]).replace("\n","")}, on {(amount_content[amount_list[0]][0])} for {(amount_content[amount_list[0]][1])}"



def Average_amount():
        with open("books.txt", "r") as file:  # read the file
            content = file.readlines()
        content1 = []
        amount_list = []
        all_date_truncated = []
        for expense in content[1:]:  # split each of the expenses from '|'
            expense = expense.split("|")
            content1.append(expense)
        for expense in content1:
            # make a date list from the converted date in each list
            amount_list.append(float(expense[4])) 
        sum=0
        for amount in amount_list:
             sum+=amount
        average=sum/(len(amount_list))
        return f"Average amount spent daily is {average}"







'''''''''''''''''''''''''''DATA ENTRY'''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''DATA ENTRY'''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''DATA ENTRY'''''''''''''''''''''''''''''''''
     




'''name data collection'''
name = input ("please enter your name: ").strip()
while name == '' or not name.isalpha() or name == None:
    print("enter a valid name")
    name = input ('please enter your name: ').strip()
else:
    name= name.capitalize()
    print(f"hi {name}, you are welcome to use the expense tracker\n\t\ti hope you find it useful\n\n\n")


'''ASSIGNMENT OF IDs to expense_tracker'''
try:
    with open("CSVbooks.csv", "r", newline="") as file:
         content1 = csv.reader(file) #read the whole file#split the lines
         content=[]
         for row in content1:
              content.append(row)
    ID = content[-1][0]
except FileNotFoundError :
     print("nope not found")
     ID = 0 #if program is startimng for the first time   
     print(f"{name}, please enter your first expense")
     with open("CSVbooks.csv", "w", newline="") as file:
          content = csv.writer(file)
          content.writerow(["ID","DATE","CATEGORY","DESCRIPTION","AMOUNT"])      
         
    
'''list of categories'''
categories = {
              1:"groceries", 2:"elctricity_bills", 3:"fuel", 
              4:"entertainment",5:"water_bills", 6:"clothes", 
              7:"transportation", 8:"internet",9:"savings",
              10:"gifts_and_donations", 11:"tithes", 12:"offering",
              13:"TV", 14:"children", 15:"others"
              } #list of every category available

'''decision to add expense or delete expense'''
print("TO ADD AN EXPENSE TYPE (1)\nTO GET THE TOTAL SUMS TYPE (2)\nTO GET EXPENSE FOR ANY DATE TYPE (3)\nTO GET EXPENSE FOR ANY MONTH TYPE (4)\nTO CHECK IF YOUR MONTH/DAILY BUDGET HAS BEEN EXCEEDED TYPE (5)\nTO GET REPORT OF EXPENSES FOR CURRENT YEAR TYPE (6)\nDELETE AN EXPENSE TYPE (0)")
booksaction = input("enter: ").strip() #variable to decide if tp enter expenses or delete an expense
while True:
    if booksaction.isdigit():
        if 0<=int(booksaction)<8 :
            break
        else:
                print("!!!enter a valid number, either '1' to add expese\n'2' for total expenses\n'0' to delete an expense!!!")
                booksaction = input("enter 1 or 0\n").strip()
    else:
        print("!!!enter a valid number, either '1' to add expese or '0' to delete an expense!!!")
        booksaction = input("enter 1 or 0\n").strip()

'''ADDING EXPENSES AND DELETING EXPENSES'''
if int(booksaction) == 1:
    add_expense()
elif int(booksaction) ==2:
    total_or_category = input("\nTYPE (1) FOR TOTAL EXPENSE\nTYPE (2) FOR TOTAL EXPENSES OF ANY CATEGORY\nTYPE (3) FOR TOTAL EXPENSES FOR EVERY CATEGORY:\n")
    while not total_or_category.isdigit() or not 0<int(total_or_category)<5:
        print("!!!!!input a valid number (1,2,3)!!!!!\n")
        total_or_category =input(": ")              
    if int(total_or_category) == 1:
        total_expenses()
    elif int(total_or_category) == 2:
        sum_category()
    elif int(total_or_category) == 3:
        all_categorysums()
elif int(booksaction) ==3 :
    check_expense_by_date()
elif int(booksaction) == 4:
        monthly_expenses() 
elif int(booksaction) == 0: #DELETION
    ID1 = input("TYPE (1) TO DELETE BY ID\nTYPE (2) TO DELETE BY DATE\nTYPE (3) TO CLEAR ALL EXPENSE\nenter: ")
    while not ID1.isdigit() or not 0<int(ID1)<4:
        print("!!!!!input a valid number (1 or 2 or 3)!!!!!\n")
        ID1 =input(": ") 
    if int(ID1) == 1:
        delete_expenses_ID() 
    elif int(ID1) == 2:
        delete_expenses_DATE()
    elif int(ID1) == 3:
        blank_expenses()
elif int(booksaction) == 5:
     print("TYPE (1) FOR MONTHLY BUDGET CHECK\nTYPE (2) FOR DAILY LIMIT CHECK")
     check_ = input(": ")
     while True:
          if check_.isdigit() and 0<int(check_)<3:
               break
          else:
               print("!!!INVALID INPUT!!!\nENTTER EITHER (1) or (2)")
               check_ = input(": ")
     check_= int(check_)
     if check_==1:
          monthly_budget()
     elif check_ == 2:
          daily_limit()
elif int(booksaction) == 6:
     report_()
