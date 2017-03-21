console.log("Bot is working");

var inshorts = require('inshorts').init();

var category = ' ';

inshorts.getNews(category,gotData);
//inshorts.more({category:'startup',id:'jo8dm6fs-1'},error);
function gotData(err,result){
	var headlines = result.headline;
	for(var i=0; i< headlines.length;i++){
		console.log(headlines[i]);
		
	}
	//if(!err)
	//	console.log(result);
	//else
	//	console.log(err);
};