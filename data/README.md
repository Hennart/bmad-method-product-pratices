# 📊 ADEO Global Ready Requirements - Source de Vérité

## 🎯 Objectif

Ce fichier CSV est la **source unique de vérité** pour tous les requirements ADEO Global Ready 2026.

**Fichier** : `2026-Global-Ready-Requirements.csv`

## 🔄 Utilisation

### Par Giovanni (ADEO Technical Lead Agent)
Giovanni **lit ce fichier** à chaque assessment pour :
- ✅ Obtenir les requirements les plus récents
- ✅ Vérifier les IDs, descriptions et niveaux
- ✅ Construire les évaluations et plans d'action
- ✅ Garantir la cohérence avec les standards ADEO

### Par les Équipes Produit
Ce fichier permet de :
- 📋 Tracker les assessments produits
- ✅ Marquer les requirements comme YES/NO/NOT APPLICABLE
- 📝 Ajouter des commentaires et précisions
- 🔗 Référencer les JIRA issues associées

## 📁 Structure du Fichier

| Colonne | Description | Exemple |
|---------|-------------|---------|
| **Version** | Année du framework | 2026 |
| **Domain** | Domaine technique | Security, APIzation, Data... |
| **Topic** | Sous-domaine | Identity Access Management |
| **Level** | Niveau de maturité | 2, 3, 4, 5, 6 |
| **#** | ID unique du requirement | SEC-IAM-#10 |
| **Requirement** | Nom court | Identity & Access Governance |
| **Description** | Description complète | I keep every human and non-human... |
| **Gitbook link** | Lien documentation | SEC-IAM-#10 |
| **Assessment** | Statut évaluation | YES / NO / NOT APPLICABLE |
| **Issue Keys** | JIRA tickets liés | GOT-1234, GOT-5678 |
| **Comment / Precision** | Notes additionnelles | We don't have personal data |
| **Workload** | Estimation effort | 2 weeks, 3 sprints |
| **Delay** | Délai prévu | Q2 2026 |

## 🔄 Comment Mettre à Jour

### Option 1 : Édition Directe
```bash
# Ouvrir avec votre éditeur préféré
code data/2026-Global-Ready-Requirements.csv

# Ou avec un tableur (Excel, Google Sheets)
# Attention : Toujours réexporter en CSV avec encodage UTF-8
```

### Option 2 : Importer depuis Excel
```bash
# 1. Exporter votre fichier Excel en CSV
# 2. Remplacer le fichier
cp ~/Downloads/GlobalReady2026.xlsx data/
# Ou convertir : xlsx2csv GlobalReady2026.xlsx > data/2026-Global-Ready-Requirements.csv
```

### Option 3 : Script de Mise à Jour
```python
# Exemple de script Python pour mise à jour programmatique
import pandas as pd

# Lire le CSV
df = pd.read_csv('data/2026-Global-Ready-Requirements.csv')

# Modifier (exemple : marquer un requirement comme YES)
df.loc[df['#'] == 'SEC-IAM-#10', 'Assessment'] = 'YES'
df.loc[df['#'] == 'SEC-IAM-#10', 'Comment / Precision'] = 'Implemented on Q1 2026'

# Sauvegarder
df.to_csv('data/2026-Global-Ready-Requirements.csv', index=False)
```

## ⚠️ Règles Importantes

### ✅ À Faire
- Toujours utiliser l'encodage **UTF-8**
- Respecter la structure des colonnes
- Garder les IDs uniques inchangés
- Commiter les changements avec un message clair
- Tester avec Giovanni après modification

### ❌ À Éviter
- Ne pas changer les noms de colonnes
- Ne pas modifier les IDs des requirements existants
- Ne pas supprimer de lignes sans raison
- Ne pas mélanger les séparateurs (toujours virgule)

## 🔍 Validation du Fichier

### Vérification Manuelle
```bash
# Vérifier le nombre de lignes
wc -l data/2026-Global-Ready-Requirements.csv

# Vérifier la structure
head -5 data/2026-Global-Ready-Requirements.csv

# Rechercher un requirement
grep "SEC-IAM-#10" data/2026-Global-Ready-Requirements.csv
```

### Validation avec Giovanni
```
Giovanni, vérifie que le fichier Global Ready est valide
```

## 📊 Statistiques Actuelles

- **Total Requirements** : 200+
- **Domaines** : 8
- **Topics** : 26+
- **Niveaux** : 2-6
- **Dernière Mise à Jour** : 2026-03-10

## 🔄 Workflow de Mise à Jour

```
1. Modifier le CSV
   ↓
2. Valider la structure
   ↓
3. Commiter les changements
   ↓
4. Giovanni lit automatiquement la nouvelle version
   ↓
5. Tester avec un assessment
```

## 🎯 Exemples d'Utilisation

### Marquer un Requirement comme Complété
```csv
# Avant
...,SEC-IAM-#10,...,Identity & Access Governance,...,,,,,,

# Après
...,SEC-IAM-#10,...,Identity & Access Governance,...,YES,GOT-1234,Implemented IAM governance,2 weeks,Q1 2026
```

### Ajouter un Nouveau Requirement
```csv
2026,Security,Identity Access Management,3,SEC-IAM-#23,New Requirement,Description here,SEC-IAM-#23,,,,,,,
```

### Marquer comme Non Applicable
```csv
...,DCO-CAU-#10,...,Collect point identification,...,NOT APPLICABLE,,We don't process personal data,,
```

## 🔗 Intégration

### Avec Giovanni
Giovanni lit ce fichier pour :
- Assessment Global Ready complet
- Vérification compliance
- Génération de plans d'action

### Avec Pierre
Pierre peut créer des Initiatives/Epics basées sur les requirements :
```
Pierre, crée une Initiative pour implémenter les requirements SEC-IAM-#20 à SEC-IAM-#22
```

### Avec Dashboards
Ce fichier peut être importé dans :
- Power BI / Tableau pour visualisation
- JIRA pour tracking
- Confluence pour documentation

## 📝 Template pour Nouveaux Requirements

```csv
Version,Domain,Topic,Level,#,Requirement,Description,Gitbook link,Assessment,Issue Keys,Comment,Workload,Delay
2026,[Domain],[Topic],[Level],[DOMAIN-TOPIC-#XX],[Name],[Full description],[Link],,,,,[Effort],[Timeline]
```

## 🚀 Commandes Utiles

### Git
```bash
# Voir les modifications
git diff data/2026-Global-Ready-Requirements.csv

# Commiter les changements
git add data/2026-Global-Ready-Requirements.csv
git commit -m "feat: Update Global Ready requirements - [description]"

# Voir l'historique
git log --follow data/2026-Global-Ready-Requirements.csv
```

### Recherche
```bash
# Trouver tous les requirements Security niveau 3
grep "2026,Security,.*,3," data/2026-Global-Ready-Requirements.csv

# Compter les requirements par domaine
cut -d',' -f2 data/2026-Global-Ready-Requirements.csv | sort | uniq -c

# Lister les requirements marqués YES
grep ",YES," data/2026-Global-Ready-Requirements.csv
```

## 📞 Support

Pour toute question sur la gestion du fichier :
- Consulter Giovanni : `Giovanni, aide-moi avec le fichier Global Ready`
- Voir la documentation : `ADEO-AGENT-TECHNICAL-LEAD-FR.md`
- Check le README : `src/bmm/agents/README-GIOVANNI.md`

---

**Ce fichier est votre source de vérité pour Global Ready. Maintenez-le à jour et Giovanni fera le reste !** 📊✨
