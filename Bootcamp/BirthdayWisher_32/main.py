import random
import smtplib
import datetime as dt


def send_mail(subject, message):
    my_email = "papersblack7@gmail.com"
    password = "-C.4Fv5j_LVh9NL"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="ankitparashar88@gmail.com", msg=f"Subject: {subject}\n\n"
                                                                                          f"{message}")


def generate_quote():
    try:
        with open("quotes.txt", "r") as quotes:
            quote_list = quotes.readlines()
    except FileNotFoundError:
        print("File not found")
    else:
        return random.choice(quote_list)


now = dt.datetime.now()
if now.weekday() == 6:
    send_mail(subject="Your quote for today", message=generate_quote())
