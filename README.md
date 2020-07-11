# PongAI
Pong+simple_neutral_network


 English description below
 
 readme.txt is better 
 
 ==============================================
 
 GUI jeszcze nie gotowe więc aby uruchomić gre gracz vs gracz należy uruchomić plik Window
 (przez to na razie nie da się zmieniać konfiguracji innaczej niż z poziomu kodu ) 
 
 Gracz vs Gracz sterowanie 
 
  gracz 1:
  "w" w góre
  "s" w du 
  
  gracz 2:
  
  "i" w góre
  "k" w du 
 
 
 
aby uruchomić ai vs ai nalezy uruchomić plik WindowAI

gra jest puszczona w maksymalnym tempie 
dostepne "sterowanie" 
"p" spowalnia gre dzięki czemu można zobaczyć co się dzieje
"o" z powrotem przyspiesza gre 

"L" gra przełacza się w tryp gracz vs AI 
  gracz przejmuje konrole nad gracz 1 :
  "w" w góre
  "s" w du 
  
  aby AI naczyło sie grać należy uruchomić gre i zostawić na kilka minut na najwyższym tempie (czas zależy od posiadanego sprzetu oraz szcześcia gdyż sieć neuronowa uczy się   niedetermistycznie )
  
  można co jakiś czas kliknoć "p" i zobaczyć czy już umie w miare odbijać piłeczke.
  
  Pózniej mam zamiar dodać kilka zapisanych sieci które już umieją grać aby można było od razu zagrać przeciwko t
  
  
  sieć posiada 4 warstwy
  każda warstwa posiada 7 neuronów 
  sieć jest jednokierunkowa 
  połoczenie miedzy warstwami każdy z każdym
  
  Warstwa \\ Wewnetrzna(1)\\ Wewnetczna(2) //  Wyjścia
  Wejścia \\ Wewnetrzna(1)\\ Wewnetrzna(2) //  Wyjście
  
  W pongu wykorzystuje tylko 6 neuronów wejściowych ( jeden jest zawsze =0) 
  oraz jedynie 2 neurony wyjścia e_1,e_2 (zasada jest prosta jeśli e_1>e_2 to sieć idzie w góre a jeśli e_1<e_2 to idzie w du ) 
  
  Nauka polega na graniu sieć vs sieć 
  Wpierw jest tworzone X sięci (domyślnie 10) 
  nastepnie każda sieć rozgrywa 2 macze przeciw innym siecią 
  graja z limitem czasowym ( GUI nie gotowe wiec można zobaczyć ten limit tylko z poziomu codu ) 
  po skończonym czasie każda sieć dostaje "ocene" (oceny sumuja sie w ramach 1 generacji ) 
  
  po rozegraniu wszystkich meczy w "generacji"
  kilka najlepszych sieci "przeżywa " i na ich podstawie są tworzone sieci do nastepnej generacji
  
  z każda nastepna generacja zmiany są coraz mniejsze tzn. miedzy 1-2 generacja wartość z każdej krawedzi może zmieić się nawet o 0.3 a już w 10 generacji o ok 0.15
  
  całośc powtarza się (jak na razie non-stop aż użytkownik wyłaczy program lub klinknie "L") 
  
  oczywiście do Ponga można napisać AI w znacznie prostrzy sposób (prosty warunek if ball.pos_y<paddle_pos_y to w góre (: ,czy nawet dokładnie obliczyć miejsce przelotu piłki i ustawić tam paletke) lecz ideą było użycie prostej sięci na prostym przypadku (dzieki czemu łatwo ocenić czy wszystko jest jak należy) 
  
  
  =================================================
  
  
  English 
  
  
  The GUI is not ready yet, so to start the game player vs player you need to run the "Window" file
 (thus it is not possible to change the configuration at the moment except from the code level)
 
 Player vs Player control key
 
  player 1:
  "w" up
  "s" down
  
  player 2:
  
  "i" up
  "k" down
 
 
 
to run ai vs ai you just run the WindowAI file

the game is set at maximum speed
"control" available
"p" slows down the game so you can see what's going on
"o" speeds up the game again

"L" game switches to player vs AI mode
  the player takes control over player 1:
  "w" up
  "s" down
  
 if you want play vs AI you need to start the game and leave it for a few minutes at the highest speed (ime depends on your computer and luck because the neural network 
  program is non-deterministic)
  
  you can click "p" from time to time and see if AI can bounce the ball.
  
  Later I'm going to add some saved networks that can already play so that you can immediately play against AI
  
