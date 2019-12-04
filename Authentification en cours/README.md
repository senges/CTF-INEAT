# Authentification en cours

Pour ce challenge, il faut connaitre un peu le fonctionnement de emacs (ou d'autres outils sous linux) qui a une facheuse tendance à générer des fichiers cachés lorsqu'on édite un fichier.
Les nouveaux fichiers temporaires sont suffixés avec "~" selon : `<nom du fichier>~`

On peut donc supposer ici que nos fichiers php n'échappent pas à cette règle :

```
$  wget https://authent.ctf.ineat.fr/index.php~
[...]
index.php~                               100%[==================================================================================>]   1.70K  --.-KB/s    in 0s

2019-12-02 14:14:26 (74.4 MB/s) - ‘index.php~’ saved [1740/1740]
```

On retrouve à l'interrieur les login/mdp :

```php
//TODO : Change it
$username="admin";
$password="monS3p3rP4ss1ntr0uv4bl3";
```

Il ne reste plus qu'à se connecter pour récupérer le flag : `INEAT{v1m-0r-N4n0-or-3ma4cs}`
