# WHOIS Lookup en Python

Ce projet fournit un script Python permettant de réaliser des recherches WHOIS pour des domaines. Le script offre des fonctionnalités interactives pour saisir les domaines, afficher les informations WHOIS, et les sauvegarder dans un fichier.

## Fonctionnalités

- **Validation de domaine** : Vérifie que le domaine saisi est valide.
- **Recherche WHOIS** : Récupère les informations WHOIS pour un ou plusieurs domaines.
- **Affichage des informations** : Présente les informations WHOIS de manière lisible.
- **Sauvegarde des résultats** : Permet d'enregistrer les résultats dans un fichier texte.
- **Recherche pour plusieurs domaines** : Prend en charge la recherche pour plusieurs domaines en une seule exécution.
- **Interface interactive** : Permet à l'utilisateur de saisir des domaines, de choisir de sauvegarder les résultats, et de faire plusieurs recherches.

## Prérequis

Avant de pouvoir utiliser le script, vous devez avoir Python installé sur votre machine. Vous aurez également besoin de la bibliothèque `python-whois`. Vous pouvez l'installer en utilisant pip :

```bash
pip install python-whois
Utilisation
Cloner le dépôt :
Clonez ce dépôt sur votre machine locale :

bash
Copier le code
git clone https://github.com/username/repository.git
cd repository
Exécuter le script :
Exécutez le script Python à l'aide de la commande suivante :

bash
Copier le code
python whois_lookup.py
Suivez les instructions interactives pour entrer les domaines et choisir les options souhaitées.

Exemples d'utilisation
Saisie d'un seul domaine :

scss
Copier le code
Entrez le(s) domaine(s) séparés par une virgule (ex. example.com, test.org): example.com
Saisie de plusieurs domaines :

scss
Copier le code
Entrez le(s) domaine(s) séparés par une virgule (ex. example.com, test.org): example.com, test.org
Sauvegarde des résultats :

bash
Copier le code
Souhaitez-vous sauvegarder les informations dans un fichier pour 'example.com' ? (o/n): o
Ré-exécution du script :

bash
Copier le code
Souhaitez-vous effectuer une autre recherche ? (o/n): n
Structure du projet
whois_lookup.py : Le script principal qui effectue les recherches WHOIS et gère les interactions avec l'utilisateur.
README.md : Ce fichier, qui explique le projet et son utilisation.
Contribuer
Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, veuillez soumettre une demande de tirage (pull request) avec vos modifications.

Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
