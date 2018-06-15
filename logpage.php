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
	<div class="container">  
        <h1>Seadme logi</h1>
		<?php
		$lines = file('logfile.txt');
		$first5 = array_slice($lines, 0, 6);
		echo implode("</li><li>", $first5);
		
		if(isset($_POST['kogulogi']))
		{
			$content = file('logfile.txt');
			foreach ($content as $line){ 
				echo ('<li>' . $line . '</li>');
			}
		}
		?> 
        <form method="POST">
		   <div class="submit">
		   <br>
                <input type="submit" value="KUVA KOGU LOGI" name="kogulogi">
           </div> 
        </form>
    </div>        
</body>
</html>
