# Elliot

Nous devons donc ici crack une archive zip.  
Dans un premier temps, il faut générer notre wordlist en rapport avec Mr.Robot.

Je vous invite à lancer un outil comme `BEWGor`, à vous rendre sur le wiki de la série, puis à lancer la génération. 
Une fois les 1.3 Millions de lignes correctement générées, nous pouvons utiliser `fcrackzip`pour finaliser l'opération :

```
fcrackzip -v -u -b -D -p wordlist.txt Private-data.zip
```
