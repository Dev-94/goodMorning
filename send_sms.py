from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACda05149c0b4d416716ba2ba9e217ae3b"
# Your Auth Token from twilio.com/console
auth_token  = "3d46e40bd95ee85114d46c387c78bc3c"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18172668041" , 
    from_="+13343669860",
    body="Good Morning")

print(message.sid)