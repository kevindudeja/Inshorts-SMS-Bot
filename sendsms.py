import twilio
import schedule
import time
from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC395e6e1f866844d26250ae25264d9c58" 
AUTH_TOKEN = "Your_secret_auth_token" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
def send(t):
	fo = open("filename.txt","r")
	with fo as f:
		content = f.readlines()

	for i in content:
		headline = i #content[0]
		client.messages.create(
			to = "Your_number_with_country_code", 
			from_="Your_twilio_outgoing_number", 
			body = headline, 
		)
	#open the file and clear it for the next day of headlines
	fs = open("filename.txt","w")
	fs.write("")
	fs.close()
return

print "Bot is running"

#schedule.every().day.at("08:15").do(send,'')
schedule.every().day.at("10:30").do(send,' ') #schedule the function to run at 10:30AM

while True:
	schedule.run_pending()
	time.sleep(5)
