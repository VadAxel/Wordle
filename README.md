Appens syftar till att du som användare ska kunna spela WORDLE med flera olika funktioner.

Inställningar ger dig en möjlighet att ändra tema, Nytt Spel ger dig möjligheten att starta om med ett nytt ord.

Systemkrav:

Python 3, pysimpleGUI, Windows

Senaste Release:

https://github.com/VadAxel/Wordle/releases/tag/Wordle

Hur gör man?

1. Starta programmet
2. Skriv in din gissning alternativt byt tema
3. Avsluta (stäng programmet) eller klicka nytt spel

High score:

Lägsta poäng (som golf) ger högst placering på listan.

* Vid fel position, fel bokstav, erhålles: 2p
* Vid fel position, rätt bokstav, erhålles: 1p
* Vid rätt position, rätt bokstav, erhållas: 0p

Funktioner:

* main.py : startar programmet
* SwedishWordle.py : är grundprogrammet
* layout.py : ger grafikens grundläggande layout
* wordleGUI.py : sköter grafikuppdateringar
* open_hiscore.py : öppnar och läser tidigare high score
* file_score_upd.py : uppdaterar high score (vid vinst)
* result_text_func.py : översätter resultat till användare
* change_theme.py : ruta för uppdatering av tema/färger
