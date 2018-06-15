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
    
    <h1>seadmed</h1>
        <br>  
    <div class="main-grid">
        <div class="header-uks">
          <h2>Seadmed</h2>
		  <?php
		if(isset($_POST['seadme_nimetus']) && isset($_POST['seadme_voimsus'])) {
			$data = $_POST['seadme_nimetus'] . ' - ' . $_POST['seadme_voimsus'] ."W"."\n";
			$ret = file_put_contents('seadmed.txt', $data, FILE_APPEND | LOCK_EX);
		}

		$myfile = fopen("seadmed.txt", "r") or die("ei saa avada faili!");
				while(!feof($myfile)) {
				echo fgets($myfile) . "<br>";
				}
				fclose($myfile);
				
		// change the name below for the folder you want
		$dir = "new_folder_name";

		$file_to_write = 'test.txt';
		$content_to_write = "The content";

		if( is_dir($dir) === false )
		{
			mkdir($dir);
		}

		$file = fopen($dir . '/' . $file_to_write,"w");

		// a different way to write content into
		// fwrite($file,"Hello World.");

		fwrite($file, $content_to_write);

		// closes the file
		fclose($file);

		// this will show the created file from the created folder on screen
		include $dir . '/' . $file_to_write;
		?>
        </div>

        <div class="loetelu">

        <br>
            
        </div>
	<form method="POST">
        <div class="header-kaks">
            <h2>Lisa seade</h2>
        </div>

        <div class="lisamine">
		
            <legend>Nimetus</legend>
                <input type="text" name="seadme_nimetus"><br>
            <br>
            <legend>Võimsus (W)</legend>
                <input type="text" name="seadme_voimsus"><br>
			<br>
            <div class="submit">
                <input type="submit" value="SALVESTA">
            </div>
        </div>
    </div>
    </form>
</body>
</html>



