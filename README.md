# Equity Risk Portfolio Analysis

## Project Overview

This project presents a historical risk and performance assessment of a hypothetical investment portfolio using Python-based financial analysis.

Historical market data covering January 2016 to July 2026 was collected for a combination of individual stocks, a broad equity market ETF, gold, and long-term U.S. Treasury bonds.

The project evaluates both individual assets and the overall portfolio using financial metrics including daily and annualised returns, volatility, correlation, covariance, beta, Sharpe ratio, drawdown, maximum drawdown, and Value at Risk (VaR).

A Power BI dashboard was also developed to communicate the major findings and provide a visual overview of portfolio performance and risk.


## Objectives

This project aims to:

- Examine the historical returns of the selected assets.
- Quantify asset risk through return volatility.
- Study diversification opportunities using correlation and covariance.
- Build a hypothetical multi-asset portfolio and analyse its behaviour.
- Determine the market exposure of individual assets using beta.
- Compare investments based on risk-adjusted returns using the Sharpe ratio.
- Measure the portfolio's downside risk through drawdown analysis.
- Calculate the portfolio's maximum observed drawdown.
- Estimate potential one-day losses using a 95% VaR measure.
- Develop a structured and reproducible Python-based analytical workflow.
- Communicate the analysis through a Power BI visualisation dashboard.


## Assets Analysed

The portfolio consists of the following securities and market instruments:

| Ticker | Asset |
|--------|-------|
| AAPL | Apple Inc. |
| JPM | JPMorgan Chase & Co. |
| JNJ | Johnson & Johnson |
| KO | The Coca-Cola Company |
| XOM | Exxon Mobil Corporation |
| SPY | SPDR S&P 500 ETF Trust |
| GLD | SPDR Gold Shares |
| TLT | iShares 20+ Year Treasury Bond ETF |


## Tools & Technologies

The analysis was implemented using a combination of Python-based data tools and business intelligence software:

- **Python 3.10.11** – Used to perform the financial analysis and build the data processing workflow.
- **pandas** – Used for handling financial time series, calculating returns, and generating analytical datasets.
- **NumPy** – Used for numerical and mathematical operations.
- **yfinance** – Used as the source for historical market price information.
- **Jupyter Notebook** – Used for exploratory analysis, calculations, and documenting the analysis process.
- **Git/GitHub** – Used to maintain project versions and track changes.
- **Microsoft Power BI** – Used to create the final portfolio risk and performance dashboard.
- **CSV files** – Used to store processed datasets and transfer analytical results into the visualisation layer.


## Dataset & Data Preparation

### Data Source

Market price data was obtained through the `yfinance` library in Python. The historical dataset spans **January 2016 to July 2026** and contains observations for eight selected financial instruments.

The assets included are:

- AAPL
- JPM
- JNJ
- KO
- XOM
- SPY
- GLD
- TLT

Adjusted closing prices were used as the basis for calculating historical returns.

### Data Processing

The raw market data was prepared using pandas before being used in the financial analysis. The workflow involved:

1. Retrieving historical price data for the selected assets.
2. Extracting the relevant adjusted closing prices.
3. Aligning the assets by trading date.
4. Reviewing the data for missing or inconsistent observations.
5. Converting price data into daily percentage returns.
6. Exporting the processed data into CSV files for use in the subsequent analysis stages.

Daily returns generated during this process served as the primary input for calculating asset performance, portfolio returns, correlations, beta, volatility, and other risk metrics.



## Methodology & Financial Metrics

The financial analysis was conducted using daily return data and progressed from individual asset analysis to portfolio-level performance and risk assessment.

### 1. Daily Return Calculation

Daily percentage returns were derived from consecutive adjusted closing prices:

$$
R_t = \frac{P_t}{P_{t-1}} - 1
$$

Here, \(P_t\) represents the current adjusted closing price and \(P_{t-1}\) represents the previous trading day's price.

Using returns rather than absolute prices makes it possible to compare assets with different price levels.

### 2. Annualized Performance

Historical returns were converted to an annualised measure to provide a common basis for comparing the performance of the selected assets.

### 3. Volatility

Return volatility was measured using the standard deviation of daily returns.

Annualised volatility was calculated using the standard square-root-of-time convention:

$$
\sigma_{\text{annual}} = \sigma_{\text{daily}}\sqrt{252}
$$

Higher volatility indicates greater historical variability in returns.

### 4. Correlation Analysis

Correlation was used to determine how closely the returns of different assets moved together.

The coefficient ranges between -1 and +1:

- A value close to +1 indicates strong positive co-movement.
- A value close to 0 indicates little linear relationship.
- A value close to -1 indicates strong negative co-movement.

The resulting correlation matrix was used to assess the diversification characteristics of the portfolio.

### 5. Covariance Analysis

Covariance measures the direction in which two asset returns tend to move relative to one another.

Positive covariance suggests similar movement, while negative covariance suggests opposite movement.

Covariance is important in portfolio risk analysis because relationships between assets influence total portfolio risk.

### 6. Portfolio Return

The portfolio return for each trading day was calculated using the weighted returns of the individual assets:

$$
R_p = \sum_{i=1}^{n} w_iR_i
$$

where \(w_i\) represents the assigned portfolio weight and \(R_i\) represents the return of the corresponding asset.

### 7. Beta Analysis

SPY was selected as the market benchmark for beta calculations.

Beta was calculated as:

$$
\beta_i =
\frac{\mathrm{Cov}(R_i,R_m)}
{\mathrm{Var}(R_m)}
$$

Beta indicates how sensitive an asset's returns are to movements in the selected market benchmark.

A beta above 1 indicates greater sensitivity than the benchmark, while a beta below 1 indicates lower sensitivity. A negative beta indicates an inverse relationship with the benchmark.

### 8. Sharpe Ratio

Risk-adjusted performance was evaluated using the Sharpe ratio:

$$
Sharpe =
\frac{R_p-R_f}{\sigma_p}
$$

The measure compares excess return with the volatility associated with achieving that return.

A higher Sharpe ratio generally indicates better risk-adjusted performance, as more excess return is generated per unit of volatility.

### 9. Portfolio Growth

A normalised portfolio value series was created by compounding the daily portfolio returns:

$$
V_t = V_{t-1}(1+R_t)
$$

The initial portfolio value was normalised to approximately 1, allowing portfolio growth and decline to be tracked consistently throughout the historical period.

### 10. Running Portfolio Peak

For each date, the running maximum records the highest portfolio value achieved up to that point:

$$
M_t = \max(V_1,V_2,\ldots,V_t)
$$

This series provides the reference required to measure declines from previous portfolio highs.

### 11. Drawdown Analysis

Portfolio drawdown was calculated as the percentage difference between the current portfolio value and its running maximum:

$$
D_t = \frac{V_t-M_t}{M_t}
$$

Negative drawdown values represent declines below previous portfolio peaks.

### 12. Maximum Drawdown

The minimum value in the drawdown series represents the portfolio's maximum drawdown.

The observed maximum drawdown was approximately:

**-26.9%**

This indicates that the portfolio experienced a peak-to-trough decline of roughly 26.9% during the historical period analysed.

### 13. Value at Risk

The analysis also included a 95% daily Value at Risk estimate.

The portfolio's estimated 95% daily VaR was approximately:

**-1%**

The result is expressed as a negative return/loss threshold in this analysis. In magnitude terms, this corresponds to approximately **1% of portfolio value**.

## Key Results & Findings

The historical analysis highlighted several differences in return, risk, market sensitivity, and diversification characteristics across the selected assets.

### Return Performance

AAPL delivered the strongest annualised return among the assets, at approximately **28.29%**.

The annualised return ranking was:

| Rank | Asset | Annualized Return |
|------|-------|------------------:|
| 1 | AAPL | 28.29% |
| 2 | JPM | 20.68% |
| 3 | SPY | 15.15% |
| 4 | GLD | 13.20% |
| 5 | JNJ | 12.32% |
| 6 | XOM | 11.46% |
| 7 | KO | 9.86% |
| 8 | TLT | -0.78% |

The strongest return was therefore associated with AAPL, although the asset also carried the highest historical volatility.

### Volatility

AAPL had annualised volatility of approximately **28.92%**, making it the most volatile asset in the dataset.

TLT recorded the lowest annualised volatility at approximately **14.75%**.

The results demonstrate that assets with stronger historical returns may also experience larger fluctuations, reinforcing the need to consider risk alongside return.

### Beta and Market Sensitivity

Beta was calculated relative to SPY.

AAPL had a beta of approximately **1.20**, while JPM had a beta of approximately **1.08**. These values indicate relatively high sensitivity to movements in the selected market benchmark.

TLT recorded a beta of approximately **-0.13**, suggesting a small inverse historical relationship with the benchmark.

### Correlation and Diversification

The correlation matrix demonstrated that the assets had different relationships with one another.

Some notable relationships included:

- AAPL and SPY: approximately **0.74**
- JPM and SPY: approximately **0.70**
- JPM and TLT: approximately **-0.31**
- SPY and TLT: approximately **-0.16**

The relatively strong positive correlations among several equity assets indicate that they can move together during market conditions, while TLT's negative relationships with several equity assets provide a contrasting return pattern.

### Portfolio Risk-Adjusted Performance

The portfolio generated a Sharpe ratio of approximately:

**1.22**

This indicates favourable historical risk-adjusted performance based on the return and volatility assumptions used in the analysis.

The individual asset comparison also placed AAPL at the top of the calculated Sharpe ranking.

### Drawdown

The portfolio's maximum drawdown was approximately:

**-26.9%**

This was the largest decline from a previous portfolio high during the analysed period.

Maximum drawdown provides a different perspective from volatility because it focuses specifically on the portfolio's most severe historical peak-to-trough decline.

### Value at Risk

The estimated 95% daily VaR was approximately:

**-1%**

Under the assumptions of the selected methodology, this represents a daily loss threshold that would be exceeded on approximately 5% of observations.

The VaR estimate was considered alongside maximum drawdown and volatility to provide a broader view of portfolio downside risk.

### Overall Finding

The results show that no single metric provides a complete assessment of an investment.

Although AAPL produced the highest historical return, it also exhibited the highest volatility. Assets such as TLT displayed lower volatility and different market relationships, contributing potential diversification characteristics.

At the portfolio level, the combination of assets produced a Sharpe ratio of approximately **1.22**, while the portfolio's maximum historical drawdown was approximately **-26.9%**.

These results illustrate the trade-off between return, volatility, diversification, and downside risk in portfolio construction.


## Power BI Dashboard

The project includes an interactive Power BI dashboard designed to communicate the main findings from the Python-based risk analysis.

The dashboard provides visualisations for:

- Asset returns
- Asset volatility
- Portfolio Sharpe ratio
- Maximum drawdown
- Value at Risk
- Beta and market sensitivity
- Correlation between assets
- Portfolio drawdown behaviour
- Comparative asset performance

The Power BI report can be found under the following project directory:

```text
powerbi/equity_risk_dashboard.pbix
```

## Project Structure

The project follows a modular directory structure that separates data, analytical notebooks, reusable code, and visualisation resources.

```text
Equity-Risk-Portfolio-Analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_return_analysis.ipynb
│   ├── 03_risk_metrics.ipynb
│   ├── 04_downside_risk.ipynb
│   ├── 05_risk_adjusted_performance.ipynb
│   └── 06_dashboard_data.ipynb
│
├── src/
│   └── data_loader.py
│
├── powerbi/
│   └── equity_risk_dashboard.pbix
│
├── README.md
├── requirements.txt
└── .gitignore
```

## How to run the project

The project can be reproduced locally using the Python environment and notebooks included in the repository.

### 1. Clone the Repository

Clone the GitHub repository and move into the project directory:

```bash
git clone https://github.com/sahitiputcha/Equity-Risk-Portfolio-Analysis
cd Equity-Risk-Portfolio-Analysis
```
### 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Select the Python Environment

When working with the Jupyter notebooks in VS Code, select the project's `.venv` Python environment as the notebook kernel.

### 5. Run the Analysis

Open the notebooks in the `notebooks/` directory and execute them in the following order:

1. `01_data_collection.ipynb` – Collect and prepare historical market data.
2. `02_return_analysis.ipynb` – Calculate and analyse asset returns.
3. `03_risk_metrics.ipynb` – Calculate asset-level and portfolio risk metrics.
4. `04_downside_risk.ipynb` – Analyze portfolio drawdown and downside risk.
5. `05_risk_adjusted_performance.ipynb` – Evaluate risk-adjusted portfolio performance.
6. `06_dashboard_data.ipynb` – Prepare the final datasets used by the Power BI dashboard.

The notebooks follow this general workflow:

```text
Data Collection
      ↓
Data Preparation
      ↓
Return Calculation
      ↓
Asset Analysis
      ↓
Portfolio Construction
      ↓
Risk Analysis
      ↓
Dashboard Data Preparation
```

### 6. Generated Data

The analysis produces processed datasets in:

```text
data/processed/
```

These datasets contain the outputs required for subsequent analysis and visualisation.

### 7. Power BI Dashboard

After generating the required processed datasets, the Power BI report can be opened from:

```text
powerbi/equity_risk_dashboard.pbix
```

## Limitations & Assumptions

Several considerations should be taken into account when interpreting the results:

- The analysis relies on historical observations, which may not represent future market behaviour.
- The portfolio used in this study is hypothetical and is intended for analytical purposes rather than actual investment management.
- The selected sample covers January 2016 to July 2026, meaning the results reflect the market environments occurring within this particular period.
- Historical volatility captures return variability but does not represent all possible dimensions of financial risk.
- Asset correlations are not constant and can change significantly during periods of market stress.
- Beta estimates depend on the choice of market benchmark; SPY was used as the benchmark in this analysis.
- Sharpe ratio results depend on the return, volatility, and risk-free-rate assumptions used in the calculation.
- VaR provides a statistical estimate of potential losses and should not be interpreted as a guaranteed maximum loss.
- Maximum drawdown reflects the worst historical peak-to-trough decline and does not establish a limit for future losses.
- Trading costs, taxes, commissions, bid-ask spreads, and market liquidity were not incorporated into the analysis.
- The analysis does not incorporate individual investor preferences, investment objectives, or portfolio constraints.


## Future Improvements

Several extensions could be added to build upon the current framework:

- Introduce Expected Shortfall to provide additional information about extreme portfolio losses.
- Analyse rolling measures of volatility and beta to identify changes in risk and market exposure over time.
- Develop historical stress-testing and scenario-analysis capabilities.
- Add Monte Carlo simulations for probabilistic portfolio risk assessment.
- Explore optimisation techniques for determining alternative portfolio allocations.
- Develop an efficient frontier to compare potential portfolios based on expected return and risk.
- Expand the analysis to include additional asset classes and alternative investments.
- Account for practical considerations such as transaction costs, taxes, and liquidity.
- Automate data retrieval and dashboard data generation for more frequent portfolio updates.

## Conclusion

The completed framework provides a structured approach to analysing historical portfolio performance and risk using Python and Power BI.

Beginning with historical market prices, the project transforms the data into daily returns and applies a series of financial risk and performance measures, including volatility, correlation, beta, Sharpe ratio, drawdown, and Value at Risk.

The analysis demonstrates that evaluating an investment requires more than comparing returns. AAPL achieved the strongest historical return in the selected dataset but also exhibited the greatest volatility, while TLT showed lower volatility and distinct relationships with equity assets.

The hypothetical portfolio achieved a Sharpe ratio of approximately **1.22** and experienced a maximum historical drawdown of approximately **-26.9%**.

The project therefore demonstrates how quantitative financial analysis and business intelligence visualisation can be combined to evaluate portfolio characteristics in a reproducible and interpretable manner.

