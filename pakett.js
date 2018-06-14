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

function addItem(){
	
    var ul = document.getElementById("dynamic-list");
    var candidate = document.getElementById("candidate");
    var li = document.createElement('li');
    li.setAttribute('id',candidate.value);
    li.appendChild(document.createTextNode(candidate.value));
    ul.appendChild(li);
	
}

function removeItem(){
	
	var ul = document.getElementById("dynamic-list");
    var candidate = document.getElementById("candidate");
    var item = document.getElementById(candidate.value);
    ul.removeChild(item);
}

function post(ans) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
    }
  };
  xhttp.open("GET", "/result.php?answer="+ans, true);
  xhttp.send();
}