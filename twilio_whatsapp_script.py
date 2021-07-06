from twilio.rest import Client

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
TWILIO_ACCOUNT_SID = 'AC2a4fe5daa22009a0d95c5d730a954c5d'
AUTH_TOKEN = '14c6cb9310b352c454c294a883040a7a'
client = Client(TWILIO_ACCOUNT_SID, AUTH_TOKEN)

# Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'

# Test Numbers
#to_whatsapp_number='whatsapp:+256757163101'
#to_whatsapp_number='whatsapp:+256751964081'
#to_whatsapp_number='whatsapp:+256753586752'

contact_dict = {"Essy" : "+917042020895"}
phone_number = 'whatsapp:+917042020895'
single_number = 'whatsapp:+256751964081'
test_message = 'Hey there!'

# Sending messages to a contacts in the contact_dict
for key, value in contact_dict.items():
    msg_whats_ = client.messages.create(body='Hey {}!'.format(key),
                       from_=from_whatsapp_number,
                       to='whatsapp:' + value)

# Sending message to single number
def send_message(number, body):
    msg_whats_ = client.messages.create(body=body,
                       from_=from_whatsapp_number,
                       to=number)  
    
send_message(single_number, test_message)

# Qeurying messages details of a given number
def get_messaging_info(number):
    for single_message in client.messages.list():
        if(single_message.to == number):
            print("Message Details")
            print("===============")
            print("Body: " + single_message.body)
            print("Sent to: " + single_message.to)
            print(single_message.date_sent)
            print("Price: " + single_message.price)
            print("Status: " + single_message.status)
            print("===============")

get_messaging_info(phone_number)


                                                                                                                                                              