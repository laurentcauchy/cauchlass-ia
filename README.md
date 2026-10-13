# CAUCHLASS IA / CloseAI — V1

Site statique FR/EN, cinq rubriques : Accueil, Météo IA, Évolution, Registre des risques et Notre mission. Les fichiers publics sont exclusivement dans `site/`. Aucun service payant, bibliothèque distante ou clé secrète n’est nécessaire.

## Aperçu

Depuis ce dossier, lancer `python3 -m http.server 8765 --directory site`, puis ouvrir http://localhost:8765. Le chargement des données nécessite un serveur HTTP ; une ouverture directe du HTML en fichier local peut bloquer les données.

## Publication GitHub Pages

Publication initiale autorisée par Laurent le 9 octobre 2026. Compte : **laurentcauchy**. Dépôt public : **cauchlass-ia**.

Adresse du site : `https://laurentcauchy.github.io/cauchlass-ia/`.

La source de publication est GitHub Actions. Pour les éditions suivantes, vérifier le commit à publier, obtenir l’approbation puis lancer le workflow « Publish approved CAUCHLASS IA edition » en cochant l’approbation. La publication n’est déclenchée ni par un envoi de fichiers ni par une horloge. Configurer une protection d’environnement avec relecteur si cette option est disponible dans le compte.

Le workflow téléverse uniquement `site/`. Les documents CloseAI copiés dans `site/sources/` font partie des contenus publics approuvés. Aucun fichier issu des autres dépôts GitHub n’est utilisé.

Documentation : https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages

## Sources et réserves

Deux documents disponibles récupérés : bulletin Word et tableau Excel du 9 octobre 2026. Ils sont conservés sans modification dans `site/sources/`. La conversation référencée n’a fourni que des marqueurs de contenu pour les réponses de l’assistant ; les détails de l’ancienne maquette n’étaient pas accessibles. La V1 suit les exigences explicites du présent échange.

Le fichier maître historique n’a pas été retrouvé. Les indices historiques de N01–N06, N08, N09, N12 et N14 restent visibles comme entrées à compléter, mais sont exclus du graphique. Le graphique reproduit seulement N07, N10, N11, N13 et N15, soit cinq fiches détaillées. Ces indices sont une opinion éditoriale CloseAI sourcée dans le classeur, et non une mesure externe du risque. Les lignes détaillées ne sont pas toutes vérifiées indépendamment. Aucune moyenne, probabilité ou série historique inventée.

N16 est cité mais absent du registre fourni : aucun nouvel indice ajouté. Le signal N15 reste explicitement importé et à revalider (liens Reuters et WSJ non vérifiés). L’étude Zenity est accessible ; le désaccord AWS est conservé en citant la réponse rapportée par The Next Web. Vérification des sources : 9 octobre 2026.

## Mise à jour quotidienne à partir de la veille de 8 h

**État : publication GitHub reliée à une validation explicite par e-mail ; veille et génération quotidienne encore à raccorder.** Une publication n’est autorisée qu’après réponse de Laurent au mail récapitulatif de mise à jour. La veille de 8 h reste à relier proprement au générateur de candidat.

1. La veille existante de **8 h Europe/Paris** recherche les nouveaux éléments et produit un candidat complet au format de `site/data/bulletin.json`, plus ses documents sources. L’heure doit rester liée à Europe/Paris pour suivre l’heure d’été ; elle ne garantit pas une publication à 8 h.
2. Vérifier les liens et distinguer faits, interprétation, hypothèse, désaccord et limites. Garder les indices précédents s’il n’y a pas de justification. Traduire tous les champs et conserver l’historique. Sans nouveau bulletin vérifié, ne pas modifier la date de fraîcheur.
3. Exécuter `python3 scripts/update.py chemin/vers/candidat.json`. Ce contrôle ne modifie rien. Le validateur vérifie structure, traductions et références ; il ne peut pas certifier la véracité des sources.
4. Laurent relit le candidat, puis autorise son intégration : `python3 scripts/update.py chemin/vers/candidat.json --apply --approved-by Laurent`. Ce paramètre consigne une approbation obtenue au préalable ; il ne la sollicite pas et n’est pas un contrôle d’identité. Une archive est conservée avant le remplacement atomique des données. Les nouveaux documents source doivent être ajoutés dans `site/sources/` avant intégration.
5. Tester l’affichage puis envoyer les modifications au dépôt ; déclencher la publication manuelle après approbation. Pour une future publication quotidienne sans présence humaine, Laurent devra autoriser explicitement ce changement et un raccordement de la veille devra être testé de bout en bout. Aucun déclencheur quotidien factice n’est livré.

Les contenus quotidiens FR/EN, le niveau, les risques et les événements sont dans le JSON. Le niveau « very-high » est le seul niveau mis en forme dans cette V1 : un changement de l’échelle nécessite une revue de la présentation et du validateur. Le site signale un bulletin de plus d’un jour ; il ne se prétend pas à jour par simple ouverture.

## Contrôles

`python3 scripts/validate.py` vérifie le fichier courant. Tests navigateur : cinq rubriques dans les deux langues, ordinateur/mobile, recherche et filtres, fiches dépliables, état sans résultat, téléchargements locaux, agrandissement du texte, erreur de chargement et reprise. Les résultats et captures sont livrés à côté du site. Aucun test ne publie de contenu.
