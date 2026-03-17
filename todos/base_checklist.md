Exploratory Data Analysis

Objectif: comprendre au maximum les données dont on dispose pour définir une stratégie de modélisation.

I - Analyse de la forme:
	[] Identification de la target
	[] Nombre des lignes et de colonnes 
	[] Identification des valeurs manquantes 
	[] Types de variables

II - Analyse du fond:
	[] Visualisation de la target (histogramme/boxplot)
	[] Compréhension des différentes variables (recherche)
	[] Visualisation des relations : features/target
	[] Identification des outliers


Pre-processing

Objectif: transformer le data pour le mettre dans un format propice au machine learning

	[] Création du Train Set / Test Set
	[] Élimination des NaN : dropna(), imputation, colonne"vides"
	[] Encodage
	[] Suppression des outliers néfastes au modèle
	[] Feature selection
	[] Feature engineering
	[] Feature scaling

Modelling

Objectif: développer un modèle de machine learning capable de répondre a l'objectif final.

	[] Définir une fonction d'évaluation
	[] Entrainement de différents modèles
	[] Optimisation avec GridSearchCV
	[] Analyse des erreurs et retour au Preprocessing / EDA
           Learning Curve et prise de décision