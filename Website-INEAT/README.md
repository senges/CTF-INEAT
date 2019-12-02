# Website INEAT

Après un petit tour du site, on ne trouve pas grand chose d'intéressant. On va donc utiliser un petit outil de bruteforce de répertoires.
Personellement, j'ai utilisé `diresearch.py` dispo sur github.

```
python3 dirsearch.py -u https://website.ctf.ineat.fr -e php,asc,prk -r
```

> [09:39:55] 301 -  169B  - /files  ->  http://website.ctf.ineat.fr/files/
> [09:39:55] 403 -  555B  - /files/
> [09:39:58] 200 -   21KB - /index.php
> [09:40:07] 200 -    1KB - /robots.txt

