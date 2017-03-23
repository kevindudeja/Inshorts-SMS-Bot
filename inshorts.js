console.log("Bot is Initialising...");

var inshorts = require('inshorts').init();
//var schedule = require('node-schedule');

//var j = schedule.scheduleJob('*/1 * * * *', get());

get();

function get(){
	console.log("Bot is working");

	var category = ' ';
	
	var fs = require("fs");
	fs.open('out3.txt', 'w+' , function(err,fd){
		if(err){
			return console.error(err);
		}
	});

	inshorts.getNews(category,gotData);

	//inshorts.more({category:'startup',id:'jo8dm6fs-1'},error);
	function gotData(err,result){
		var headlines = result.headline;
		for(var i=0; i< headlines.length;i++){
			//console.log(headlines[i]);
			fs.appendFile('out3.txt', headlines[i]+'\r\n' , function(err){
				if(err)
					return console.error(err);
			} )
		}
		//if(!err)
		//	console.log(result);
		//else
		//	console.log(err);
	};
}
