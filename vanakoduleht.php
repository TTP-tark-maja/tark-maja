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
            <li><a href="seadmed.php">Seadmed</a></li>
            <li><a href="tingimused.html">Seadme tingimused</a></li>
        </ul>
    </nav>
    <div class="banner">
        <img class="banner-image" src="4.png">
    </div><hr>

    <h1>Seadmed</h1>
        <br>
        <div class="main-grid">
            <div class="header-uks">
                <h2>Seadmed</h2>
            </div>

        <div class="loetelu">
            <div class="seade">
                <a href="hetkeseis.html">RÖSTER</a>
            </div>
        <br> 
        </div>

        <div class="header-kaks">
            <h2>Lisa seade</h2>
        </div>

        <div class="lisamine">
            <ol id="dynamic-list"></ol><br>
            <legend>Nimetus</legend>
                <input type="text" id="candidate"><br>
            <br>
            <legend>Võimsus (W)</legend>
                <input type="text" id="candidate"><br>

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
        </div>
    </div>
</body>
</html>
