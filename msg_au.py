from twilio.rest import Client 
import random
from configparser import ConfigParser

file = "config.ini"
config = ConfigParser()
config.read(file)
params = dict(config['params'])

client = Client(params["account_sid"],params["auth_token"]) 

messages = []
p = open("texte.txt", "r")
messages = list(p)
msg = random.choice(messages)
message = client.messages.create( 
                              from_='whatsapp:+14155238886',#14155238886  
                              body= msg,      
                              to='whatsapp:+33xxxxxxx'# 
                          ) 
 
print(message.sid)