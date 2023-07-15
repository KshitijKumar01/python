import smtplib

my_email = "ridebrave3801@gmail.com"
password = "Ridebrave*123"
generated_pass = "wwgzgpwtxxduwfiy"
to_email = "kshitijkumar.kk.sunny@gmail.com"

# #creating connection
# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls()
# connection.login(user=my_email, password=generated_pass)
# connection.sendmail(from_addr=my_email, to_addrs="kshitijkumar.kk.sunny@gmail.com", msg="Subject:Helloooo\n\nthis the body")
# print("mail sent")
# connection.close()


import datetime as dt
import random
PATH = "C:\\Users\\acer\\Desktop\\CHANDIGARH UNIVERSITY\\AI ML\\python\\day32\\quotes.txt"

now = dt.datetime.now()
weekday = now.weekday()
if(weekday == 2):
    with open(PATH, 'r') as data_file:
        data = data_file.readlines()
        quote = random.choice(data)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=generated_pass)
        connection.sendmail(from_addr=my_email, 
            to_addrs=to_email, 
            msg=f"Subject:wednesday Motivation\n\n{quote}")
    
     



    