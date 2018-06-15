<!DOCTYPE html>
<html lang="et">
<head>
    <meta charset="utf-8">
    <title>Tark Maja</title>
    <link rel="stylesheet" type="text/css" href="design/style.css">
</head>
<body class="page_bg">
    <nav>
        <ul>
            <li><a href="koduleht.php">Home</a></li>
            <li><a href="paketiinfo.html">Paketi informatsioon</a></li>
            <li><a href="tingimused.html">Seadme tingimused</a></li>
			<li><a href="seadmed.php">Seadmed</a></li>
        </ul>
    </nav>
    <div class="banner">
        <img class="banner-image" src="4.png">
    </div><hr>

    <h1>Seadme logi</h1>

	<div class="container">  
		<?php
		$myfile = fopen("logfile.txt", "r") or die("ei saa avada faili!");
		while(!feof($myfile)) {
		echo fgets($myfile) . "<br>";
		}
		fclose($myfile);
		?> 
        <form>
        </form>
    </div>        
</body>
</html>
