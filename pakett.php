<?php
$myFile = fopen("clientData.txt", "a");
$txt1 = "Hommikune hind:".$_GET["amprice"]."\n";
$txt2 = "Õhtune hind:".$_GET["pmprice"]."\n";
$txt3 = "Kohaletommistasu:".$_GET["deliveryprice"]."\n";
$txt4 = "Müüjamarginaal:".$_GET["sellerprice"]."\n";
if(empty($_GET["amprice"])){
	$txt1 = "Hommikune hind: 0 \n";
}
if(empty($_GET["pmprice"])){
	$txt2 = "Õhtune hind: 0 \n";
}
if(empty($_GET["deliveryprice"])){
	$txt3 = "Kohaletoimetamistasu: 0 \n";
}
if (empty($_GET["sellerprice"])){
	$txt4 = "Müüjamarginaal: 0 \n";
}
fwrite($myFile, $txt1);
fwrite($myFile, $txt2);
fwrite($myFile, $txt3);
fwrite($myFile, $txt4);
