# Inshorts-SMS-Bot
Creating a Inshorts SMS Bot to send News Headlines using Twilio SMS API - Easy

Installing Ubuntu terminal for windows users
 - https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/

PART 1 - Creating a python script to send sms to my mobile

API
 - Used Twilio API for python to send text messages using its web service APIs.
   - Twilio is free for 1 registered user 
   - Experience with Python - Just read articles about what can be done with python and basic syntax
   - Experience with Git - gittergoo.. gittergoo..
   - Fun article to read - https://hackernoon.com/the-programmers-guide-to-booking-a-plane-11e37d610045#.ixuetm3pf
   - Read up on API's and Modules
     - https://docs.python.org/2/tutorial/modules.html 
     
 - Create a free account on twilio to register your mobile for the service
 
Packages
- pip is used to install python packages
  ```
  sudo apt - get install pip
  ```  
Modules
 - Install the twilio module for python using pip
   ```
   sudo pip install twilio
   ```
Steps
 - The documentation says an outgoing number needs to be set up, which is passed as an argument in the function calls of the api
 - Hence, set up an outgoing number in your twilio dashboard - https://www.twilio.com/console/sms/getting-started/basics
 - Edit the sendsms.py script with your phone number, OAuth code etc...
 - run the python script in the terminal
   - python sendsmstest.py
 
 OUTPUT: Recieved 1 Message from 51465
 " Sent from your Twilio trial account - Hello World "
 
PART 2 - Getting data using Inshorts npm package and saving it in a text file

Packages Required
 - Install npm for installing NodeJS packages
   ```
   sudo apt - get install npm
   ```
 - Install NodeJS
   ```
   sudo apt - get install nodejs
   ```
   
Modules
 - Install inshorts package
   ```
   sudo npm install inshorts --save
   ```
 - Install node-schedule package
   ```
   sudo npm install node-schedule --save
   ```
   
Documentation and ref
 - Follow this playlist to learn how to use API's, JSON file, NPM and creating a BOT - https://www.youtube.com/watch?v=s70-Vsud9Vk&list=PLRqwX-V7Uu6atTSxoRiVnSuOn6JHnq2yV
 - Inshort Package Documentation - https://www.npmjs.com/package/inshorts
 - https://www.npmjs.com/package/node-schedule
 - http://stackoverflow.com/questions/15088037/python-script-to-do-something-at-the-same-time-every-day
 - http://stackoverflow.com/questions/26306090/running-a-function-everyday-midnight
 
Steps
 - Creating your own JSON file for your project
   ```
   npm init
   ```
 - --save will add the packages installed to your JSON dependencies
 - Run the inshortstest.js
   ```
   node inshortstest.js
   ```
 - If you want just the headlines then comment the if else block and umcomment the lower block of code
 - By executing the inshorts.js, an 'out.txt' file will be created with the news headlines
  
File handling in Node.js
 - https://www.tutorialspoint.com/nodejs/nodejs_file_system.htm

PART 3 - Reading the text file created line-by-line and sending the headlines from the sendsms script
  - By executing the sendsms2.py will send the first headline in the textfile to your mobile
  - By executing the sendsms3.py you can shedule when the SMS is sent
    ```
    schedule.every().day.at("08:00").do(sendsms,' ') #will send SMS at 8:00AM
    ```
