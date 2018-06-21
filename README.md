# MacGyver-The-game-

Joue MacGyver et essaie de t'échapper du labyrinthe !

![mcgyver](https://media2.giphy.com/media/rR6t2tTUGe9ig/giphy.gif)

> NOTE: J'ai utilisé le module Pytest pour mes testes, tapez simplement ```pytest``` dans votre SHELL, depuis la racine du projet.

## Fonctionnalités demandés

- Labyrinthe possède un seul niveau
- ce niveau écrit dans un fichier
- mcgyver est controlé par les touches directionnelles
- 3 objets/items à ramasser (aiguille, tube plastique et éther)
- les objets spawnent aléatoirement
- la fenêtre du jeu est un carré de 15 sprites de longueur
- Macgyver récupère les objets en se posant dessus
- fin de la partie si mcgyver touche le garde
- victoire s'il a tout les objets, défaite sinon
- le programme s'éxecute en standalone

## Fonctionnalités ajoutés

- Un écran titre et un écran de victoire.
- des graphismes personnalisés (le liens des graphismes ne marchait pas, haha)
- des musiques et des sons
- un fichier de configuration
- il peut y avoir plusieurs gardiens.
- le joueur spawn aussi aléatoirement
- le joueur se déplace de façon animé d'une case à l'autre (rien de foufou)
- un menu montrant les items récupérés et le nombre d'items restants
- une génération dynamique des items; enlever/ajouter un item dans le dossier ```objects``` sera prit en compte par le programme.

## Préréquis

Il faut posséder ```Python 3.6```+ pour jouer à ce jeu (j'utilise les f-string, fonctionnalité de la 3.6)
Installer ```Pygame``` est aussi necessaire.
L'installation de ```Pytest``` est optionnelle, et permet de lancer les testes unitaires du projet.

## Comment jouer

![image du jeu](https://i.imgur.com/NsN91rq.png)

Le but du jeu est de toucher le gardien avec au moins 3 items.
Le personnage joueur est la chose avec des cheveux blonds, le gardien l'autre chose avec des cheveux bruns.
Pour bouger le personnage joueur, il suffit d'utiliser les touches directionnelles.
Pour "toucher" le gardien, il faut qu'il soit à une case du joueur, et enclencher un mouvement vers lui.
Une fois sur l'écran de victoire, cliquer avec la souris/appuyer sur une touche du clavier fermera le programme.
