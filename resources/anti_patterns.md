# Anti-Pattern Firewall

> **Role in quality system**: Self-check tool -- standard library of known error patterns (execution manual for the "Error Pattern Detector" reviewer role)
> **Purpose**: Identify and avoid common error patterns in business analysis
>
> **Scope boundaries**:
> - This file = "what not to do" (error pattern identification + firewall)
> - `judgment_rules.md` = "how to judge" (8 rules, Insight generation process)
> - `report_standards.md` = "how to write" (report structure, language, format standards)
>
> **Loading timing**: Loaded at Stage 5 start (as background constraints for Rules 1-7, not as an independent execution step); loaded during Stage 6 report generation (using the self-check checklist below)

---

## Anti-Pattern Checklist (10 patterns to avoid)

---

## Anti-Pattern 1: Correct but Useless Truisms

**Symptoms**:
- Conclusions are correct but contain no information
- Universally applicable to any situation
- Cannot guide specific actions

**Examples**:
```
❌ "Open-source models are changing the industry landscape"
✅ "In 2025, open-source models caught up with closed-source models on key benchmarks, with the gap narrowing from 17.5% to 0.3%"

❌ "Companies need to choose the right strategy"
✅ "Companies with ecosystem operation capabilities should accelerate open-sourcing; otherwise, proceed with caution"
```

**Detection method**:
- Replace the subject with another industry -- does it still hold true?
- Can this statement tell a decision-maker exactly what to do?

---

## Anti-Pattern 2: Data Dumping Without Insights

**Symptoms**:
- Lists large amounts of data
- No "So What"
- Reader doesn't know what it means

**Examples**:
```
❌ "Qwen has 600 million downloads, 170K derivative models, Alibaba Cloud revenue grew 34%..."
✅ "Qwen's 600 million downloads -> ecosystem effect has formed -> recommend following the open-source strategy"
```

**Detection method**:
- Does every data point have a "So What" interpretation?
- What action recommendations can the reader derive from the data?

---

## Anti-Pattern 3: Ignoring Counter-Evidence

**Symptoms**:
- Only collects evidence supporting the hypothesis
- Ignores/downplays contradictory evidence
- One-sided conclusions

**Examples**:
```
❌ Only emphasizing open-source success stories, ignoring Meta Llama team upheaval
✅ Analyzing both open-source successes and obstacles, providing balanced judgment
```

**Detection method**:
- Was counter-evidence actively sought?
- Was counter-evidence discussed thoroughly?

---

## Anti-Pattern 4: Disconnected from User Context

**Symptoms**:
- Generic template-style report
- Fails to answer "Relevance to Us"
- Recommendations cannot be applied to the user's scenario

**Examples**:
```
❌ "Companies should consider an open-source strategy" (unspecified which type of company)
✅ "As a major tech company that has released large models, you should assess: 1) Ecosystem capability 2) Commercialization progress 3) Competitive position"
```

**Detection method**:
- Replace "companies" in the report with a specific company name -- does it still read well?
- Do the recommendations consider the user's specific constraints?

---

## Anti-Pattern 5: Causal Confusion

**Symptoms**:
- Treating correlation as causation
- Ignoring third variables
- Reversing causal direction

**Examples**:
```
❌ "Open-sourcing leads to success" (ignoring the selection bias that successful companies are more likely to open-source)
✅ "Open-sourcing is one strategy of successful companies; the causal relationship requires careful evaluation"
```

**Detection method**:
- Are there alternative explanations?
- Is the causal mechanism clear?

---

## Anti-Pattern 6: Static Analysis

**Symptoms**:
- Ignoring dynamic changes
- Assuming the current state persists
- Not considering competitive responses

**Examples**:
```
❌ "Open-source models have caught up, so we should open-source"
✅ "Open-source models have caught up, but consider: 1) Closed-source model counterattack 2) Technology iteration speed 3) Window of opportunity"
```

**Detection method**:
- Does the analysis consider the time dimension?
- Does it consider competitors' responses?

---

## Anti-Pattern 7: False Precision

**Symptoms**:
- Providing precise numbers from unreliable sources
- Over-quantifying vague concepts
- Using precision to mask uncertainty

**Examples**:
```
❌ "Open-sourcing will bring 37.5% revenue growth" (no basis)
✅ "Open-sourcing may bring significant revenue growth, referencing Alibaba Cloud AI revenue +34%"
```

**Detection method**:
- Is the data source reliable?
- Is uncertainty annotated?

---

## Anti-Pattern 8: Non-Actionable Recommendations

**Symptoms**:
- Recommendations too abstract
- Lacking resource/time constraints
- No clear responsible party

**Examples**:
```
❌ "Strengthen ecosystem development"
✅ "Invest 5 million by Q2 to build a 10-person community operations team, targeting 100K developers"
```

**Detection method**:
- Do recommendations include specific actions, responsible parties, and timeframes?
- Does the user know what to do tomorrow after receiving the recommendation?

---

## Anti-Pattern 9: Framework Abuse

**Symptoms**:
- Using Frameworks for the sake of using them
- Frameworks disconnected from analysis
- Forced application

**Examples**:
```
❌ Forcing all six PESTEL dimensions, discussing each superficially
✅ Using only the 2-3 dimensions most relevant to the problem, analyzing in depth
```

**Detection method**:
- Does the Framework serve the analytical purpose?
- If you remove the Framework name, does the analysis still hold?

---

## Anti-Pattern 10: Ignoring Implementation Barriers

**Symptoms**:
- Only discussing "what should be done"
- Not discussing "how to achieve it"
- Ignoring organizational resistance

**Examples**:
```
❌ "Should open-source the large model"
✅ "Should open-source the large model, but need to overcome: 1) Technical team resistance 2) Commercialization uncertainty 3) Risk of competitor exploitation"
```

**Detection method**:
- Are implementation barriers discussed?
- Are there specific recommendations for overcoming barriers?

---

## Report Self-Check Checklist (for Stage 6)

> Stage 5 Insight generation self-checks are covered by the eight rules in `judgment_rules.md`.

**Stage 6 Report Generation Self-Check**:
- [ ] No "correct but useless truisms"
- [ ] Every data point has a "So What" interpretation
- [ ] Recommendations are specific and actionable (action/responsible party/timeline)
- [ ] Anchored to user context
- [ ] Implementation barriers are discussed
