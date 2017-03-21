# Inshorts-SMS-Bot
Creating a Inshorts SMS Bot to send News Headlines using Twilio SMS API - Easy

The un-intimidating guide to creating a SMS Bot using Python and NodeJS
 - I really haven't finished the NodeJS part but fingers-crossed! - DONE Hooray!
 
PART 1 - Creating a python script to send sms to my mobile

API - Twilio
 - Used Twilio to send text messages using its web service APIs.
   - Twilio is free for 1 registered user 
   - Experience with Python - Just read articles about what can be done with python and basic syntax
   - Experience with Git - gittergoo.. gittergoo..
   - Fun article to read - https://hackernoon.com/the-programmers-guide-to-booking-a-plane-11e37d610045#.ixuetm3pf
   - Read up on API's and Modules
     - https://docs.python.org/2/tutorial/modules.html 
 - Created a free account on twilio to register my mobile for the service
 
Packages
- pip is used to install python packages
     - sudo apt - get install pip
     
Modules
 - Install the twilio module for python using pip
   - sudo pip install twilio
   
Steps
 - Create a new python file say sendsms.py and in your python script import the twilio module
   - import twilio
 - Follow the rest of the code here in the twilio api documentation - https://www.twilio.com/docs/api/rest/sending-messages
 - The documentation says an outgoing number needs to be set up, which is passed as an argument in the function calls of the api
 - Hence, set up an outgoing number in your twilio dashboard - https://www.twilio.com/console/sms/getting-started/basics
 - run the python script in the terminal
   - python sendsms.py
 
 OUTPUT: Recieved 1 Message from 51465
 " Sent from your Twilio trial account - Hello World "
 
PART 2 - Getting data from Inshorts npm package

Reference
 - Follow this playlist to learn how to use API's and creating a BOT - https://www.youtube.com/watch?v=s70-Vsud9Vk&list=PLRqwX-V7Uu6atTSxoRiVnSuOn6JHnq2yV
 
Packages Required
 - Install npm for installing NodeJS packages
   - sudo apt - get install npm
 - Install NodeJS
   - sudo apt - get install nodejs
   
Documentation
 - Inshort Package Documentation - https://www.npmjs.com/package/inshorts
 
Steps
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
   - Create a var headlines = result.headline; in the function(err,result) block//here headlines is a object consisting of all the headlines
   - Run a for loop from i = 0 to headlines.length and print using console.log(headlines[i]);
   - Comment out the if and else block
  - run the file again in terminal
