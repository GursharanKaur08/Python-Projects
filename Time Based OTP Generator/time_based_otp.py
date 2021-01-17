import pyotp
from timeit import default_timer as timer

# base32 secret key --> 32 characters are used while generating this private key
# length of this key is 16

# 32 characters ---> A-Z(uppercase) and 2-7
# Space -- for per character, there is a space of 5 bits. Total memory space ---> 160 bit ---> 20 bytes

with open('secret_key.txt','r') as rf:
    base_32_secret_key = rf.read()

# print(base_32_secret_key)


# OTP generation

Timebasedotp = pyotp.TOTP(base_32_secret_key)
current_otp = Timebasedotp.now()

# print(current_otp)

def verification(time_gap, Entered_otp, otp, Timebasedotp):
    if (time_gap)<30 and (Entered_otp==otp):
        print("Hello User u are successfully verified.$$")
        return
    elif (time_gap)<30 and (Entered_otp!=otp):
        print("Entered OTP is not correct. Hence u are not verified. That's why we have resent u a new OTP.")
        resend_otp(Timebasedotp)
    elif (time_gap)>=30:
        print("Time up!!!")
        resend_otp(Timebasedotp)


def resend_otp(Timebasedotp):
    current_otp = Timebasedotp.now()
    while True:
        new_current_otp = Timebasedotp.now()
        if new_current_otp!=current_otp:
            print(f'Curent_otp : {new_current_otp}')
            start = timer()
            enter_otp = input("Enter current otp : ")
            end = timer()
            resend_time_interval = end-start
            print(f'Time taken: {resend_time_interval}')
            verification(resend_time_interval, enter_otp, new_current_otp, Timebasedotp)
            break
            return



while True:
    new_current_otp = Timebasedotp.now()
    if new_current_otp !=current_otp:
        print(f'Current_otp: {new_current_otp}')
        start = timer()
        enter_otp = input("Enter current_otp : ")
        end = timer()

        time_interval = end-start
        print(f"Time taken : {time_interval}")
        verification(time_interval, enter_otp, new_current_otp, Timebasedotp)
        break
