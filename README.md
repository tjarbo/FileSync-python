# FileSync-python
Lieber Daniel,
hier endlich nach langer Arbeit dein ersehntes Programm! Angepasst auf folgende Strukturen:

Festplatte
- [...] (Bsp. kommt noch)
    - "Musik" (zu synchronisierender Ordner)
        - "Projekt 1"
            - paar Datein.txt
        - weitere Datein

USB
- [...]
    - sync.py (wichtig, dass die sync.py genau hier über dem Sync-Ordner liegt!)
    - "Musik" (muss genau, wie der andere Ordner heißen)
      - weitere Ornder
        - weitere Datein
      - weitere Datein

> ## Wichtig !
> es darf nur noch Unterornder der Stufe 1 geben! 
> Damit meine ich ```./Musik/Proj1/weitere.dateinen``` 
>sind erlaubt!
>```./Musik/Proj2/BackUp/weitere.dateinen``` wiederrum nicht !

## Einrichten
1. Downloade das Repo
2. Ziehe die Datei an die oben angegebene Position auf dem USB-Stick
3. Bearbeite in sync.py in den ersten Zeilen die Configurationsvariabeln
Bsp:
```
(kommt noch)
```
4. Erstelle eine Verknüpfung für die Datei mit dem Inhalt ```sync.py "%1"```

Und dann kann es auch schon losgehen :)
