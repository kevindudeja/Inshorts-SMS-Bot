# Inshorts-SMS-Bot
Creating a Inshorts SMS Bot to send News Headlines using Twilio SMS API - Easy
The un-intimidating guide to creating a SMS Bot using Python and NodeJS
 - I really haven't finished the NodeJS part but fingers-crossed! - DONE Hooray!
 
PART 1 - Creating a python script to send sms to my mobile
 - Used Twilio to send text messages using its web service APIs. This can be done by making a python script.
   - Experience with Python - Just read articles about what can be done with python and basic syntax
   - Experience with Git - n/a
   - Fun article to read - https://hackernoon.com/the-programmers-guide-to-booking-a-plane-11e37d610045#.ixuetm3pf
   - "Know the possibilities of a language" - ketan
   - Read up on API's and Modules
     - https://docs.python.org/2/tutorial/modules.html 
 - Created a free account on twilio to register my mobile
 - Install the twilio module using pip
   - pip is used to install python packages
   - sudo pip install twilio
 - In your python script import twilio module
 - Follow the code here - https://www.twilio.com/docs/api/rest/sending-messages
 - Set up an outgoing number in your dashboard - https://www.twilio.com/console/sms/getting-started/basics
 - run the python script in the terminal
   - python sendsms.py
 
 OUTPUT: Recieved 1 Message from 51465
 " Sent from your Twilio trial account - Hello World "
 
 How other people are doing this
  - https://github.com/ksdme/py-textbelt
  - http://textbelt.com/
  But the above didn't work for me. Just sharing.

PART 2 - Getting data from Inshorts npm package
 - Follow this playlist to learn how to use API's and creating a BOT - https://www.youtube.com/watch?v=s70-Vsud9Vk&list=PLRqwX-V7Uu6atTSxoRiVnSuOn6JHnq2yV
 - Install npm for installing NodeJS packages
   - sudo apt - get install npm
 - Install NodeJS
   - sudo apt - get install nodejs
 - Inshort Package Documentation - https://www.npmjs.com/package/inshorts
 - Create a directory say inshorts
 - Create a JSON file in that dir using 'npm init' command
 - install the inshorts package in that dir
   - npm install inshorts --save
   - Above command will download the packages in that directory
 - Create a js file say inshorts.js
   - console.log("Bot is working");
 - run this file in terminal
   - node inshorts.js
   - OUTPUT: Bot is working
 - Call the library package in your inshorts.js file
   - var inshorts= require('inshorts').init();
 - Run the file again in terminal to check if no error.
 - Use the getNews method to get news from the api
 - If you want just headlines, then edit the code as 
		function(err,result){
 		var headlines = result.headline;
		 for(var i=0; i< headlines.length;i++){
 		console.log(headlines[i]);
 		}
 		//if(!err)
 		//	console.log(result);
 		//else
 		//	console.log(err);
		}
