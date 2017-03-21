import twilio
from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC395e6e1f866844d26250ae25264d9c58" 
AUTH_TOKEN = "6e124f1874d28954bbb2c47425acb37b" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
    to="+919790712004", 
    from_="+13052406750", 
    body="Abhinav!!!!", 
)
