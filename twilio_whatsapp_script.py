# Installing twilio if its not already installed
# try:
#     from pip import main as pipmain
# except ImportError:
#     from pip._internal import main as pipmain

# # from pip._internal import main as pipmain

# pipmain(['install', 'twilio'])

from twilio.rest import Client
import requests
import json
from datetime import datetime

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
TWILIO_ACCOUNT_SID = 'AC2a4fe5daa22009a0d95c5d730a954c5d'
AUTH_TOKEN = '37b92f6721dcb4fd027ad1c17eee6c49'
client = Client(TWILIO_ACCOUNT_SID, AUTH_TOKEN)

# Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'

# Test Numbers
#to_whatsapp_number='whatsapp:+256757163101'
#to_whatsapp_number='whatsapp:+256751964081'
#to_whatsapp_number='whatsapp:+256753586752'

# contact_dict = {"Essy" : "+917042020895"}
contact_dict = {"Joshua" : "+256751964081"}
phone_number = 'whatsapp:+256751964081'
single_number = 'whatsapp:+256751964081'
test_message = 'Hey there!'

# Sending messages to a contacts in the contact_dict
# for key, value in contact_dict.items():
#     msg_whats_ = client.messages.create(body='Hey {}!'.format(key),
#                        from_=from_whatsapp_number,
#                        to='whatsapp:' + value)

# Sending message to single number
def send_message(number, body):
    msg_whats_ = client.messages.create(body=body,
                       from_=from_whatsapp_number,
                       to=number)  
    
send_message(single_number, test_message)

# Qeurying messages details of a given number
def get_messages_data(number):
    chat_json = {}
    chat_history = []

    for single_message in client.messages.list():
        if(single_message.to == number): # we can remove this if statement to get a dictionary of all the chat history in our twilio account

            date_time = single_message.date_sent
            date_format = "%Y-%m-%d"
            time_format = "%H:%M:%S"
            date = datetime.strftime(date_time, date_format)
            time = datetime.strftime(date_time, time_format)

            if(single_message.direction == 'outbound-reply'):
                # print('inbox')
                single_chat = {
                    "message_contact": single_message.to, 
                    "message_text": single_message.body, 
                    "box": "Inbox", 
                    "status": "",
                    "message_date": date, 
                    "message_time": time
                  }
            elif (single_message.direction == 'outbound-api'):
                # print('outbox')
                single_chat = {
                    "message_contact": single_message.to, 
                    "message_text": single_message.body, 
                    "box": "Outbox", 
                    "status": single_message.status,
                    "message_date": date, 
                    "message_time": time
                  }
            chat_history.append(single_chat)

    # print(chat_history)
    chat_json["whatsapp_msgs"] = chat_history
    # print(chat_json)
    return chat_json

print(get_messages_data(phone_number))

url = 'https://mhealth.fams-cit.com/mhealth_house_keeping.php'
data = get_messages_data(phone_number)
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
response = requests.post(url, json=data, headers=headers)
if response.status_code == 200:
    print('response: ',response.text) 
else:
    print('Server error encountered ' + response.status_code)
                                                                                                                                                         


