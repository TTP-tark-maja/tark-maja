# tark-maja
Arendasime projekti targa maja jaoks suvepraktika raames. Tarkvara eesmärk on tekitada inimestele võimalus oma elektriseadmete tarbimist paremini reguleerida. Kasutajal on võimalus valida oma elektriseadmetel teatud tingimused, näiteks mis kellaaegadel peab elektriseade kindlasti töötama, millise võimsuse juures lülitab seade end välja. Meie rakendus loob vastavalt kasutajate seatud tingimustele töögraafiku, millal seade töötab.

Kasutatud tehnoloogiad: Python3, PHP5, HTML5, CSS3, Javascript

Projekti panustasid: Simone Niinemägi, Robert Roos, Rando Mikksaar, Sten Markus Laht, Liisa Jakovleva, Meelis Karp, Jaagup Kippar.

1. Ühendada relee Raspberry Pi'ga ja elektriseadmega nagu pildil näidatud.
<p align="center">
  <img src="https://www.tlu.ee/~stenlaht/relee_1.png" width="250"/>
  <img src="https://www.tlu.ee/~stenlaht/relee_2.png" width="250"/>
  <img src="https://www.tlu.ee/~stenlaht/relee_3.png" width="250"/>
</p>

2. Installige käsurealt Raspberry Pi'le pythoni plotly  moodul. Selle jaoks on käsk "sudo pip3 install plotly".

3. Selleks, et tarbijaid kustutada, tuleb kasutajale anda selleks õigused. Selle jaoks tuleb käsureale kirjutada "sudo chown www-data /var/www/html/users"

4. Selleks, et anda kasutajale õigus tarbijat manuaalselt sisse ja välja lülitada tuleb käsureale kirjutada "usermod -G dialout www-data"

5. Selleks, et relee automaatselt tarbijat sisse ja välja lülitama hakkaks, tuleb kirjutada käsureale "crontab -e". Seejärel tuleb liikuda avanenud faili lõppu ja sinna kirjutada käsk "* * * * * python3.5 /home/pi/Desktop/tark-maja/Arvutaja.py" 
