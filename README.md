# GolDigger

Un crawler web rapide et efficace écrit en Go pour la découverte automatique de liens et l'exploration de sites web, avec support automatique du parsing des `robots.txt` et `sitemap.xml`.

## Installation

### Installation rapide

```bash
go install github.com/ygp4ph/GolDigger/v2@latest
```

### Mise à jour

Pour mettre à jour l'outil vers la dernière version, relancez simplement la commande d'installation :

```bash
go install github.com/ygp4ph/GolDigger/v2@latest
```

### Compilation depuis les sources

```bash
# Cloner le repository
git clone https://github.com/ygp4ph/GolDigger.git
cd GolDigger

go install
```

## Utilisation

### Syntaxe de base (façon Nmap)

Il suffit de passer l'URL directement en argument, peu importe sa position. Le scanner ajoutera automatiquement le préfixe `https://` si manquant pour une exécution éclair.

```bash
./GolDigger <URL> [options]
# ou
./GolDigger [options] <URL>
```

### Protocoles couverts automatiquement

À chaque lancement, le crawler vérifie immédiatement à la racine de la cible :

- Le `/robots.txt` (extraction de toutes les arborescences listées dans `Allow` et `Disallow` + liens vers sitemaps personnalisés)
- Le `/sitemap.xml` naturel et extraits

### Options disponibles

| Flag | Alias       | Description                            | Défaut |
| ---- | ----------- | -------------------------------------- | ------ |
| `-d` | `--depth`   | Profondeur maximale de récursion       | 3      |
| `-e` | `--ext`     | Inclure également les liens externes   | false  |
| `-t` | `--tree`    | Afficher l'arbre des liens internes    | false  |
| `-o` | `--output`  | Sauvegarder les résultats en JSON      | -      |
| `-v` | `--verbose` | Afficher les erreurs détaillées        | false  |
| `-h` | `--help`    | Afficher l'aide                        | -      |
|      | `--version` | Afficher la version de l'outil         | -      |

### Exemple

```text
~/CTF/HTB/en_cours $ GolDigger ygp4ph.me

   ______      ______  _                      
  / ____/___  / / __ \(_)___ _____ ____  _____
 / / __/ __ \/ / / / / / __ `/ __ `/ _ \/ ___/
/ /_/ / /_/ / / /_/ / / /_/ / /_/ /  __/ /    
\____/\____/_/_____/_/\__, /\__, /\___/_/     
                     /____//____/             v2.3.0
 
[INF] Scanning https://ygp4ph.me (Depth: 3)
[INT] https://ygp4ph.me/assets/pdp_anime.mp4
[INT] https://ygp4ph.me/assets/pdp.png
[INT] https://ygp4ph.me/
[INT] https://ygp4ph.me/script.js
[INT] https://ygp4ph.me/assets/rooftop.jpg
[INT] https://ygp4ph.me/styles.css
[INT] https://ygp4ph.me#links
[INT] https://ygp4ph.me/assets/favi.png
[INT] https://ygp4ph.me/Portfolio/
[INT] https://ygp4ph.me/writeups/
[INT] https://ygp4ph.me/writeups/writeups.css
[INT] https://ygp4ph.me/writeups/chemistry/
[INT] https://ygp4ph.me/writeups/trickster/
[INT] https://ygp4ph.me/assets/labalsa.jpg
[INT] https://ygp4ph.me/Portfolio/gallery.js
[INT] https://ygp4ph.me/#links
[INT] https://ygp4ph.me/writeups/trickster/image.png
```
