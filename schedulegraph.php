<!DOCTYPE html>
<html lang="et">
<style>
*{
	margin:0;
	padding:0;
}
body {
	display: block;
}
.ontimes {
	text-align: left;
}
.offtimes {
	text-align: center;
}
.times {
	display: inline-flex;
	margin-right:631px;
}
.block {
	display: block;
}
#test{
	text-align: center;
}
#test2{
	float: left;
}
</style>
<head>
	<meta charset = "UTF-8"><meta/>
	<title>Töögraafik</title>
</html>
</head>
<body>

<h1 id= "test2">Sisselülitusajad</h1>
<h1 id= "test">Väljalülitusajad</h1>
<div class="block">
	<div class= "times" style="clear: both;">
	</div>

	<div class = "times" style="clear: both;">
</div>
<div class="block">
	<?php
	$myFile = fopen("WorkingTimes.txt", "r");
	echo '<div class ="times">';
	while(! feof($myFile)){
		echo fgets($myFile)."<br />";
	}
	echo'</div>';
	$myFile2 = fopen("TurnOffTimes.txt","r");
	echo '<div class = "times">';
	while(! feof($myFile2)){
		echo fgets($myFile2)."<br />";
	}
	echo '</div>';

	?>
</div>
</body>
</html>
