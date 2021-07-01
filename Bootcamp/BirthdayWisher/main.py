import pandas as pd
import datetime as dt
import random
import smtplib

# Extra Hard Starting Project

# 1. Update the birthdays.csv
birthday_data = pd.read_csv("birthdays.csv")
# 2. Check if today matches a birthday in the birthdays.csv
month_today = dt.datetime.now().month
day_today = dt.datetime.now().day


def pick_template():
    selection = random.randint(1, 3)
    try:
        with open(f"letter_templates/letter_{selection}.txt", "r") as template:
            letter_text: str = template.read()
    except FileNotFoundError:
        print("File not found")
    else:
        return letter_text


def send_mail(subject, message, recipient):
    my_email = "papersblack7@gmail.com"
    password = "-C.4Fv5j_LVh9NL"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=recipient, msg=f"Subject: {subject}\n\n"
                                                                        f"{message}")


for i, row in birthday_data.iterrows():
    if row["month"] == month_today and row["day"] == day_today:
        name = row["name"]
        email = row["email"]
        letter_template = pick_template()
        send_mail(subject=f"Happy Birthday! {name}", message=letter_template.replace("[NAME]", name), recipient=email)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
