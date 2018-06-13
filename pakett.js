function textAll() {

	var radio = document.getElementById("1");
	var text1 = document.getElementById("text1");
	var text2 = document.getElementById("text2");
	var text3 = document.getElementById("text3");
	var text4 = document.getElementById("text4");
	
	if (radio.checked == true){
	text1.style.display = "block";
	text2.style.display = "block";
	text3.style.display = "block";
	text4.style.display = "block";
	} 
}

function textHide(){
	
	var radio = document.getElementById("2");
	var text1 = document.getElementById("text1");
	var text2 = document.getElementById("text2");
	var text3 = document.getElementById("text3");
	var text4 = document.getElementById("text4");
	
	if (radio.checked == true){
	text1.style.display = "none";
	text2.style.display = "none";
	text3.style.display = "block";
	text4.style.display = "block";
	}
}