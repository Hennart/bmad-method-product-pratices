# GitHub Copilot Instructions for BMAD Method - Product Practice

## 🤖 Agent Routing Rules

### Mandatory Agent Consultation

When working on topics related to the following domains, **ALWAYS** invoke the specified agent:

#### 📋 Product Management → **Pierre (ADEO Delivery Manager)** 🏢

**MANDATORY consultation for:**
- Product Lifecycle (6 phases: Strategy, Discovery, Delivery, Launch, Product Life, Sunset)
- Gate validations (Gates #1 through #5)
- ADEO Product Operating Model (7 dimensions)
- JIRA hierarchy (Initiative → Package → Epic → Story)
- Product dimensions (Valuable, Viable, Usable, Feasible)
- Backlog construction and prioritization
- Roadmap planning
- Business Terms and canonical glossary
- Product maturity assessment
- Go-to-Market strategy
- Product vision and strategy alignment

**Keywords that trigger Pierre:**
- "initiative", "package", "epic", "story"
- "gate", "lifecycle", "phase"
- "operating model", "product ops"
- "valuable", "viable", "usable", "feasible"
- "backlog", "roadmap"
- "product strategy", "product vision"
- "business terms", "glossary"

**How to invoke Pierre:**
```
@pierre [your question about product management]
```

#### 💻 Technical Excellence → **Giovanni (ADEO Technical Lead)** 💻

**MANDATORY consultation for:**
- Global Ready framework assessment
- Technical standards and architecture
- Security, Quality, DevOps best practices
- API design and data management
- Maturity levels (2-6) evaluation
- Technical debt management
- Finance domain (ESG, Tax, Accounting, Internal Control)

**Keywords that trigger Giovanni:**
- "global ready", "technical standards"
- "architecture", "security", "quality"
- "devops", "ci/cd", "api"
- "data compliance", "finance"
- "maturity level", "technical debt"

**How to invoke Giovanni:**
```
@giovanni [your question about technical excellence]
```

### 🎯 Priority Rules

1. **Product Management questions** → Pierre is PRIMARY expert
2. **Technical implementation** → Giovanni is PRIMARY expert
3. **Overlap scenarios** → Consult BOTH agents:
   - Technical roadmap planning (Pierre for lifecycle, Giovanni for technical feasibility)
   - Product architecture decisions (Pierre for business value, Giovanni for technical standards)
   - Gate #3 validation (Pierre for process, Giovanni for technical compliance)

### 🚫 Anti-patterns to Avoid

❌ **DON'T** answer Product Lifecycle questions without consulting Pierre
❌ **DON'T** create JIRA structure without Pierre's validation
❌ **DON'T** assess Global Ready maturity without consulting Giovanni
❌ **DON'T** skip agent consultation for their domain expertise

### ✅ Best Practices

✅ **DO** invoke Pierre for any Initiative/Package/Epic/Story creation
✅ **DO** consult Pierre before any Gate validation
✅ **DO** reference Pierre when discussing Product Operating Model
✅ **DO** invoke Giovanni for Global Ready assessments
✅ **DO** consult both agents when bridging product and technical domains

## 📚 Documentation References

- **Pierre's expertise**: `src/bmm/agents/adeo-delivery-manager.agent.yaml`
- **Giovanni's expertise**: `src/bmm/agents/adeo-technical-lead.agent.yaml`
- **Product Operating Model**: `ADEO-PRODUCT-OPERATING-MODEL.md`
- **Product Lifecycle**: `ADEO-PRODUCT-LIFECYCLE.md`
- **Global Ready**: `data/2026-Global-Ready-Requirements.csv`

## 🔄 Workflow Integration

When a user asks about:
- Creating product structure → Suggest Pierre's workflows: [CI], [CP], [CE], [CS]
- Technical assessment → Suggest Giovanni's workflows: [GRA], [GRI]
- Specific domains → Suggest domain workflows: [API], [DAT], [DCO], [DFA], [FIN], [OPS], [QUA], [SEC]

---

**Remember**: Pierre and Giovanni are domain experts with deep, specialized knowledge.
Always leverage their expertise rather than attempting to answer from general knowledge.
