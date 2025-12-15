# FPS — Fraud Prediction System

## Présentation

**FPS (Fraud Prediction System)** est un projet pédagogique de machine learning appliqué à la détection de fraude dans des transactions crypto / Web3.

Le cœur du projet est le notebook **`FPS.ipynb`**, qui illustre **deux approches complémentaires** :

- une approche **supervisée avec labels synthétiques**
- une approche **réaliste sans labels** basée sur la détection d’anomalies

L’objectif n’est pas de “prédire la fraude réelle”, mais de démontrer une **compréhension rigoureuse des pipelines ML**, des métriques, et des pièges classiques du domaine.

---

## Objectifs du projet

Ce projet vise à démontrer :

- la construction d’un pipeline ML propre (sans data leakage)
- le choix de métriques adaptées aux classes déséquilibrées
- la différence entre labels artificiels et signaux exploitables
- une approche réaliste en absence de labels
- la capacité à **expliquer les limites d’un modèle**

---

## Installation & exécution

```bash
python -m venv .venv
# activer l'environnement, puis :
pip install -r requirements.txt
jupyter notebook
```
Ouvrir ensuite : `notebooks/FPS.ipynb`

---

## Dataset

- **Source** : Kaggle — *Synthetic Crypto/Web3 Transaction Dataset*
- **Type** : données transactionnelles synthétiques
- **Lien** : https://www.kaggle.com/datasets/chusmman/synthetic-cryptoweb3-transaction-dataset
- **Aucun label de fraude réel fourni**

Colonnes principales :

- `tx_hash`
- `from_wallet`, `to_wallet`
- `token`
- `amount`
- `gas_fee_usd`
- `platform`
- `tx_type`
- `timestamp`

> ⚠️ Les données sont **synthétiques** et utilisées uniquement à des fins pédagogiques.

---

## Contenu du notebook `FPS.ipynb`

### PARTIE A — Approche supervisée avec labels synthétiques

**Objectif :**
Illustrer un pipeline supervisé classique lorsque des labels sont disponibles.

**Étapes :**
1. Split train/test **avant toute création de label**
2. Création de labels synthétiques (`is_suspicious`) basés sur :
   - montants extrêmes (percentiles)
   - gas fees élevés
   - self-transfers
3. Analyse du déséquilibre de classes
4. Baseline naïve (toujours prédire la classe majoritaire)
5. Modèles supervisés :
   - Régression Logistique
   - Random Forest
6. Évaluation avec :
   - Recall (classe minoritaire)
   - PR AUC (métrique clé)
   - ROC AUC (comparaison)
7. Choix du seuil **sur un jeu de validation**
8. Tests de robustesse (*What would break this model?*)

**Message clé :**
Les performances élevées reflètent la capacité du modèle à **reproduire des règles**, pas à détecter une fraude réelle.

---

### PARTIE B — Approche réaliste sans labels

**Objectif :**
Illustrer une stratégie applicable lorsque **aucun label n’est disponible**.

**Pipeline :**
1. Détection d’anomalies non supervisée (IsolationForest)
2. Génération de scores d’anomalie
3. Création de pseudo-labels
4. Entraînement de modèles supervisés sur ces pseudo-labels
5. Analyse critique des résultats

**Points importants :**
- Pas de fuite de données
- Séparation stricte train/test
- Paramètre `contamination` explicitement discuté
- Mise en évidence du risque de circularité

---

## Métriques et bonnes pratiques

- ❌ Accuracy seule (trompeuse)
- ✅ Recall (classe suspecte)
- ✅ PR AUC (classe déséquilibrée)
- ⚠️ ROC AUC utilisé avec prudence

Le notebook montre également :
- pourquoi une baseline naïve est indispensable
- comment choisir un seuil sans biaiser l’évaluation
- comment interpréter un bon score de manière critique

---

## Limites assumées

- Pas de fraude réelle
- Pas d’historique par wallet
- Pas de graphes de transactions
- Pas de labels validés humainement

Ces limites sont **documentées volontairement**.

---

## À propos de l’usage de l’IA

Des outils modernes (ex. Cursor/LLM) ont été utilisés comme assistants pour accélérer l’itération.
Les choix de méthode (split, métriques, seuil, interprétation) et la cohérence du pipeline sont contrôlés et justifiés dans le notebook.

---

## Méthodologie & règles de développement ML

Ce projet s’appuie sur un cadre méthodologique explicite visant à :
- éviter les fuites de données (data leakage),
- garantir la reproductibilité,
- maintenir une séparation claire entre exploration, features et modèles,
- utiliser l’IA comme copilote contrôlé (AIDD).

Les règles et checklists sont documentées dans :
- `docs/rules/aidd_rules.md`
- `docs/rules/ml_rules.md`
- `docs/rules/ml_checklist.md`

Ces documents font partie intégrante du projet.


---

## Licence

MIT
