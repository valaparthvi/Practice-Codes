"""
/usr/bin/python3.5
Packages used: django_otp, twilio
To install django_otp: pip install django_otp
To install twilio: pip install twillio
Obtain a twilio account_sid, auth_token and phone number.
"""


from django_otp.oath import TOTP
from binascii import hexlify
from os import urandom
from twilio.rest import TwilioRestClient


def send_sms(phone, msg_to_be_sent):
    # creating TwilioRestClient object that will be used
    # to send request to Twlio Rest API.
    client = TwilioRestClient(
        account="",
        token=""
    )
    # sending message to the phone number
    client.messages.create(to=phone, from_="", body=msg_to_be_sent)


def generate_token():
    # enter a phone number where you want to send the token.
    phone_num = ""

    # hex-encoded secret key that will be used to create totp tokens
    secret_key = hexlify(urandom(20))

    # creating TOTP object that will generate a new token after every `step`
    # seconds
    token = TOTP(secret_key, step=300)

    # message body to be sent to the phone number
    message = "Your token is: %s. It is valid for 5 minutes." % str(
        token.token())

    send_sms(phone=phone_num, msg_to_be_sent=message)
    verify_token(phone=phone_num, token_obj=token)


def verify_token(phone, token_obj):
    try:
        your_input = int(input("Enter the token you received: "))
    except ValueError:
        print("Enter only decimal value.")
        your_input = int(input("Enter the token you received: "))

    if token_obj.verify(your_input):
        print('Phone is verified')
        message = "Congratulations! Your phone has been successfully verified."
        send_sms(phone=phone, msg_to_be_sent=message)
    else:
        print('Phone could not be verified!')


if __name__ == '__main__':
    generate_token()
