# Space Invaders
![Space Invaders](https://s3.envato.com/files/154016874/Screenshots/Pic1.jpg)


**Space Invaders** este unul din primele shooting games si misiunea este sa rezisti cat mai mult invaziei unor nave extraterestre
folosind un tun cu laser. In proiectarea acestui joc, *Nishikado*, creatorul sau, s-a inspirat din mai multe produse media cum ar
fi jocul arcade *Breakout*, romanul *Razboiul lumilor* sau franciza *Razboiul stelelor*.

## TODO 0 - In a galaxy far, far away - 0p

Asigurati-va ca scheletul exercitiului ruleaza optim:
  * Fereastra este **obligatoriu** sa porneasca pentru verificare.
  * Anuntati supraveghetorii pentru orice inconvenient.
  * Toate cerintele se corecteaza **manual**.

## TODO 1 - Din auzite - 1p
Cu totii stim ca sunetul nu se poate transmite prin vid. Insa nu si in lumea jocurilor, unde orice este posibil. Ca developeri,
aduceti sunetul la viata in spatiul cosmic al aplicatiei. Folositi fisierul `hit.wav` pentru pentru a marca in istorie momentul
cand o nava inamica este distrusa de raza laser. Trebuie sa ai in vedere:
  * Initializarea modulelor corespunzatoare.
  * Identificarea zonei de cod ce se ocupa cu aceasta logica.
  * Pornirea sunetului.

## TODO 2 - Un rau necesar - 1p
  Universul este plin cu diverse nave inamice. Una din ele este definita in clasa `Enemy_1`. Se remarca 3 metode semnificative
  pentru game-developement: **__init__** (constructorul obiectului), **update** (realizeaza logica obiectului la fiecare frame)
  si **draw** (deseneaza obiectul). Observati particularitatile ei de implementare.

  Totusi aceasta lume este cam plictisitoare. Cum ar fi sa ne facem un inamic care sa faca miscari mai interesante. Un inamic
  care sa se miste stanga dreapta pare adecvat. In clasa `Enemy_2` va trebui sa modificati urmatoarele:

  1. Constructorul - Este similar (identic) cu cel de la inamicul anterior doar ca mai primeste un parametru **range**, care
  este o pereche de coordonate pe *axa x* (stanga dreapta) intre care se poate misca nava.
  2. Update - stabiliti logica de miscare si de intoarcere. Pe *axa x* nava se va misca cu **1 unitate** per apel. Cand nava
  ajunge la una din coordonatele din **range** aceasta isi va schimba directia si va continua. Pe *axa y* se va comporta ca
  `Enemy_1`.

  Pentru **verificare** spawnati 4 nave la coordonate diferite care sa se plimbe in range-ul `(0, 800)`.

## TODO 3 - Entropie continua - 1p
  Clasa `Enemy_3` ascunde un inamic imprevizibil. Acesta este identic ca cel de la `TODO 2` insa miscarea lui este mai
  intamplatoare si depinde de timp. Intial, directia sa de deplasare (stanga - dreapta) este random.

  Ecuatia lui de miscare pe **axa y** (sus - jos) este definita de `y(t) = (t + r(10)) % 5`, unde **t** este timpul de
  la inceputul jocului iar **r(10)** este un numar intamplator intre 0 si 10.

  Pentru **verificare** spawnati 4 nave la coordonate diferite care sa se plimbe in range-ul `(0, 800)`.

## TODO 4 - Posibilitati infinite - BONUS - 1p

  Universul este plin de *...nimic...* . Dar lucrurile nu trebuie sa ramana asa. Atunci cand pe ecran nu mai exista inamici,
  spawnati la alegere 4 inamici noi (de tipul vostru preferat).
