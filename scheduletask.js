var schedule = require('node-schedule');

console.log("Bot is running");

var j = schedule.scheduleJob('*/1 * * * *', function(){
	//runs every 1 minute
	console.log('The answer to life, the universe, and everything!');
});