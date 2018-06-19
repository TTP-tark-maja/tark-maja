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
            <li><a href="../../koduleht.php">Avaleht</a></li>
            <li><a href="../../paketiinfo.php">Paketi informatsioon</a></li>
        </ul>
    </nav>
    
    <div class="banner">
        <img class="banner-image" src="4.JPG">
     </div><hr>

     <h1>Tarbija</h1>


    <div class="container">
            <div class="button">
                <a href="tingimused.php"><input type="button" value="Seadme tingimused"></a>
            </div>
        <h2>seadme olek</h2>
            <label class="switch">
                <input type="checkbox">
                <span class="slider"></span>
            </label><br>
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
                ?> 
        <form method="POST">
		   <div class="submit">
			   <br>
				<input type="submit" value="kuva kogu logi" name="kogulogi" id="1"><br>
			   </div> 
			   <div class="delete">
			   <br><br>
				<input type="submit" value="kustuta" name="kustuta" ><br>
           </div> 
        </form>
    
    </div>
    
</body>
</html>



