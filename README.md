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
 - By running the file you will get output like
{"body":
        ["India's middle and long distance coach Nikolai Snesarev was detained for half a day by Rio police and later released after a lady doctor at the Games Village filed a complaint of misbehaviour. Snesarev, who trains the likes of Lalita Babar, Sudha Singh and OP Jaisha, was later let off reportedly after the intervention of the Indian Embassy in Brazil.",
        "The Mexican pair of Karem Achach and Nuria Diosdado performed to an Indian beat in the synchronised swimming event at the Rio Olympics on Monday. They performed to the Bollywood song ‘Aila re Aila’ from the film ‘Khatta Meetha’, that starred actor Akshay Kumar. The pair was in the ninth spot, having qualified for the final of the event.",
        "Himachal Pradesh CM Virbhadra Singh on Monday announced that state government employees and pensioners will get an additional 6% Dearness Allowance with effect from January 1, 2016. Speaking at a state-level function on the Independence Day, he added that the additional DA would be paid from October 2016 onwards and will cost ₹330 crore more to the state exchequer annually.",
        "The leader of the Lebanon-based terror network Hezbollah Hassan Nasrallah has said US Presidential nominee Donald Trump was right to say that the US President Barack Obama has founded ISIS. Nasrallah said what the American presidential candidate says \"is  based on facts and documents\". Notably, Nasrallah blames the US for the rise of Islamic extremists in the Middle East. "],
"image":
        ["http://images.newsinshorts.com.edgesuite.net/app_assets/images/2016/8aug/15/3dcee6a8-6b1b-4ddc-a673-e2d6329b20c5-1-14712874674300.jpg?resize=400px:*",
        "http://images.newsinshorts.com.edgesuite.net/app_assets/images/2016/8aug/15/e984176e-477d-4b08-9def-0dfd6b8dea23-1-14712870099380.jpg?resize=400px:*",
        "http://images.newsinshorts.com.edgesuite.net/app_assets/images/2016/8aug/15/a798aa47-7875-4e1f-aaa0-da5e5f934b98-1-14712860532710.jpg?resize=400px:*",
        "http://images.newsinshorts.com.edgesuite.net/app_assets/images/2016/8aug/15/7f668916-9c76-4284-83e3-80733f332c11-1-14712860131540.jpg?resize=400px:*"],
"headline":
        ["India's long distance coach detained for assault",
        "Mexican pair perform on B'wood beat in swimming event",
        "6% hike in DA for HP govt employees, pensioners",
        "Trump is right Obama founded ISIS: Hezbollah leader  "],
"id":"865296bf-759b-4ebd-acdb-2fc68d3ccbcb-1",
"category":"startup"
}
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
  - OUTPUT: 
India's long distance coach detained for assault
Mexican pair perform on B'wood beat in swimming event
6% hike in DA for HP govt employees, pensioners
Trump is right Obama founded ISIS: Hezbollah leader
