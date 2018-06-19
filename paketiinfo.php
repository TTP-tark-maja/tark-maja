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
        </ul>
    </nav>

    <div class="banner">
        <img class="banner-image" src="4.JPG">
    </div><hr>
     
        <h1>Paketi informatsioon</h1>
        <br>
    <div class="container">   
        <form class="pakett"  action="pakett.php" method="GET">
		<script src="pakett.js"></script>
            <legend>Fikseeritud hind või fikseerimata hind?</legend>
			<br>
            <label class="radiobtn">Fikseeritud
                <input id="1" type="radio" name="price1" value="fikseeritud" onclick="textAll()">
                <span class="checkmark"></span>
            </label><br>
            <label class="radiobtn">Fikseerimata
                <input id="2" type="radio" name="price2" value="fikseerimata" onclick="textHide()">
                <span class="checkmark"></span><br>
            </label>
			<p id="text1" style="display:none">
            <legend>Päevahind (kW/h)</legend>
                <input type="number" name="amprice" value="paevahind"><br>
            <br></p>
			<p id="text2" style="display:none">
            <legend>Ööhind (kW/h)</legend>
                <input type="number" name="pmprice" value="oohind"><br>
            <br></p>
			<p id="text3" style="display:none">
            <legend>Kohaletoimetamisetasu</legend>
                <input type="number" name="deliveryprice" value="kohaletoimetamisetasu"><br>
            <br></p>
			<p id="text4" style="display:none">
            <legend>Müüja marginaal</legend>
                <input type="number" name="sellerprice" value="muujamarginaal"><br>
            <br>
            <div class="button">
                <input type="submit" name="submit" value="SALVESTA">
            </div>
        </form>
    </div>        
</body>
</html>