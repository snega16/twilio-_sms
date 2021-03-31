from twilio.rest import Client

account_sid='your sid'
auth_token='your token'

client=Client(account_sid,auth_token)
message=client.messages\
              .create(
                   body="message to be delivered",
                   from_= 'number',
                   to='number'
            )
print(message.sid)
