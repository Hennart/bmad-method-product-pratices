# BMAD Method - Agent Routing Rules

## 🎯 Mandatory Agent Consultation Policy

This document defines the mandatory routing rules to ensure proper agent consultation for their domains of expertise.

### Rule #1: Product Management → Pierre 🏢

**POLICY**: All Product Management questions MUST be routed to Pierre (ADEO Delivery Manager)

**Scope**:
- Product Lifecycle (6 phases, 5 Gates)
- ADEO Product Operating Model (7 dimensions)
- JIRA hierarchy (Initiative/Package/Epic/Story)
- 4 Product Dimensions (Valuable, Viable, Usable, Feasible)
- Backlog and roadmap management
- Business Terms and canonical glossary
- Product strategy and vision
- Gate validation processes

**Trigger Keywords**:
```
initiative, package, epic, story, gate, lifecycle, phase,
operating model, product ops, valuable, viable, usable, feasible,
backlog, roadmap, product strategy, product vision, business terms
```

**Action**: When any of these keywords are detected in a user query, the system MUST:
1. Alert the user that Pierre should be consulted
2. Provide context on why Pierre is the expert
3. Suggest invoking Pierre via: `@pierre <question>`

**Rationale**: Pierre possesses deep expertise in ADEO Product frameworks that cannot be replicated by generic knowledge. His structured approach ensures compliance with ADEO standards.

---

### Rule #2: Technical Excellence → Giovanni 💻

**POLICY**: All Technical Excellence and Global Ready questions MUST be routed to Giovanni (ADEO Technical Lead)

**Scope**:
- Global Ready framework (9 domains, 248 requirements)
- Technical maturity assessment (levels 2-6)
- Architecture and security best practices
- DevOps, CI/CD, quality standards
- API design and data management
- Finance domain compliance
- Technical debt tracking

**Trigger Keywords**:
```
global ready, technical standards, architecture, security, quality,
devops, ci/cd, api design, data compliance, finance compliance,
maturity level, technical debt, ESG, tax archiving
```

**Action**: When any of these keywords are detected in a user query, the system MUST:
1. Alert the user that Giovanni should be consulted
2. Provide context on Giovanni's Global Ready expertise
3. Suggest invoking Giovanni via: `@giovanni <question>`

**Rationale**: Giovanni is the authoritative source on Global Ready framework with access to 248 requirements across 9 domains. His expertise ensures technical compliance.

---

### Rule #3: Cross-Domain Collaboration

**POLICY**: For questions spanning both domains, BOTH agents must be consulted

**Scenarios requiring both agents**:
1. **Technical Roadmap Planning**
   - Pierre: Product lifecycle positioning, value prioritization
   - Giovanni: Technical feasibility, maturity assessment

2. **Gate #3 (Delivery) Validation**
   - Pierre: Gate process and validation criteria
   - Giovanni: Technical compliance checks (Global Ready)

3. **Product Architecture Decisions**
   - Pierre: Business value and viability
   - Giovanni: Technical standards and security

4. **Feature Prioritization with Technical Constraints**
   - Pierre: Product backlog and roadmap structure
   - Giovanni: Technical debt and feasibility assessment

**Action**: System must suggest consulting both agents in sequence:
```
Step 1: @pierre <product management aspect>
Step 2: @giovanni <technical aspect>
Step 3: Synthesize both perspectives
```

---

### Rule #4: Enforcement Mechanisms

**Implementation**:

1. **Pre-flight checks**: Before answering Product/Technical questions, verify if agent should be consulted
2. **Keyword detection**: Automated scanning of user queries for trigger keywords
3. **Warning messages**: Display clear warnings when agent consultation is recommended
4. **Workflow suggestions**: Propose relevant workflows ([CI], [CP], [CE], [CS], [GRA], [GRI])

**Warning Template**:
```
⚠️ AGENT CONSULTATION RECOMMENDED

This question involves [Product Management / Technical Excellence].
The expert agent for this domain is [Pierre 🏢 / Giovanni 💻].

Recommended action: @[pierre/giovanni] [your question]

Why? [Brief explanation of agent's expertise]
```

---

### Rule #5: Documentation Compliance

**POLICY**: All agent routing decisions must reference official documentation

**Required references**:
- Pierre: `src/bmm/agents/adeo-delivery-manager.agent.yaml`
- Giovanni: `src/bmm/agents/adeo-technical-lead.agent.yaml`
- Product Operating Model: `ADEO-PRODUCT-OPERATING-MODEL.md`
- Global Ready: `data/2026-Global-Ready-Requirements.csv`

**Action**: When recommending an agent, include a link to their documentation.

---

## 🔄 Review and Updates

- **Frequency**: Quarterly review of routing rules
- **Trigger**: When new agents are added or domains expand
- **Owner**: Product Practice team
- **Version**: 1.0 (March 10, 2026)

## 📊 Metrics

Track the following metrics to ensure rule effectiveness:
- % of Product Management queries routed to Pierre
- % of Technical Excellence queries routed to Giovanni
- User satisfaction with agent recommendations
- False positive/negative routing decisions

---

**Last Updated**: March 10, 2026
**Version**: 1.0
**Status**: Active
