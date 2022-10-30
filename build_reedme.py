# Automatisela création du fichier README.md
import os
from glob import glob
import json

BASE_PATH = "https://dylanbaptiste.github.io/NN-2D-Projection"
TITLE = "NN-2D-Projection"
DESC = "Visualisation de projection de données 2D avec des réseaux de neurones"

PATH_HTML = ".\\Resultats"
PATH_HIST = ".\\Training_Historique"
# liste les fichier html
HTMLS = glob(PATH_HTML + "\\*.html")
RUN_NAMES = [os.path.basename(f).split('.')[0] for f in HTMLS]
CONFIGS = [f"{PATH_HIST}\\HIST_{run}\\config.json" for run in RUN_NAMES]

README = f"""
# {TITLE}
{DESC}  
## Liste des runs :
| Lien | Description | LR | Epochs | Batch Size | Optimizer |
| ---- | --- | --- | --- | --- | --- |
"""
for html, config, run in zip(HTMLS, CONFIGS, RUN_NAMES):
	run_data = {}
	try:
		with open(config, 'r') as f:
			run_data = json.load(f)
	except:
		pass
	optimizer = run_data.get('OPTIMIZER', {})
	optimizer = optimizer.get('name', 'None')
	README += f"""| [{run}]({BASE_PATH}/Resultats/{run}.html) | {run_data.get('description', 'Aucune')} | {run_data.get('LR', 'Aucune')} | {run_data.get('EPOCH', 'Aucune')} | {run_data.get('BATCH_SIZE', 'Aucune')} | {optimizer} |\n"""

README += """
## Qu'est-ce que c'est ?
L'avant-dernière couche du modèle est composé de 2 neurones activés par la fonction tangente hyperbolique $\\tanh(z) = \\frac{e^z - e^{-z}}{e^z + e^{-z}}$ qui donne une valeur entre -1 et 1.  
À chaque époque d'entrainement le modèle est évalué sur des données qu'il n'a jamais vues (donnée de validation) et la valeur d'activation pour chaque donnée à la sortie de cette avant-dernière couche est enregistrée. Ces valeurs sont ensuite projetées dans un plan 2D avec en ordonnée la valeur d'activation du premier neurone et en abscisse la valeur d'activation du deuxième neurone. On peut ainsi visualiser la représentation 2D que fait le modèle des données (plot central).

La dernière couche est composée d'un neurone activé en sigmoïde $\sigma(z) = \\frac{1}{1 + e^{-z}}$ qui donne une valeur entre 0 et 1 permetant la classification binaire. L'espace des données d'entrainements est alors segmenté sur une plage de valeur entre 0 et 1 (plot de droite).

Si ce travail vous a plu, vous aimeiez peut etre aussi: https://playground.tensorflow.org/
"""
with open("README.md", 'w+', encoding='utf-8') as f:
	f.write(README)

