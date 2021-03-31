from twilio.rest import Client

account_sid='your sid'
auth_token='your token'

client=Client(account_sid,auth_token)
message=client.messages\
              .create(
                   body="Whoa you recieved my message",
                   from_= 'number',
                   to='number'
            )
print(message.sid)
