# Research on Local Government Financing Vehicles (LGFVs) in China

## Project Structure
```
.
├── data/               # Data folder
│   ├── raw/           # Raw data
│   └── processed/     # Processed data
├── code/              # Code folder
│   ├── data_cleaning/ # Data cleaning scripts
│   ├── analysis/      # Analysis scripts
│   └── visualization/ # Visualization scripts
├── results/           # Results output
│   ├── tables/       # Table results
│   └── figures/      # Figure results
└── docs/             # Documentation
```

## Research Design
This project employs a Triple-Differences (DDD) method to study the impact of China's 2014 State Council Document No. 43 on Local Government Financing Vehicles (LGFVs).

### Data Description
1. Main Data Sources:
   - WIND Database (2010-2024)
     - 2,330 LGFVs across 447 cities
     - 14,297 bond issuances and yield spreads
   - State Administration for Market Regulation
     - 43,647 subsidiaries controlled by LGFVs
   - CEIC Database
     - GDP, local land revenues, fiscal revenues

2. Key Variables:
   - Treatment: Post-2014 policy shock
   - Sensitivity Measure: Pre-2014 reliance on land collateral
   - Outcomes:
     - Bond issuance volume and terms
     - Credit ratings
     - Financial indicators (ROA, EBIT, cash flows)
   - Control Variables:
     - GDP
     - Local fiscal revenues
     - Land transfer revenues
     - Regional characteristics

### Empirical Strategy
1. Triple-Differences (DDD) Design:
   - Time: Pre vs. Post 2014
   - Treatment: High vs. Low sensitivity LGFVs
   - Region: Coastal vs. Inland provinces

2. Identification Strategy:
   - Exploit cross-sectional heterogeneity in LGFVs' pre-policy sensitivity
   - High-sensitivity group: Heavy reliance on land collateral
   - Low-sensitivity group: Diversified revenue structure

3. Key Hypotheses:
   - H1: Post-2014 equity restructuring improved LGFVs' credit profiles
   - H2: High-sensitivity LGFVs undertook more significant restructuring
   - H3: Restructuring led to enhanced bond market capacity

4. Robustness Checks:
   - Parallel trends test
   - Placebo tests
   - Alternative sensitivity measures
   - Heterogeneity analysis by region and size

### Mechanism Analysis
1. Equity Structure Changes:
   - M&A with high-performing SOEs
   - Asset quality improvements
   - Revenue stream diversification

2. Credit Profile Enhancement:
   - Total assets growth
   - ROA improvements
   - Cash flow stability

3. Bond Market Impact:
   - Interest rate spread reduction
   - Maturity extension
   - Issuance volume increase
