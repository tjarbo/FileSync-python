<a href="http://its.tjarbo.me">
    <img src="https://github.com/tjarbo/FileSync-python/blob/master/Ressourcen/logo.png" alt="FileSyncLogo" title="FileSync" align="right" height="80" />
</a>

# FileSync-python

Lieber Daniel,
hier ist endlich dein gewünschtes Programm ... Aber "leider" erstmal nicht für Windows :P Solange musst du halt eben noch warten, oder du steigst endlich auf Linux um xD

## Was und worfür is FileSync-python ?
Die sync.py ist ein kleines in Python2.7 geschriebenes, einfachgehaltenes Synchronisations-Tool um **ein** Verzeichnis auf 2 Speichermedien synchron zu halten.

### Beispiel:

_Festplatte_
- /home/tjarbo/
    - musik/ (zu synchronisierender Ordner)
        - "Projekt_1/"
            - paarDateien.txt
        - weitereDateien

_USB_
- /
    - sync.py (wichtig, dass die sync.py genau hier über dem Sync-Ordner liegt!)
    - musik/ (muss genau, wie der andere Ordner heißen)
      - weitere_Ornder/
        - weitereDateien
      - weitere_Dateien

> ## Wichtig !
> Da es _einfach_ gehalten wurde, daf es nur Unterornder der Stufe 1 geben! Damit meine ich ```./musik/Proj1/weitere.dateinen``` wäre erlaubt <-> ```./musik/Proj2/BackUp/weitere.dateinen``` wiederrum nicht !
> ## genauso:
> Der Sync-Ordner muss auf beiden Speichermedien schon existieren && es dürfen keine Leerzeichen in Namen verwendet werden (weil _einfach_ gehalten) 

## Einrichten
1. Downloade das Repo
2. Ziehe die Datei ```sync.py``` an die im Bsp. angegebene Position auf dem USB-Stick
3. Bearbeite die Configurationsvariabeln in den ersten Zeilen der sync.py

Bsp:
```
PfadAufHDD = "/home/tjarbo/" 
OrdnerName = "musik"
```

4. Starte das Script mit ```$ python sync.py```
