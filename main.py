# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib
import os

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

bday_dates = pandas.read_csv("birthdays.csv")
bday_dates_dict = bday_dates.to_dict(orient="records")

date_today = dt.datetime.now()
month = date_today.month
day = date_today.day

for bday_celebrant in bday_dates_dict:
    print(bday_celebrant)
    if bday_celebrant["month"] == month and bday_celebrant["day"] == day:
        letter_number = random.randint(1,3)
        print(letter_number)
        with open(f"letter_templates/letter_{letter_number}.txt", mode = "r") as letter:
            file = letter.read()
            msg_to_be_sent = file.replace("[NAME]", f"{bday_celebrant["name"]}")
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            print("Starting TLS...")
            connection.starttls()
            print("Logging in...")
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            print("Sending email...")
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=bday_celebrant["email"],
                                msg=f"Subject: Happy Birthday!\n\n"
                                    f"{msg_to_be_sent}")
            print("Email sent.")
