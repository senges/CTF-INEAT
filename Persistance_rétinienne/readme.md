

# Persistance rétinienne
=======================================

### Détails du challenge

Points : 50
Catégorie : ## Stéganographie
Fichier : [cats_eyes.png](https://ctf.ineat.fr/files/a4ef5b3688b2f7047122ff768b25734f/cats_eyes.png)

```text
Un laboratoire de recherche scientifique a été attaqué et certains documents ont été volés.
Selon les médias, ce laboratoire étudie, entre autres, les stimulis visuels et la persistance de la réponse du ganglion rétinien du chat.
Vous avez trouvé un de ces documents, analysez-le et apprenez-en plus sur leurs recherches!
```

### Méthodologie

#### Analyse
Tout d'abord analysons le fichier

```bash
file ./cats_eyes.png
./cats_eyes.png: PNG image data, 640 x 320, 8-bit/color RGBA, non-interlaced

binwalk ./cats_eyes.png
DECIMAL       HEXADECIMAL     DESCRIPTION
    --------------------------------------------------------------------------------
    0             0x0             PNG image, 640 x 320, 8-bit/color RGBA, non-interlaced
    99            0x63            Zlib compressed data, best compression
    328355        0x502A3         Zlib compressed data, best compression
    334692        0x51B64         Zlib compressed data, best compression
```

    
Rien de vraiment intéressant ici.
Ouvrons le fichier avec un lecteur d'image (Navigateur, Logiciel par défaut de l'OS, ...)
    
#### Cas MacOS
Evidemment non prévu, le cas du lecteur d'image par défaut de Mac découpe l'image en 3 images distinctes dont une représente le flag écrit.
Fin de l'histoire pour les utilisateurs Mac qui n'ont peut être toujours pas compris l’intérêt de ce challenge.


#### Cas des vrais OS
En regardant assez longtemps l'image, on aperçoit subitement un flash qui disparait rapidement.
Il y a bien quelque chose d'étrange dans cette image.

Analysons son contenu avec l'outil [TweakPNG](https://github.com/jsummers/tweakpng)

Nous découvrons que l’image PNG est animée et contient:

  * Une première image affichée pendant 5 secondes
  * Une deuxième image affichée pendant 200 millisecondes: nous comprenons que le sujet de l'animation est de vérifier la persistance rétinienne.
  * Une troisième image affichée pendant 5 secondes

Modifions l'image pour ne pas afficher la première et la troisième image, mais seulement la deuxième directement avec les métadonnées des Chunks PNG.

Résultat : Seule la seconde image s'affiche et on peut lire le flag.

On comprend maintenant le comportement de mac qui ne semble pas savoir gérér les images .png animées.

#### Flag

`APRK{4N1M4710N_C0N7R0L_CHUNK}`
