# Automatisela création du fichier README.md
import os
from glob import glob
import json

TITLE = "NN-2D-Projection"
DESC = "Visualisation de données 2D avec des réseaux de neurones"

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
	README += f"""| [{run}]({html}) | {run_data.get('description', 'Aucune')} | {run_data.get('LR', 'Aucune')} | {run_data.get('EPOCH', 'Aucune')} | {run_data.get('BATCH_SIZE', 'Aucune')} | {optimizer} |\n"""

with open("README.md", 'w+', encoding='utf-8') as f:
	f.write(README)

