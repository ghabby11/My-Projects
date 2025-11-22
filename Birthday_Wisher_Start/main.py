##################### Normal Starting Project ######################
import datetime
import random
import smtplib

import pandas
# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)

import datetime as dt
now = dt.datetime.now()
day_of_the_week = now.weekday()
today = (now.month, now.day)

# HINT 2: Use pandas to read the birthdays.csv
d= pandas.read_csv("birthdays.csv")

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
data= {(data_row.month,data_row.day): data_row for (index, data_row) in d.iterrows()}


#Dictionary comprehension template for pandas DataFrame looks like this:
# = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
if today in data:
    numbers= [1,2,3]
    random_letter = random.choice(numbers)
    if random_letter == 1:
        with open("letter_templates/letter_1.txt") as file:
            let = file.read()
    elif random_letter == 2:
        with open("letter_templates/letter_2.txt") as file:
            let = file.read()
    else:
        with open("letter_templates/letter_3.txt") as file:
            let = file.read()

    letter = let.replace("[NAME]", data[today]["name"])
    print(letter)



# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv

# HINT 1: Think about the relative file path to open each letter.
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.


my_email = "gabpythontest@gmail.com"
password ="gdlooyovxustfoyl"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="gabrielacehood@yahoo.com",
                        msg=f"Subject:Happy Birthday\n\n {letter}")
#
