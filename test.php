<!DOCTYPE html>
<html lang="et">
<head>
<script>
</script>
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
        </ul>
    </nav>
        <h1>Seadme logi</h1>
		<?php
		$myfile = fopen("logfile.txt", "r") or die("Unable to open file!");
		while(!feof($myfile)) {
		echo fgets($myfile) . "<br>";
		}
		fclose($myfile);
		if(isset($_POST['test'])) {
			echo shell_exec('sh /desktop/praktika/relee_käivitus.sh');
		}
		?>
    <div>   
		<form method = "post">
			<input type="submit" name="test" value="lülita sisse" onclick= "myAjax()" href="">
        </form>
    </div>        
</body>
</html>
