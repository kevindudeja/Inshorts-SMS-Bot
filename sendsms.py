import twilio
import schedule
import time
from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC395e6e1f866844d26250ae25264d9c58" 
AUTH_TOKEN = "6e124f1874d28954bbb2c47425acb37b" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
def send(t):
	fo = open("out3.txt","r")
	with fo as f:
		content = f.readlines()

	for i in content:
		headline = i #content[0]
		client.messages.create(
			to = "+919790712004", 
			from_="+13052406750", 
			body = headline, 
		)
	
	fs = open("out3.txt","w")
	fs.write("")
	fs.close()
	
	return

print "Bot is running"

#schedule.every().day.at("08:15").do(send,'')
schedule.every().day.at("10:30").do(send,' ')

while True:
	schedule.run_pending()
	time.sleep(5)




