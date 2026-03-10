# [GRA] Global Ready Assessment

## Workflow Purpose
Assess the maturity level of a digital product across all 8 ADEO Global Ready domains and identify gaps and improvement opportunities.

## Input Required
- Product name and description
- Current technical stack (languages, frameworks, infrastructure)
- Team composition (roles available)
- Current practices and processes (if known)

## Assessment Process

### Step 1: Product Context
Gather information about:
- Product type (web, mobile, API, data platform, etc.)
- Business criticality (critical, important, standard)
- User base size and type (internal, external, B2B, B2C)
- Compliance requirements (GDPR, specific BU needs)

### Step 2: Domain-by-Domain Assessment

For each of the 8 domains, evaluate current maturity level (2-6):

#### 1. 🔌 APIzation
**Questions:**
- Do you expose APIs? If yes, are they documented?
- Are APIs published in a centralized platform?
- Do you follow API design guidelines (REST, versioning)?
- How do you manage API performance and changes?

**Assessment:** Determine level (2-6) based on responses

#### 2. 📊 Data
**Questions:**
- Do you have identified data owners and stewards?
- Is your data model documented and semantically defined?
- How do you manage data quality?
- Do you provide data to other systems/products?

**Assessment:** Determine level (2-6) for each sub-topic

#### 3. 🔐 Data Compliance
**Questions:**
- Do you process personal data (GDPR)?
- How do you manage data retention and deletion?
- Do you have consent management in place?
- How do you handle data subject rights (access, deletion)?

**Assessment:** Determine level (2-6) and identify NA requirements

#### 4. 🏭 Dev Factory
**Questions:**
- How is your source code managed (Git, branching strategy)?
- Do you have CI/CD pipelines?
- Are your releases automated?
- How do you manage artifacts and deployments?

**Assessment:** Evaluate CI, CD, and Deployment maturity

#### 5. ⚙️ Operations
**Questions:**
- How do you manage changes (ITSM, CAB)?
- Do you track cloud costs (FinOps)?
- Where is your product hosted (cloud, on-prem)?
- How do you handle incidents?
- What observability tools do you use?
- Do you have SLOs defined?
- How do you ensure reliability (backup, DRP)?

**Assessment:** Evaluate each sub-topic (Change, FinOps, Hosting, Incidents, Observability, Reliability)

#### 6. 📦 Product Management
**Questions:**
- Do you track technical debt?
- How do you measure and reduce debt?
- Do you have a debt reduction strategy?

**Assessment:** Determine debt management maturity

#### 7. ✅ Quality
**Questions:**
- What types of tests do you have (unit, integration, e2e)?
- Are tests automated?
- Do you have quality gates in your CI/CD?
- How do you manage test coverage?
- Do you have acceptance criteria defined?

**Assessment:** Evaluate Delivery, Implementation, and Management

#### 8. 🔒 Security
**Questions:**
- Do you use security scanners (SAST, DAST)?
- How do you manage vulnerabilities?
- How is identity and access managed (IAM)?
- Do you enforce MFA?
- How is your infrastructure secured?
- Do you have a risk matrix?

**Assessment:** Evaluate Application, IAM, Infrastructure, and Risk maturity

### Step 3: Gap Analysis

For each domain:
1. **Current Level**: X
2. **Target Level**: Y (based on product criticality and business needs)
3. **Gap**: Y - X levels to improve
4. **Missing Requirements**: List specific requirement IDs not met

### Step 4: Prioritization Matrix

Create prioritization based on:
- **Business Impact**: Critical, High, Medium, Low
- **Security Risk**: Critical, High, Medium, Low
- **Effort**: High, Medium, Low
- **Dependencies**: Blocking other improvements?

### Step 5: Improvement Roadmap

Generate a phased roadmap:

**Phase 1 (0-3 months)**: Critical gaps, quick wins
- List specific requirements to implement
- Estimated effort per requirement

**Phase 2 (3-6 months)**: High-impact improvements
- List requirements
- Dependencies and prerequisites

**Phase 3 (6-12 months)**: Advanced maturity
- List requirements for higher maturity levels

## Output Format

### Executive Summary
```
Product: [Name]
Overall Maturity: [Average across domains]
Critical Gaps: [Number]
High Priority Actions: [Number]

Maturity Distribution:
- APIzation: Level X/6
- Data: Level X/6
- Data Compliance: Level X/6
- Dev Factory: Level X/6
- Operations: Level X/6
- Product Management: Level X/6
- Quality: Level X/6
- Security: Level X/6
```

### Detailed Assessment by Domain
For each domain, provide:
- Current maturity level
- Specific requirements met (with IDs)
- Specific requirements not met (with IDs)
- Recommended next level requirements
- Estimated effort

### Action Plan
Prioritized list of actions with:
- Requirement ID
- Requirement description
- Current gap
- Priority (Critical/High/Medium/Low)
- Estimated effort (days/weeks)
- Dependencies
- Owner/Responsible team

### Tracking Dashboard
Suggest KPIs to track:
- Number of requirements met per domain
- Overall maturity score
- Improvement velocity (requirements/month)
- Critical gaps remaining

## Follow-up Actions

1. **Review with team**: Present assessment results
2. **Validate priorities**: Adjust based on team feedback
3. **Plan sprints**: Integrate improvements in backlog
4. **Track progress**: Regular review (monthly/quarterly)
5. **Re-assess**: Full assessment every 6 months

## Integration with Other Workflows

- Use **[GRI] Global Ready Improve** to create detailed action plans for specific domains
- Use **[API]**, **[DAT]**, **[SEC]**, etc. for domain-specific guidance
- Link to **[CI] Create Initiative** (Pierre) to create improvement initiatives in JIRA
- Link to **[BK] Build Backlog** (Pierre) to integrate improvements in product backlog

---

**Ready to start your Global Ready Assessment? Let's go!** 🎯
