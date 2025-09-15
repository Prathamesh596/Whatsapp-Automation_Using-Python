from twilio.rest import Client
from datetime import datetime,timedelta
import time 

account_sid='take it from twilio' 
auth_token='take it from twilio'

client = Client(account_sid, auth_token)

def send_whatsapp_message(recipent_number, message_body):
  try:
    message=client.messages.create(
      from_='whatsapp:take number from twilio',
      body = message_body,
      to=f'whatsapp:{recipent_number}'
    )
    print(f'Message sent successfully! Message SID{message.sid}')

  except Exception as e:
    print('An error occured')
    
name=input('Enter your name:')
recipient_number=input('Enter the recipient number with country code (e.g., +1234567890):')
message_body=input(F'enter the message you want to send to {name}: ')

date_str = input('Enter the date to send the message (YYYY-MM-DD):')
time_str = input('Enter the time to send the message (HH:MM in 24-hour format):')

scheduled_datetime = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M')
current_datetime = datetime.now()
delay_seconds = (scheduled_datetime - current_datetime).total_seconds()
if delay_seconds > 0:
  print(f'Scheduling message to be sent at {scheduled_datetime}')
  time.sleep(delay_seconds)
  send_whatsapp_message(recipient_number, message_body)
else:
  print('The scheduled time is in the past. Please enter a future date and time.')