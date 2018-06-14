<!DOCTYPE html>
<html lang="et">
<head>
    <meta charset="utf-8">
    <title>Tark Maja</title>
    <link rel="stylesheet" type="text/css" href="design/style.css">
</head>
<body>
    <nav>
        <ul>
            <li><a href="koduleht.php">Home</a></li>
            <li><a href="paketiinfo.html">Paketi informatsioon</a></li>
            <li><a href="tingimused.html">Seadme tingimused</a></li>
			<li><a href="seadmed.php">Seadmed</a></li>
        </ul>
    </nav>
        <h1>Seadmed</h1>
		
    <div class="container">     
        <form>
			<ol id="dynamic-list"></ol><br>
			<input type="text" id="candidate"/>
				<div class="button">
				<script src="pakett.js"></script><br>
					<input onclick="addItem();" type="button" value="LISA" name="answer" id="answer">
					<input onclick="removeItem()" type="button" value="EEMALDA">
					<?php
					$fname = "answer.txt";
					$result = isset($_GET['answer']);
					$prev = file_get_contents($fname);
					$result = $result.",".$prev;
					file_put_contents($fname,$result);
					?>
				</div> 
        </form>
    </div>        
</body>
</html>