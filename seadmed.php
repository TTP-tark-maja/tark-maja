<!DOCTYPE html>
<html lang="et">
<head>
    <meta charset="utf-8">
    <title>Tark Maja</title>
    <link rel="icon" type="image/png" href="M.png">
    <link rel="stylesheet" type="text/css" href="design/style.css">
</head>
<body class="page_bg">
    <nav>
        <ul>
            <li><a href="koduleht.php">Avaleht</a></li>
            <li><a href="paketiinfo.html">Paketi informatsioon</a></li>
        </ul>
    </nav>

    <div class="banner">
        <img class="banner-image" src="4.JPG">
     </div><hr>

     <h1>Tarbija</h1>


    <div class="container">
            <div class="button">
                <input type="button" value="Seadme tingimused">
            </div>
        <h2>seadme olek</h2>
		<form method="POST">
            <div class="button">
				<input type="submit" value= "Lülita sisse" name="test1" ><br>
				<input type="submit" value= "Lülita välja" name = "test">

                <span class="slider"></span>
            </div><br>
		</form>
            <h2>seadme logi</h2>
                    <?php
                    $lines = file('logfile.txt');
                    $first5 = array_slice($lines, 0, 5);
                    echo implode("<ul></ul>", $first5);
                    
                    if(isset($_POST['kogulogi']))
                    {
                            $content = file('logfile.txt');
                            foreach ($content as $line){ 
                                echo ('<ul>' . $line . '</ul>');
                            }
                    }
					if (isset($_POST['test1'])){
						$dir = basename(dirname(__FILE__));
						shell_exec("sh /home/pi/Desktop/tark-maja/relee_sisselylitus.sh");
						shell_exec("python3.5 /home/pi/Desktop/tark-maja/users/$dir/manual_logwrite.py");
					}
					if (isset($_POST['test'])){
						$dir = basename(dirname(__FILE__));
						shell_exec("sh /home/pi/Desktop/tark-maja/relee_valjalylitus.sh");
						shell_exec("python3.5 /home/pi/Desktop/tark-maja/users/$dir/manual_logwrite.py");
						
					}
					
					
                ?> 
        <form method="POST">
		   <div class="submit">
           <br>
            <input type="submit" value="kuva kogu logi" name="kogulogi" id="1"><br>
           </div> 
           <div class="delete">
           <br><br>
            <input type="button" value="kustuta" name="kustuta" ><br>
           </div> 
        </form>
    
    </div>
    
</body>
</html>



