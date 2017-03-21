import twilio
from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC395e6e1f866844d26250ae25264d9c58" 
AUTH_TOKEN = "Your_secret_auth_token" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
    to = "Your_number_with_country_code", 
    from_="Your_twilio_outgoing_number", 
    body ="Your_message", 
)
