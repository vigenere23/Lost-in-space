# Perdu dans l'espace

## À propos

Projet scolaire réalisé dans le cadre du cours GLO-1901: Introduction à la programmation avec Python. On contrôle un vaisseau en tentant de rejoindre l'arrivée le plus vite possible, avec la quantité de gaz donnée. Possibilité de multi-joueurs en ligne jusqu'à 4. 

P.S.: Les images n'étaient pas données, elles ont donc été crée sur Inkscape :)

## Execution examples

Go to the project's root folder. Then : 

### Server

```bash
python -m server.server
```

### Client

Offline :
```bash
python -m client.perdu player1 -o monde2
```

## Développement

Le développement d'un nouveau serveur est maintenant débuté. À voir sur la branche `new_server`.

## Problèmes connus

### Serveur déconnecté

Bien que non-supposé, le serveur, hébergé à l'Université Laval, a été déconnecté. Il n'est donc plus possible d'y jouer. Voir la section "Futur" pour de plus amples renseignement. 

### Flickering

Un effet de "flickering screen" peut être observé sur certains écrans. La cause reste encore inconnue.

## Futur

### Serveur maison [En cours]

Afin de contourner la problématique du serveur, il serait également possible d'en créer un sois-même et de l'implenter au sein du jeu. Il deviendrait donc entièrement portable et indépendant. 

## TODO

* Responding to ship status update
* Deleting server game and terminating thread when game has finished
* Implementing the "join" command
