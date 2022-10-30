
# NN-2D-Projection
Visualisation de projection de données 2D avec des réseaux de neurones  
## Liste des runs :
| Lien | Description | LR | Epochs | Batch Size | Optimizer |
| ---- | --- | --- | --- | --- | --- |
| [20221019_171014](https://dylanbaptiste.github.io/NN-2D-Projection/Resultats/20221019_171014.html) | Aucune | 0.0001 | 100 | 64 | Adam |

## Qu'est-ce que c'est ?
L'avant-dernière couche du modèle est composé de 2 neurones activés par la fonction tangente hyperbolique $\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$ qui donne une valeur entre -1 et 1.  
À chaque époque d'entrainement le modèle est évalué sur des données qu'il n'a jamais vues (donnée de validation) et la valeur d'activation pour chaque donnée à la sortie de cette avant-dernière couche est enregistrée. Ces valeurs sont ensuite projetées dans un plan 2D avec en ordonnée la valeur d'activation du premier neurone et en abscisse la valeur d'activation du deuxième neurone. On peut ainsi visualiser la représentation 2D que fait le modèle des données (plot central).

La dernière couche est composée d'un neurone activé en sigmoïde $\sigma(z) = \frac{1}{1 + e^{-z}}$ qui donne une valeur entre 0 et 1 permetant la classification binaire. L'espace des données d'entrainements est alors segmenté sur une plage de valeur entre 0 et 1 (plot de droite).

Si ce travail vous a plu, vous aimeiez peut etre aussi: https://playground.tensorflow.org/
