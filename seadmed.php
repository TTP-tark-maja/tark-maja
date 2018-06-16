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
		 foreach (scandir('users/') as $dir){
			echo "<a href=users/$dir>$dir</a>" . "<br>";
		}
		if(isset($_POST['seadme_nimetus']) && isset($_POST['seadme_voimsus'])) {
			$dir = $_POST['seadme_nimetus'];
			$power = $_POST['seadme_voimsus'];
			$file_to_write1 = "logfile.txt";
			$file_to_write2 = "tingimused.txt";
			$file_to_write3 = "WorkingTimes.txt";
			$file_to_write4 = "TurnOffTimes.txt";
			$file_to_write5 = "todaydata.txt";
			$file_to_write6 = "seadme_info.txt";
			
			
			
			if( is_dir($dir) === false )
		{
			mkdir('users/'. $dir);
			$file1 = fopen('users/'.$dir. '/' .$file_to_write1, "w");
			$file2 = fopen('users/'.$dir. '/' .$file_to_write2, "w");
			$file3 = fopen('users/'.$dir. '/' .$file_to_write3, "w");
			$file4 = fopen('users/'.$dir. '/' .$file_to_write4, "w");
			$file5 = fopen('users/'.$dir. '/' .$file_to_write5, "w");
			$file6 = fopen('users/'.$dir. '/' .$file_to_write6, "w");
			fwrite($file1, "");
			fwrite($file2, "");
			fwrite($file3, "");
			fwrite($file4, "");
			fwrite($file5, "");
			fwrite($file6, "Seadme nimetus:". $dir ."\n Seadme võimsus:". $power);
			chmod('users/' . $dir. '/' .$file_to_write1, 0777);
			chmod('users/' . $dir . '/' . $file_to_write2, 0777);
			chmod('users/' . $dir, 0777);
			echo "<a href='$dir'>$dir</a>";
}
			
		}
		
			
		
				
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




