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
            <label class="switch">
                <input type="checkbox">
                <span class="slider"></span>
            </label><br><br>
            <h2>seadme logi</h2>
                    <?php
                    $lines = file('logfile.txt');
                    $first5 = array_slice($lines, 0, 6);
                    echo implode("<p></p>", $first5);
                    
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
                <input type="submit" value="KUVA KOGU LOGI" name="kogulogi" id="1">
           </div> 
        </form>
    </div> 
</body>
</html>