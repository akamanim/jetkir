from twilio.rest import Client

def send_sms(phone_number, message):
    account_sid = "ACa92db69105d2c0582a1199e879c54bf0"
    auth_token = "75fe0b2d21f88bdc9d358c06059019b5"
    from_number = "+996550171999"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_=from_number,
        to=phone_number
    )

    print("SMS sent with SID:", message.sid)