# Industry Lifecycle

> **Core Value**: Determine which evolutionary stage an industry is in — different stages demand different strategic approaches
>
> **Source**: Raymond Vernon (Product Life Cycle) → extended to the industry level
>
> **One-liner**: Entering during the growth phase vs. entering during decline requires entirely different strategies — identify the stage first, then set the strategy

---

## Overview

The Industry Lifecycle framework describes how industries evolve from birth to decline, serving as a foundational tool for judging development stages and forecasting future trends.

**Core Design Principles**:
- **Phased Evolution**: Industries pass through Introduction → Growth → Maturity → Decline
- **Stage Characteristics**: Each stage has unique competitive dynamics, profit models, and key success factors
- **Strategy Fit**: Different stages require different competitive strategies

**Best Use Cases**:
- Industry development stage assessment
- Market entry timing evaluation
- Competitive strategy selection
- Investment timing decisions

**Output Value**:
- Lifecycle stage determination
- Stage-characteristic matching analysis
- Evolutionary trend forecasts
- Strategy-fit recommendations

---

## Framework Overview

```
Market Size / Growth Rate
    ↑
    │          ╱╲
    │        ╱    ╲
    │      ╱  Growth  ╲        Maturity
    │    ╱              ╲──────────────╲
    │  ╱                                ╲  Decline
    │╱  Introduction                      ╲────────
    └──────────────────────────────────────────→ Time
```

---

## Four-Stage Characteristics

| Dimension | Introduction | Growth | Maturity | Decline |
|-----------|-------------|--------|----------|---------|
| **Market Growth** | Low / uncertain | High (>20%) | Slowing (<10%) | Negative |
| **Market Size** | Very small | Rapidly expanding | Large and stable | Shrinking |
| **Number of Competitors** | Few (pioneers) | Rapidly increasing | Consolidating | Few (survivors) |
| **Profit Levels** | Mostly losses | High profits | Margin compression | Low profits |
| **Customer Type** | Innovators / early adopters | Early majority | Late majority | Laggards |
| **Competitive Focus** | Product viability | Feature differentiation | Cost efficiency | Cost / exit |
| **Entry Barriers** | High technology barriers | Medium | High scale barriers | Not worth investing |
| **Key Success Factors** | Technical innovation | Speed of market acquisition | Operational efficiency / scale | Cash flow management |

---

## Execution Steps

### Step 1: Collect Stage-Assessment Indicators

The following data is needed to determine the industry stage:

| Indicator | Data Source | Assessment Use |
|-----------|-----------|----------------|
| Market size (past 3-5 years) | Industry reports / TAM estimates | Scale magnitude |
| Market growth rate (YoY) | Industry reports / statistics | Growth trend |
| Industry concentration (CR5/HHI) | Competitor data | Degree of competitive consolidation |
| Number / frequency of new entrants | Business registration databases | Entry intensity |
| Profit margins of leading firms | Financial reports / research reports | Profit headroom |
| Technology iteration frequency | Patent data / tech coverage | Technology maturity |
| User penetration rate | User data | Market saturation |

### Step 2: Stage Determination

Use a decision tree for quick positioning:

```
Market growth > 20%?
├── Yes → Does the market have a proven business model?
│        ├── Yes → Growth stage
│        └── No → Late Introduction / Early Growth
│
└── No → Market growth > 0%?
         ├── Yes → Is industry concentration increasing?
         │        ├── Yes → Maturity (consolidation phase)
         │        └── No → Maturity (stable phase)
         └── No → Decline
```

**Important Note**: Many industries are not uniformly in one stage. Distinguish between:
- **Overall industry** vs. **sub-segments** (some segments may be at different stages)
- **Domestic market** vs. **global market** (one may lag or lead the other)

### Step 3: Derive Strategic Implications

| Stage | Core Strategic Logic | Typical Strategies |
|-------|---------------------|-------------------|
| **Introduction** | Validate demand, iterate rapidly | Focus on core use cases, MVP validation, market education |
| **Growth** | Capture share, build moats | Rapid expansion, scaled customer acquisition, fundraising, ecosystem building |
| **Maturity** | Improve efficiency, differentiate | Cost optimization, deep sub-segment focus, M&A consolidation |
| **Decline** | Harvest or pivot | Cash flow management, strategic pivots, divestiture |

### Step 4: Identify Stage-Transition Signals

Identify leading indicators (with quantitative thresholds) for an industry about to enter the next stage:

| Transition | Leading Signals | Quantitative Thresholds | Assessment Method |
|------------|----------------|------------------------|-------------------|
| **Introduction → Growth** | Killer app emerges, policy support, major players enter | Penetration rate breaks 5-10%; YoY >30% for 2 consecutive quarters; 3+ companies raise Series A or above | Meet 2 of 3 criteria to confirm transition |
| **Growth → Maturity** | Growth inflection point, price wars, M&A wave | YoY drops >5pct quarter-over-quarter for 2 consecutive quarters (e.g., 25%→20%→15%); CR5 exceeds 60%; >3 M&A deals per year | Growth inflection is the most reliable signal; others serve as validation |
| **Maturity → Decline** | Substitutes emerge, user attrition, leaders pivot | Core MAU declines >3% QoQ for 2 consecutive quarters; substitute penetration >15%; leaders' non-core revenue >30% | User attrition is the earliest signal, typically leading financial indicators by 2-3 quarters |

**Precise Growth Inflection Detection**:
```
Focus on the rate of change of growth (acceleration), not the absolute rate:
- Accelerating growth (e.g., 20%→25%→30%) = Still in upper growth phase
- Flat growth (e.g., 25%→24%→25%) = Peak of growth stage, watch for transition
- Decelerating growth (e.g., 30%→22%→15%) = Transition has begun
- YoY drops >5pct QoQ for 2 consecutive quarters = Confirmed entry into maturity
```

---

## Output Format

```markdown
## Industry Lifecycle Analysis: [Industry Name]

### Stage Determination
**Current Stage**: [Growth / Maturity / ...]
**Supporting Evidence**:
- Market growth rate: [XX%] → [explanation]
- Industry concentration: CR5 = [XX%] → [explanation]
- User penetration rate: [XX%] → [explanation]
- New entrant trends: [description]

### Sub-Segment Differences (if applicable)
| Sub-Segment | Stage | Growth Rate | Notes |
|-------------|-------|-------------|-------|
| [Segment 1] | Growth | XX% | [notes] |
| [Segment 2] | Maturity | XX% | [notes] |

### Strategic Implications
The core strategic logic for this stage is: [...]
This specifically means:
1. [Implication 1]
2. [Implication 2]

### Stage Transition Signal Monitoring
| Signal | Current Status | Trigger Condition |
|--------|---------------|-------------------|
| [Signal 1] | [status] | [condition] |
| [Signal 2] | [status] | [condition] |
```

---

## Best Practices

### Data Source Recommendations

| Analysis Need | Recommended Data Sources |
|---------------|------------------------|
| Market size / growth | Brokerage industry research reports (iResearch, IDC, Frost & Sullivan), national statistics bureau industry data, industry association annual reports |
| Industry concentration | Public company financials (revenue comparisons), business registration data (registrations/cancellations), bidding data |
| User penetration | QuestMobile (internet industries), CNNIC reports, industry white papers |
| Technology maturity | Gartner Hype Cycle, patent searches (CNKI/Google Patents), academic publication trends |
| Investment activity | IT Juzi, PitchBook, 36Kr, Crunchbase |

### Industry Stage Assessment Cases

| Industry | Stage Assessment | Key Evidence | So What |
|----------|-----------------|-------------|---------|
| **New Energy Vehicles** | Growth → Maturity transition (2024) | YoY dropped from 96% in 2022 to ~25% in 2024; penetration exceeded 40%; intense price wars (BYD leading price cuts); CR5 >65% | Window has closed. New entrants should focus on niches (e.g., pickups, MPVs) rather than competing head-on in sedan/SUV main battlegrounds |
| **Online Education (K12)** | Policy-driven jump directly to Decline (2021) | "Double Reduction" policy changed industry structure overnight; leading companies (TAL/New Oriental) K12 revenue went to zero; massive workforce exodus | China-specific: Policy can skip natural lifecycle stages. Industry analysis must treat policy risk as the primary variable |
| **Live Commerce** | Late Growth stage (2024) | YoY still ~30% but decelerating (2022: 48%→2023: 35%→2024: ~28%); top streamer share dispersing; platform commission rates increasing | Deceleration signals evident. Expect maturity by 2025-2026. Entering now requires differentiated positioning (e.g., vertical-specific live streaming) |
| **Medical Aesthetics** | Stage stratification (2024) | Tier 1 cities: Maturity (penetration >20%, growth <10%, fierce price wars); Lower-tier markets: Growth (penetration <5%, growth >25%) | Classic "one industry, two stages." Strategy should be tailored by market tier |
| **AI Large Model Applications** | Late Introduction (2024) | Rapid tech iteration but unproven business models; heavy funding but very few profitable players; user penetration <10% (DAU/MAU basis) | Focus on scenario validation over scaling. Wait for "killer app" emergence signals |

---

### China Market Specifics

| Dimension | China Characteristics | Case |
|-----------|----------------------|------|
| Stage compression | Chinese market lifecycles are typically 30-50% shorter than Western markets (capital + population dividend acceleration); growth phase may last only 2-3 years | Community group buying went from boom to shakeout in just 2 years (2020-2022) |
| Policy-driven transitions | Policy can change industry stages in a short time, directly skipping or compressing certain phases | "Double Reduction" jumped education into decline; carbon neutrality accelerated NEV into growth |
| Lower-tier market extension | When Tier 1 markets enter maturity, lower-tier markets may still be in growth, creating "stage stratification" across the industry | Food delivery is saturated in Tier 1 but still penetrating in county-level cities; live commerce follows the same pattern |
| Frequent second curves | Chinese companies are more adept at restarting the lifecycle through "cross-industry expansion" | Meituan: group buying → delivery → in-store → travel; ByteDance: news → short video → e-commerce |

---

## Common Mistakes

| Mistake | Correct Approach |
|---------|-----------------|
| Equating industry growth rate with stage | Use multiple indicators comprehensively; growth rate is just one of them |
| Ignoring sub-segment stage differences | Assess each sub-segment separately |
| Assuming lifecycle is linear and irreversible | Technology breakthroughs can restart the lifecycle (e.g., AI restarting fintech) |
| Only determining stage without deriving implications | Must output "so what should be done" |

---

## Integration with Other Frameworks

| Partner Framework | Relationship |
|-------------------|-------------|
| PESTEL | T (Technology) and L (Legal) factors often drive stage transitions |
| TAM/SAM/SOM | Industry stage affects SAM/SOM growth assumptions |
| Five Forces | Competitive force intensities differ across stages |
| Three Horizons | H1/H2/H3 allocation depends on the industry's current stage |
| Disruption Theory | Industries in decline are more vulnerable to disruption |
