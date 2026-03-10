# GitHub Copilot Instructions for BMAD Method - Product Practice

## 🤖 Agent Routing Rules

### Mandatory Agent Consultation

When working on topics related to the following domains, **ALWAYS** invoke the specified agent:

#### 📋 Product Management → **Euclid (ADEO Delivery Manager)** 🏢

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

**Keywords that trigger Euclid:**
- "initiative", "package", "epic", "story"
- "gate", "lifecycle", "phase"
- "operating model", "product ops"
- "valuable", "viable", "usable", "feasible"
- "backlog", "roadmap"
- "product strategy", "product vision"
- "business terms", "glossary"

**How to invoke Euclid:**
```
@euclid [your question about product management]
```

#### 💻 Technical Excellence → **Ava (ADEO Technical Lead)** 💻

**MANDATORY consultation for:**
- Global Ready framework assessment
- Technical standards and architecture
- Security, Quality, DevOps best practices
- API design and data management
- Maturity levels (2-6) evaluation
- Technical debt management
- Finance domain (ESG, Tax, Accounting, Internal Control)

**Keywords that trigger Ava:**
- "global ready", "technical standards"
- "architecture", "security", "quality"
- "devops", "ci/cd", "api"
- "data compliance", "finance"
- "maturity level", "technical debt"

**How to invoke Ava:**
```
@ava [your question about technical excellence]
```

### 🎯 Priority Rules

1. **Product Management questions** → Euclid is PRIMARY expert
2. **Technical implementation** → Ava is PRIMARY expert
3. **Overlap scenarios** → Consult BOTH agents:
   - Technical roadmap planning (Euclid for lifecycle, Ava for technical feasibility)
   - Product architecture decisions (Euclid for business value, Ava for technical standards)
   - Gate #3 validation (Euclid for process, Ava for technical compliance)

### 🚫 Anti-patterns to Avoid

❌ **DON'T** answer Product Lifecycle questions without consulting Euclid
❌ **DON'T** create JIRA structure without Euclid's validation
❌ **DON'T** assess Global Ready maturity without consulting Ava
❌ **DON'T** skip agent consultation for their domain expertise

### ✅ Best Practices

✅ **DO** invoke Euclid for any Initiative/Package/Epic/Story creation
✅ **DO** consult Euclid before any Gate validation
✅ **DO** reference Euclid when discussing Product Operating Model
✅ **DO** invoke Ava for Global Ready assessments
✅ **DO** consult both agents when bridging product and technical domains

## 📚 Documentation References

- **Euclid's expertise**: `src/bmm/agents/adeo-delivery-manager.agent.yaml`
- **Ava's expertise**: `src/bmm/agents/adeo-technical-lead.agent.yaml`
- **Product Operating Model**: `ADEO-PRODUCT-OPERATING-MODEL.md`
- **Product Lifecycle**: `ADEO-PRODUCT-LIFECYCLE.md`
- **Global Ready**: `data/2026-Global-Ready-Requirements.csv`

## 🔄 Workflow Integration

When a user asks about:
- Creating product structure → Suggest Euclid's workflows: [CI], [CP], [CE], [CS]
- Technical assessment → Suggest Ava's workflows: [GRA], [GRI]
- Specific domains → Suggest domain workflows: [API], [DAT], [DCO], [DFA], [FIN], [OPS], [QUA], [SEC]

---

**Remember**: Euclid and Ava are domain experts with deep, specialized knowledge.
Always leverage their expertise rather than attempting to answer from general knowledge.
