# Emoji

Ici l'intitulé est assez simple, on a trois secondes pour compter le nombre d'occurences de certains emojis.
Comme c'est impossible de le faire à la main, on doit écrire un bout de code qui le fait à notre place.

> Par soucis de gains de temps, je suis parti sur un code php avec une façon discutable de parser l'arbre DOM..
> C'est probablement la  pire façon de résoudre ce challenge, mais ça fonctionne

##Solution php

```php
<?php

define("URL", "https://emoji.ctf.ineat.fr/");
define("COOKIE", "PHPSESSID=xxxxxxxxxxxxxx");

$target1 = 0;
$target2 = 0;

$options = array(
    'http' => array(
        'header'  => "Content-type: application/x-www-form-urlencoded\r\n" . "Cookie: " . COOKIE . "\r\n" . "Connection: keep-alive\r\n",
        'method'  => 'GET'
    )
);

$context  = stream_context_create($options);

$raw = file_get_contents(URL, false, $context);
$raw = explode('<hr/>', $raw);

$haystack = str_replace('<div style="font-size:14px;">', '', $raw[1]);
$haystack = str_replace(' ', '', $haystack);
$haystack = str_replace('</div>', '', $haystack);
$haystack = preg_split('//u', $haystack);

$targets = str_replace('<label for="nb1">Nombre de ', '', $raw[2]);
$targets = str_replace('<label for="nb2">Nombre de ', '', $targets);
$targets = str_replace(':', '', $targets);

$targets = str_replace('<input type="number" name="nb1"/>', '', $targets);
$targets = str_replace(' ', '', $targets);
$targets = trim(preg_replace('/\s\s+/', '', $targets));
$targets = explode('</label>', $targets);

foreach ($haystack as &$smiley) {
    switch ($smiley) {
        case $targets[0]:
            $target1++;
            break;

        case $targets[1]:
            $target2++;
            break;
        
        default:
            break;
    }
}

$fields = [
    'nb1' => $target1,
    'nb2' => $target2
];

$header = array(
    'Content-Type: application/x-www-form-urlencoded',
    'DNT: 1',
    'Connection: keep-alive',
    'Referer: URL',
    'Keep-Alive: 300'
);

$fields_string = http_build_query($fields);

$ch = curl_init();

curl_setopt($ch,CURLOPT_URL, URL);
curl_setopt($ch,CURLOPT_POST, true);
curl_setopt($ch,CURLOPT_POSTFIELDS, $fields_string);
curl_setopt($ch,CURLOPT_HTTPHEADER, $header);
curl_setopt($ch,CURLOPT_COOKIE, COOKIE);

curl_setopt($ch, CURLINFO_HEADER_OUT, true);
curl_setopt($ch, CURLOPT_VERBOSE, 1);
curl_setopt($ch, CURLOPT_HEADER, 1);
curl_setopt($ch,CURLOPT_RETURNTRANSFER, true);

echo curl_exec($ch);

?>
```

##Solution python
```python
import requests
import time

url = "https://emoji.ctf.ineat.fr/"

s = requests.session()
r = s.get(url).text

recherche = r.split("nombre de ")[1]

r1,r2 = recherche.split(" et de ")

nb1 = r.count(r1) - 2
nb2 = r.count(r2[0]) - 2

r = s.post(url,data={"nb1":nb1,"nb2":nb2}).text

print(r)
```

##Solution javascript
```javascript
Max 6 ou 7 lignes
```