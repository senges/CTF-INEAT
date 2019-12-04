

## Web logs


### Détails du challenge

Points : 150<br/>
Catégorie : Forensique<br/>
Fichier : [dump_web_logs.pcap](https://ctf.ineat.fr/files/992e48ac905e0f8331f5da2fc2528adc/dump_web_logs.pcap)<br/>

```text
Le site web de l’entreprise Foo-Bar s’est fait attaquer la semaine dernière.
L’administrateur a eu le temps de lancer une capture réseau afin d’avoir une traçabilité des potentielles fuites de données.
Investiguez et retrouver les données exfiltrées.
```

### TL;DR
Nous un fichier .pcap représentant la capture réseau d'une exploitation de SQLi (Time based). Un petit script python nous a permis de récupérer les données exfiltrées.

### Méthodologie


#### Wireshark

Nous pouvons ouvrir le fichier .pcap avec le logiciel Wireshark

```bash
wireshark dump_web_logs.pcap &
```

L'ensemble des paquets représentent des requêtes HTTP qui ont tous les mêmes pattern.

```text
GET /?user=Alex%22%20AND%20ASCII(SUBSTR(%09%09%09(SELECT%20passwd%20FROM%20accounts%20ORDER%20BY%20user%20LIMIT%200,1)%09%09%09,1,1))=113%20AND%20SLEEP(3)%20AND%20%221%22=%221 HTTP/1.1\r\n
```

Une fois décodée :

```
GET /?user=Alex" AND ASCII(SUBSTR((SELECT passwd FROM accounts ORDER BY user LIMIT 0,1),1,1))=113 AND SLEEP(3) AND "1"="1 HTTP/1.1\r\n`
```
En examinant les requêtes, on constate que l’attaquant effectue une injection SQL basée sur le temps (Time Based SQLi). La fonction ASCII () renvoie la valeur ascii d’une lettre. SUBSTR () renvoie une lettre à une position donné. Ici, chaque position est comparée à une plage allant de 0 à 255. Lorsqu'un résultat est évalué comme étant vrai (la valeur ascii est correcte), la réponse prend 3 secondes pour arriver. En d'autres termes, nous devons obtenir toutes les requêtes correctes ayant générées un délai de 3 secondes avec les requêtes suivantes.


#### Scripting

C'est l'heure de scripter tout cela! Nous allons faire un script python pour obtenir toutes les requêtes correctes. De plus, nous n’afficherons pas la totalité de la requête mais uniquement la partie ascii.

```python
from scapy.all import *

p = rdpcap("dump_web_logs.pcap")
output = ''

for i in range(len(p)-1):
	if (p[i+1].time - p[i].time) > 3:  # plus de 3 secondes encore la requête courante et la suivante
		rep = str(p[i][Raw])  
		rep = int(rep.split("%20AND%20SLEEP(3)")[0].split("=")[-1]) 
		if rep != 0:
			output += chr(rep)  
		elif output[-1] != '\n':
			output += '\n'
print(output)
```

Résultats:

```text
accounts
user
passwd
Administrator
Alex
Baptiste
APRK{SqLi_LoGs_ArE_s0_b1g_x1y2z3}
Zeeck4
Cre4sed
sqli
```

#### Flag

`APRK{SqLi_LoGs_ArE_s0_b1g_x1y2z3}`
