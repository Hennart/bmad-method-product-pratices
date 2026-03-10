# 💻 Giovanni - ADEO Technical Lead

## Vue d'Ensemble

**Giovanni** est l'agent technique ADEO expert du **framework Global Ready 2026**. Il guide les équipes techniques vers l'excellence à travers **8 domaines critiques** avec des niveaux de maturité progressifs (2-6).

## 🎯 Quand Utiliser Giovanni ?

Giovanni intervient pour :

### ✅ Assessment et Conformité
- Évaluer la maturité Global Ready de votre produit
- Identifier les gaps de conformité
- Créer des roadmaps d'amélioration technique

### ✅ Guidance Technique
- Standards API (APIzation)
- Gestion et qualité des données (Data)
- Conformité RGPD (Data Compliance)
- CI/CD et automatisation (Dev Factory)
- Excellence opérationnelle (Operations)
- Assurance qualité (Quality)
- Sécurité complète (Security)
- Dette technique (Product Management)

### ✅ Amélioration Continue
- Plans d'action priorisés
- Montée en maturité progressive
- Best practices ADEO

## 🚀 Démarrage Rapide

### 1. Lancer un Assessment Global
```
Giovanni, je voudrais faire un assessment Global Ready de mon produit [Nom du Produit]
```

Giovanni va :
- Poser des questions sur chacun des 8 domaines
- Évaluer votre niveau de maturité actuel
- Identifier les gaps critiques
- Proposer un plan d'action priorisé

### 2. Obtenir de l'Aide sur un Domaine Spécifique
```
Giovanni, j'ai besoin d'aide pour [APIzation/Data/Security/etc.]
```

### 3. Créer un Plan d'Amélioration
```
Giovanni, comment améliorer mon niveau de maturité en [Domaine] ?
```

## 📊 Les 8 Domaines Global Ready

| Domaine | Focus | Niveaux |
|---------|-------|---------|
| 🔌 **APIzation** | Design, exposition et gestion d'APIs | 2-4 |
| 📊 **Data** | Maîtrise, qualité et distribution des données | 2-6 |
| 🔐 **Data Compliance** | RGPD et protection données personnelles | 2-4 |
| 🏭 **Dev Factory** | CI/CD, automatisation, releases | 2-6 |
| ⚙️ **Operations** | Change, FinOps, Hosting, Incidents, Observability, Reliability | 2-6 |
| 📦 **Product Management** | Gestion de la dette technique | 2-6 |
| ✅ **Quality** | Tests, qualité delivery et management | 2-6 |
| 🔒 **Security** | Application, IAM, Infrastructure, Risk | 2-6 |

## 🎯 Workflows Disponibles

### Assessment & Amélioration
- `[GRA]` **Global Ready Assessment** - Assessment complet 8 domaines
- `[GRI]` **Global Ready Improve** - Plan d'action pour un domaine

### Domaines Spécifiques
- `[API]` **APIzation Guide** - Design et standards API
- `[DAT]` **Data Management** - Données et qualité
- `[DCO]` **Data Compliance** - RGPD
- `[DFA]` **Dev Factory** - CI/CD
- `[OPS]` **Operations Guide** - Excellence opérationnelle
- `[QUA]` **Quality Guide** - Qualité et tests
- `[SEC]` **Security Guide** - Sécurité
- `[DBT]` **Debt Management** - Dette technique

### Support
- `[GRH]` **Global Ready Help** - Aide générale

## 💡 Exemples d'Utilisation

### Exemple 1 : Assessment Complet
```
Utilisateur: "Giovanni, je dois évaluer mon produit 'Customer Portal' 
              pour Global Ready 2026"

Giovanni guide:
1. Collecte contexte produit
2. Évalue chaque domaine avec questions ciblées
3. Détermine niveau maturité actuel
4. Identifie gaps par rapport aux exigences
5. Génère rapport avec plan d'action priorisé
```

### Exemple 2 : Amélioration Sécurité
```
Utilisateur: "Notre produit est au niveau 2 en Security, 
              comment passer au niveau 3 ?"

Giovanni guide:
1. Identifie requirements niveau 3 manquants
2. Détaille chaque requirement (SEC-APP-#20, SEC-IAM-#20, etc.)
3. Estime l'effort par requirement
4. Propose ordre d'implémentation
5. Donne best practices ADEO
```

### Exemple 3 : Mise en Place CI/CD
```
Utilisateur: "Comment améliorer notre Dev Factory ?"

Giovanni guide:
1. Évalue CI/CD actuel
2. Identifie gaps (DFA-CIT-#X, DFA-CDL-#X, DFA-CDP-#X)
3. Propose roadmap progressive
4. Donne exemples configurations
5. Suggère outils ADEO (registry, etc.)
```

## 📋 Format des Requirements

Chaque requirement est identifié par un ID unique :

**Format** : `[DOMAIN]-[TOPIC]-#[LEVEL][VARIANT]`

**Exemples** :
- `API-DES-#10` : APIzation > Design API > Level 2 > Requirement 0
- `SEC-IAM-#21` : Security > IAM > Level 3 > Requirement 1
- `OPS-OBS-#32` : Operations > Observability > Level 4 > Requirement 2

## 🔗 Collaboration avec Autres Agents

### Giovanni + Pierre (ADEO Delivery Manager)
- Giovanni identifie improvements techniques → Pierre crée Epics/Stories
- Giovanni définit requirements → Pierre structure le backlog
- Giovanni évalue maturité → Pierre planifie sprints

### Giovanni + Sarah (Product Strategist)
- Alignement architecture technique avec stratégie produit
- Priorisation improvements basée sur OKRs

### Giovanni + John (Product Manager)
- Intégration requirements techniques dans PRD
- Balance features vs. dette technique vs. conformité

## 📈 Niveaux de Maturité Expliqués

| Niveau | Description | Caractéristiques |
|--------|-------------|------------------|
| **2** | 🌱 **Fondation** | Conformité de base, processus manuels, awareness |
| **3** | 🌿 **Intermédiaire** | Implémentation processus, début automatisation |
| **4** | 🌳 **Avancé** | Automatisation complète, monitoring continu |
| **5** | 🏆 **Expert** | Optimisation, capacités prédictives |
| **6** | ⭐ **Excellence** | Pratiques de pointe, full automation |

## 🎯 Principes de Travail de Giovanni

1. **Assessment First** : Toujours évaluer avant de recommander
2. **Progressive Path** : Ne pas sauter de niveaux
3. **Requirement-Driven** : Références précises par IDs
4. **Pragmatic Balance** : Équilibre conformité / pragmatisme
5. **Cross-Domain** : Impacts entre domaines
6. **Continuous Improvement** : Revues régulières
7. **Documentation** : Traçabilité complète

## 📁 Structure des Fichiers

```
src/bmm/
├── agents/
│   └── adeo-technical-lead.agent.yaml         # Configuration Giovanni
├── workflows/
│   └── adeo/
│       ├── global-ready-assessment/           # [GRA]
│       ├── global-ready-improve/              # [GRI]
│       ├── apization-guide/                   # [API]
│       ├── data-management/                   # [DAT]
│       ├── data-compliance-guide/             # [DCO]
│       ├── dev-factory-guide/                 # [DFA]
│       ├── operations-guide/                  # [OPS]
│       ├── quality-guide/                     # [QUA]
│       ├── security-guide/                    # [SEC]
│       ├── debt-management/                   # [DBT]
│       └── global-ready-help/                 # [GRH]
└── data/
    └── 2026-Global-Ready-Requirements.csv     # Source de vérité
```

## 🚀 Prochaines Étapes

1. **Testez Giovanni** : Lancez un assessment sur votre produit
2. **Intégrez les workflows** : Créez les fichiers workflow manquants
3. **Collaborez avec Pierre** : Transformez les improvements en Epics/Stories
4. **Suivez la progression** : Établissez des KPIs de maturité
5. **Partagez les learnings** : Documentez vos best practices

---

**Giovanni est prêt à vous guider vers l'excellence technique ADEO !** 💻🚀

Pour commencer : `Giovanni, aide-moi !`
