import twilio
import schedule
import time
from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC395e6e1f866844d26250ae25264d9c58" 
AUTH_TOKEN = "Your_secret_auth_token" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

def sendsms(t):
	fo = open("out.txt","r")
	with fo as f:
		content = f.readlines()
		for i in content:
			headline = content[0]
			client.messages.create(
				to = "Your_number_with_country_code", 
				from_="Your_twilio_outgoing_number", 
				body = headline,
			)
	return
	
print "Bot is running"

#schedule.every().day.at("08:15").do(send,'')
schedule.every().day.at("04:46").do(sendsms,' ')

while True:
	schedule.run_pending()
	time.sleep(5)

