console.log("Bot is working");

var inshorts = require('inshorts').init();

var category = ' ';
/*
	//leave blank to get All News
    national //Indian News
    business
    sports
    world
    politics
    technology
    startup
    entertainment
    miscellaneous
    hatke // out of the way
    science
    automobile
*/

inshorts.getNews(category,gotData);
//inshorts.more({category:'startup',id:'jo8dm6fs-1'},error); //get more 25 headlines
function gotData(err,result){
	if(!err)
		console.log(result);
	else
		console.log(err);
	/*
	var headlines = result.headline;
	for(var i=0; i< headlines.length;i++){
		//console.log(headlines[i]);
	}
	*/
};