import math, random, smtplib, os
digits = "123456789"
OTP = ""
for i in range(6):
    OTP += digits[math.floor(random.random() * 10)]
if __name__ == "__main__":
    otp = OTP + " is your 6 digit OTP."
mssg = otp
a = smtplib.SMTP("smtp.gmail.com",587)
a.starttls
a.login("Your Gmail Account","password")
emailid = input("Enter you email : ")
a.sendmail("&&&&&&&&&&&",emailid,mssg)
b = input("Enter your OTP --> ")
if a == OTP:
    print("Verified")
else:
    print("Not verified please check your OTP again!")

import os
import math
import random
import smtplib

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("Your Gmail Account", "You app password")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")