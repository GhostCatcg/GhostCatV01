$(function(){

	var note = $('#note'),
		ts = new Date("2019-04-13").getTime(),
        exam = true;

	if((new Date()) > ts){
	    // 如何现在时间大于设定时间，则根据下面的进行设定倒计时
		// The new year is here! Count towards something else.
		// Notice the *1000 at the end - time must be in milliseconds
		ts = (new Date("2019-10-13")).getTime();
		newYear = false;
	}
		
	$('#countdown').countdown({
		timestamp	: ts,
		callback	: function(days, hours, minutes, seconds){


		    if (days > 100 && $("#countdown .countDays > span").length < 3){
                let $one = '<span class="position"><span class="digit static" style="top:0;opacity: 1;">1</span></span>';
                $("#countdown .countDays > span:first-child").before($one).css("margin-left","8px");
            }
			var message = "";

			message += days + " day" + ( days==1 ? '':'s' ) + ", ";
			message += hours + " hour" + ( hours==1 ? '':'s' ) + ", ";
			message += minutes + " minute" + ( minutes==1 ? '':'s' ) + " and ";
			message += seconds + " second" + ( seconds==1 ? '':'s' ) + "</br>";
			
			if(exam){
				message += "left until the English exam!";
			}
			else {
				message += "left to 10 days from now!";
			}
			
			note.html(message);
			// console.log(message)
		}
	});
	
});
