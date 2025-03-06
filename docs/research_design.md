# Research Design: Impact of 2014 Policy on LGFVs

## 1. Research Context

### 1.1 Policy Background
- **Policy Shock**: 2014 State Council Document No. 43
- **Timing**: Nationwide implementation in 2014
- **Key Provisions**: 
  - Curbing implicit government guarantees
  - Restricting land-based finance
  - Promoting market-based financing

### 1.2 Research Question
How did LGFVs adapt to the 2014 policy changes through equity restructuring, and what were the implications for their credit profiles and bond market access?

## 2. Empirical Strategy

### 2.1 Triple-Differences (DDD) Design
The study employs a triple-differences approach to identify the causal effect of the 2014 policy on LGFV behavior:

1. **Time Dimension**: Pre vs. Post 2014
2. **Treatment Dimension**: High vs. Low sensitivity LGFVs
3. **Regional Dimension**: Coastal vs. Inland provinces

### 2.2 Identification Strategy
- **Treatment Group**: High-sensitivity LGFVs
  - Heavy reliance on land collateral pre-2014
  - Limited revenue diversification
  - Strong dependence on implicit guarantees

- **Control Group**: Low-sensitivity LGFVs
  - Already diversified revenue structure
  - Lower reliance on land collateral
  - More market-oriented operations

### 2.3 Key Variables

#### Treatment Variables
- **Policy Shock**: Post-2014 indicator
- **Sensitivity Measure**: 
  - Pre-2014 land collateral ratio
  - Revenue concentration index
  - Government guarantee reliance

#### Outcome Variables
1. **Equity Structure Changes**:
   - Number of new subsidiaries
   - M&A transaction value
   - Shareholding structure changes

2. **Financial Performance**:
   - Total assets growth
   - ROA
   - EBIT margin
   - Cash flow stability

3. **Bond Market Access**:
   - Issuance volume
   - Yield spread
   - Maturity structure
   - Credit rating changes

#### Control Variables
1. **Firm-level**:
   - Size
   - Age
   - Industry composition
   - Pre-policy performance

2. **Regional-level**:
   - GDP growth
   - Fiscal revenue
   - Land transfer revenue
   - Financial development

3. **Time-varying**:
   - Macroeconomic conditions
   - Policy environment
   - Market conditions

## 3. Data Sources

### 3.1 Primary Data
1. **WIND Database** (2010-2024):
   - 2,330 LGFVs across 447 cities
   - 14,297 bond issuances
   - Financial statements
   - Credit ratings

2. **State Administration for Market Regulation**:
   - 43,647 subsidiaries
   - Shareholding structure
   - M&A records

3. **CEIC Database**:
   - Regional economic indicators
   - Fiscal data
   - Land transaction data

### 3.2 Data Processing
1. **Matching Strategy**:
   - Firm-level matching based on pre-policy characteristics
   - Regional matching for coastal-inland comparison

2. **Variable Construction**:
   - Sensitivity index
   - Performance metrics
   - Market access indicators

## 4. Empirical Specifications

### 4.1 Main Specification
\[ Y_{ijt} = \alpha + \beta_1 Post_t + \beta_2 HighSens_i + \beta_3 Coastal_j + \beta_4 (Post_t \times HighSens_i) + \beta_5 (Post_t \times Coastal_j) + \beta_6 (HighSens_i \times Coastal_j) + \beta_7 (Post_t \times HighSens_i \times Coastal_j) + \gamma X_{ijt} + \delta_i + \theta_j + \lambda_t + \epsilon_{ijt} \]

Where:
- \(Y_{ijt}\): Outcome variable for LGFV i in region j at time t
- \(Post_t\): Post-2014 indicator
- \(HighSens_i\): High sensitivity indicator
- \(Coastal_j\): Coastal region indicator
- \(X_{ijt}\): Control variables
- \(\delta_i, \theta_j, \lambda_t\): Fixed effects

### 4.2 Event Study
- Pre-trend analysis
- Dynamic treatment effects
- Placebo tests

## 5. Robustness Checks

### 5.1 Identification Assumptions
1. **Parallel Trends**:
   - Pre-policy trend analysis
   - Placebo tests using alternative dates
   - Falsification tests

2. **Selection Bias**:
   - Propensity score matching
   - Heckman selection model
   - Instrumental variables

### 5.2 Alternative Specifications
1. **Different Sensitivity Measures**:
   - Alternative land reliance metrics
   - Revenue concentration indices
   - Government support proxies

2. **Sample Restrictions**:
   - Size-based subsamples
   - Regional subsamples
   - Time period variations

## 6. Mechanism Analysis

### 6.1 Transmission Channels
1. **Equity Structure Changes**:
   - M&A patterns
   - Asset quality improvements
   - Revenue diversification

2. **Credit Profile Enhancement**:
   - Financial performance
   - Risk metrics
   - Market perception

3. **Bond Market Impact**:
   - Pricing effects
   - Access expansion
   - Terms improvement

### 6.2 Heterogeneity Analysis
1. **Regional Differences**:
   - Coastal vs. Inland
   - Developed vs. Developing
   - Resource-rich vs. Resource-poor

2. **Firm Characteristics**:
   - Size effects
   - Age effects
   - Industry composition

## 7. Expected Results

### 7.1 Main Findings
1. **Treatment Effects**:
   - Significant restructuring among high-sensitivity LGFVs
   - Improved credit profiles
   - Enhanced bond market access

2. **Heterogeneity**:
   - Stronger effects in coastal regions
   - Variation by firm size and age
   - Industry-specific patterns

### 7.2 Policy Implications
1. **Regulatory Impact**:
   - Effectiveness of policy measures
   - Unintended consequences
   - Risk mitigation strategies

2. **Market Development**:
   - Bond market evolution
   - Credit rating effectiveness
   - Market discipline 