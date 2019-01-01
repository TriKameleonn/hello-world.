class birthdate:
    month=input("What is your Birth Month? in MM?")
    day=input("What is Your Birth Day? in DD?")
    year=input('What is your Birth Year? in YY?')         
if birthdate.month == "01":
    print("january")
if birthdate.month == "02":
    print("Febuary")
if birthdate.month == "03":
    print("march")
if birthdate.month == "04":
    print("april")
if birthdate.month == "05":
    print("may")
if birthdate.month == "06":
    print("june")
if birthdate.month == "07":
    print("july")
if birthdate.month == "08":
    print("augest")
if birthdate.month == "09":
    print("september")
if birthdate.month == "10":
    print("october")
if birthdate.month == "11":
    print ("november")
if birthdate.month == "12":
    print ("december")
if birthdate.day == "1":
    print(birthdate.day, "st")
if birthdate.day == "2":
    print(birthdate.day, "nd")
if birthdate.day == "3":
    print(birthdate.day, "rd")
if(day >=4) and (day <=20):
    print("th")
   


