<?php
if(isset($_GET["submit"])){
	$myFile = fopen("clientData.txt", "w");
	$txt1 = $_GET["amprice"]."\n";
	$txt2 = $_GET["pmprice"]."\n";
	$txt3 = $_GET["deliveryprice"]."\n";
	$txt4 = $_GET["sellerprice"]."\n";
	
	if(isset($_GET["price1"])){		
	
		if(empty($_GET["amprice"])){
			$txt1 = "0 \n";
		}
		if(empty($_GET["pmprice"])){
			$txt2 = "0 \n";
		}
		if(empty($_GET["deliveryprice"])){
			$txt3 = "0 \n";
		}
		if (empty($_GET["sellerprice"])){
			$txt4 = "0 \n";
		}
		
		fwrite($myFile, "Fikseeritud \n");
		fwrite($myFile, $txt1);
		fwrite($myFile, $txt2);
		fwrite($myFile, $txt3);
		fwrite($myFile, $txt4);
	
		header("Location: paketiinfo.html");
		
	} else {
		
		if(empty($_GET["deliveryprice"])){
			$txt3 = "0 \n";
		}
		if (empty($_GET["sellerprice"])){
			$txt4 = "0 \n";
		}
		
		fwrite($myFile, "Fikseerimata \n");
		fwrite($myFile, $txt3);
		fwrite($myFile, $txt4);
	
		header("Location: paketiinfo.html");
	}
}
?>