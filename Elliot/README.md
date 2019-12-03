# Elliot

Nous devons donc ici cracker une archive zip.  

Dans un premier temps, il faut générer notre wordlist en rapport avec Mr.Robot.

Je vous invite à lancer un outil comme `BEWGor`, à vous rendre sur le wiki de la série (https://fr.wikipedia.org/wiki/Mr._Robot_(s%C3%A9rie_t%C3%A9l%C3%A9vis%C3%A9e)), puis à lancer la génération. 

Une fois les 1.3 Millions de lignes correctement générées, nous pouvons utiliser `fcrackzip`pour finaliser l'opération :

```
fcrackzip -v -u -b -D -p wordlist.txt Private-data.zip
```

Mot de passe de l'archive : `Elliot1986Fsociety`
Et flag : `INEAT{Elliot1986Fsociety}`