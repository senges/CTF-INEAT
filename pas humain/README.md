# Pas humain

Ici, l'intro du challenge est un très bon indice.
Le text ressemble parfaitement à un texte classique (pas de chiffres ou caractères spéciaux), simplement les lettres ne correspondent à rien.

On peut donc supposer dans un premier temps qu'il s'agit d'un codage par décalage de lettre (Code de César), le plus classique étant le ROT13.

```text
$ cat intro.txt | rot13
Nous avons decouvert un portail menant vers un autre monde! Investiguez et ramenez le mot de passe de l’administrateur du service. Bon courage.
```

On fait donc un premier test avec netcat comme demandé.

```text
nc nothumans.ctf.ineat.fr 8080
test
UGGC/1.1 400 Onq Erdhrfg
Freire: atvak/1.16.1
Qngr: Fha, 17 Abi 2019 13:33:19 TZG
Pbagrag-Glcr: grkg/ugzy
Pbagrag-Yratgu: 270
Pbaarpgvba: pybfr
RGnt: "5qn5768o-10r"

<!qbpglcr ugzy>
<ugzy>
<urnq><gvgyr>400 Onq Erdhrfg</gvgyr></urnq>
<obql>
<pragre><u1>400 Onq Erdhrfg</u1></pragre>
<ue><pragre>atvak/1.15.12</pragre>
<o>Crhg-êger nirm-ibhf bhoyvé yr urnqre Ubfg: ? ;)</o>
<o>Znlor lbh'er zvffvat Ubfg: urnqre ? ;)</o>
</obql>
</ugzy>
```

```text
HTTP/1.1 400 Bad Request
Server: nginx/1.16.1
Date: Sun, 17 Nov 2019 13:33:19 GMT
Content-Type: text/html
Content-Length: 270
Connection: close
ETag: "5da5768b-10e"

<!doctype html>
<html>
<head><title>400 Bad Request</title></head>
<body>
<center><h1>400 Bad Request</h1></center>
<hr><center>nginx/1.15.12</center>
<b>Peut-être avez-vous oublié le header Host: ? ;)</b>
<b>Maybe you're missing Host: header ? ;)</b>
</body>
</html>
```

on va donc essayer d'envoyer une requête GET HTTP avec un host.

```
GET / HTTP/1.1
Host: toto

/* ROT13*/

TRG / UGGC/1.1
Ubfg: gbgb
```

Et voilà le travail `INEAT{!S1MPL3_ROT13_R3QUEST!}`
