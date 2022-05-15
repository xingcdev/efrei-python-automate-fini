## Structure d'automate dans .txt

A = lettres
{a, b, c}

Q = numéros >=0 sans rupture de séquence
{0,1,2,3,4} -> du coup si pas d'état on écrit -1 pour le repérer dans la table de transitions ?

I = nombre suivi de la liste, ou pas de numéro
ou Liste avec "-1" à la fin, voir si on veut gérer la fin de ligne ou pas

<? indiquer le nb de transitions ici pour que le programme sache quand s'arrêter ?>

T = récupérer la fin de fichier ou écrire "-1" sur la dernière ligne pour indiquer au programme que le fichier est terminé, ou i
Le sujet du TP ne demande pas de gérer l'epsilon, mais on pourrait le faire avec le caractère \* (BONUS ?)

```
A = a,b
Q = 1,2,3,4
I = 1,3
T = 2,4

Transitions :
1-a-2
1-b-4
3-a-4
3-b-2
4-b-3
-1
```

E (transitions) : 2a3,

## Algorithme expliqué

### Langage complémentaire

Le langage complémentaire est le fait que les états terminaux deviennent non terminaux, et vice-versa.

La fonction accepte en entrée la liste des états terminaux de l'automate

Créer une liste de nouveaux états terminaux `nouv_terminaux`.
Parcourir ancienne liste des états de l'automate et vérifier que pour chaque état :

- si l'état n'est présent dans `ancien_terminaux` alors l'ajouter dans `nouv_terminaux`

## Exemple d'automate

![automate](images/automate-exemple.png)

## Logique du programme

1.  slice()

```python
with open('workfile') as f:
    read_data = f.read()

```

2.

3. On enleve toutes les transitions sortantes et mettre une transition sortante sur les autres états

### Ce qu'on a appris

https://stackoverflow.com/a/4319271

### Enlever `\n` lors de `readlines()`

Ouvrier un fichier puis mettre le contenu dans une liste de chaîne de caractère

file.txt :

```
A = a,b
Q = 1,2,3,4
I = 1,3
T = 2,4
1,a,2
```

```python
with open("file.txt", 'r') as file:
    lines = file.readlines()
    # ['A = a,b\n', 'Q = 1,2,3,4\n', 'I = 1,3\n', 'T = 2,4\n', '1,a,2\n']

    lines = file.read().splitlines()
    # ['A = a,b', 'Q = 1,2,3,4', 'I = 1,3', 'T = 2,4', '1,a,2']
```

Source : [Getting rid of \n when using .readlines() - Stack Overflow](https://stackoverflow.com/a/15233379)
