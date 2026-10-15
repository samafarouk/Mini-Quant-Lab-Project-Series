# Urbanization Regression: OLS Estimation & Time-Series Diagnostics

**An applied econometrics project using EViews to investigate the relationship between urbanization and selected economic and demographic variables.**

![Status](https://img.shields.io/badge/Status-In%20Progress-orange)
![Methods](https://img.shields.io/badge/Methods-OLS%20%7C%20ADF%20%7C%20Diagnostics-blue)
![Software](https://img.shields.io/badge/Software-EViews-2E8B57)

## Overview

This project applies introductory econometric methods to annual time-series data covering **1991–2025**, with 35 observations in the initial regression.

The analysis examines the relationship between urbanization and selected explanatory variables using Ordinary Least Squares (OLS). It then evaluates key regression diagnostics, including heteroscedasticity, residual normality, and stationarity.

The project also investigates an important empirical question: **Can a regression with an exceptionally high \(R^2\) provide misleading conclusions when its time-series properties have not been adequately examined?**

Rather than treating statistical significance as sufficient evidence of a reliable economic relationship, this project emphasizes diagnostic testing, critical interpretation, and appropriate model specification.

## Research Objectives

- Estimate an OLS regression relating urbanization to selected explanatory variables.
- Interpret estimated coefficients, standard errors, t-statistics, and overall model significance.
- Test for heteroscedasticity using the Breusch–Pagan–Godfrey test.
- Assess residual normality using the Jarque–Bera test.
- Investigate stationarity using the Augmented Dickey–Fuller (ADF) unit-root test.
- Examine potential serial correlation and the risk of spurious regression.
- Identify the additional tests and specification decisions required before drawing reliable economic conclusions.

## Methodology

### 1. Baseline OLS regression

The initial model is specified as:

\[
URBANIZATION_t =
\beta_0+\beta_1POPULATION\_GROWTH_t
+\beta_2GDPCONST_t+\beta_3MAN_t+u_t
\]

Where:

- **Dependent variable:** `URBANIZATION`
- **Explanatory variables:** `POPULATION_GROWTH`, `GDPCONST`, and `MAN`
- \(u_t\): regression error term
- \(t\): annual time index

Variable definitions, measurement units, and data sources will be documented as the dataset metadata are finalized.

### 2. Regression diagnostics

| Diagnostic | Test | Purpose |
|---|---|---|
| Heteroscedasticity | Breusch–Pagan–Godfrey | Assess whether the error variance is constant |
| Residual normality | Jarque–Bera | Assess whether the residual distribution is consistent with normality |
| Unit root / stationarity | Augmented Dickey–Fuller | Test the null hypothesis that a series has a unit root |
| Serial correlation | To be investigated | Examine dependence between regression errors over time |

### 3. Time-series specification

The initial ADF analysis of urbanization uses two specifications:

- Intercept only.
- Intercept and linear trend.

The trend-inclusive test uses automatic lag selection based on the Schwarz Information Criterion (SIC). The selected specification includes seven lagged differences.

Because the sample is relatively small, lag selection, deterministic terms, and test power require careful consideration. The stationarity of the remaining variables and the possibility of cointegration have not yet been established.

## Preliminary Results

The following results are taken from the initial EViews outputs. They are preliminary and should not be interpreted as final evidence of a valid economic relationship.

### Baseline OLS estimates

| Metric | Result |
|---|---:|
| Observations | 35 |
| \(R^2\) | 0.991083 |
| Adjusted \(R^2\) | 0.990220 |
| F-statistic | 1148.523 |
| Probability of F-statistic | 0.000000 |
| Durbin–Watson statistic | 0.428254 |

The model exhibits a very high in-sample \(R^2\) and is statistically significant overall under the reported conventional OLS test.

However, the low Durbin–Watson statistic raises a concern about positive serial correlation. The combination of a high \(R^2\), annual time-series data, and a low Durbin–Watson statistic motivates further investigation of stationarity, serial correlation, and possible spurious regression.

### Heteroscedasticity test

**Breusch–Pagan–Godfrey**

- Null hypothesis: the error variance is constant.
- Observations: 35.
- Obs*R-squared: 0.620166.
- p-value: 0.8918.

**Interpretation:** Fail to reject the null hypothesis at the 5% significance level. The test does not provide statistically significant evidence of heteroscedasticity.

This does not prove that the error variance is constant; the test may have limited power in a small sample.

### Residual normality test

**Jarque–Bera**

- Null hypothesis: the errors are normally distributed.
- Jarque–Bera statistic: 1.202393.
- p-value: 0.548155.
- Sample skewness: −0.088777.
- Sample kurtosis: 2.109510.

**Interpretation:** Fail to reject the null hypothesis at the 5% significance level. There is insufficient statistical evidence against normality based on this test.

### Unit-root test

**Augmented Dickey–Fuller — urbanization in levels, with intercept and linear trend**

- Null hypothesis: urbanization has a unit root.
- ADF statistic: −2.368441.
- 5% critical value: −3.587527.
- p-value: 0.3863.
- Observations in the test regression: 27.

**Interpretation:** Fail to reject the unit-root null hypothesis at conventional significance levels.

The result raises a concern that urbanization may be non-stationary in levels. It does not establish conclusively that a unit root exists, and the appropriate specification and lag length require further assessment.

## Key Econometric Considerations

This project distinguishes between a model that fits the observed sample and a model that supports reliable economic inference.

The main considerations are:

1. **Potential spurious regression:** Non-stationary variables can produce misleadingly high \(R^2\) values and conventional significance statistics when a valid long-run relationship is absent.
2. **Serial correlation:** The low Durbin–Watson statistic warrants further residual testing.
3. **Stationarity:** Each series must be assessed using appropriate deterministic terms and lag selection.
4. **Cointegration:** If the relevant variables are non-stationary and integrated of the same order, cointegration should be investigated before choosing between a levels model and a differenced specification.
5. **Inference:** Conventional OLS t-tests and F-tests should not be treated as automatically reliable when important time-series assumptions remain unresolved.

No final conclusion about the validity of the baseline regression is drawn at this stage.

## Project Workflow

1. Organize the annual dataset in EViews.
2. Estimate the baseline OLS regression.
3. Interpret the coefficient estimates and model summary.
4. Run heteroscedasticity and normality diagnostics.
5. Conduct ADF tests on urbanization using alternative deterministic specifications.
6. Investigate the stationarity of the explanatory variables.
7. Assess serial correlation and the possibility of spurious regression.
8. Determine whether the baseline specification should be retained, transformed, or replaced with an appropriate time-series model.
9. Document the final specification, diagnostic results, limitations, and conclusions.

## Tools & Techniques

- **EViews:** Econometric estimation, hypothesis testing, and time-series diagnostics.
- **Ordinary Least Squares:** Baseline regression estimation.
- **Breusch–Pagan–Godfrey:** Heteroscedasticity testing.
- **Jarque–Bera:** Residual normality testing.
- **Augmented Dickey–Fuller:** Unit-root testing.
- **Statistical inference:** p-values, critical values, coefficient significance, and model diagnostics.

## Repository Structure

The repository will be organized to separate data, analysis, results, and documentation.

```text
urbanization-econometrics/
│
├── README.md
├── data/
│   └── README.md
├── eviews/
│   └── README.md
├── results/
│   ├── ols_regression.png
│   ├── heteroscedasticity_test.png
│   ├── normality_test.png
│   └── adf_test.png
└── docs/
    └── methodology.md
```

*This is a proposed structure. Add files and folders as they are created; do not include placeholder screenshots or data files as if they already exist.*

The dataset, EViews workfile, and supplementary documentation should be added only when they are ready to share. Data sources, variable definitions, and any licensing or redistribution restrictions should be documented before publication.

## Current Status & Next Steps

**Completed**
- Baseline OLS estimation.
- Initial coefficient and model-summary interpretation.
- Breusch–Pagan–Godfrey heteroscedasticity test.
- Jarque–Bera residual normality test.
- ADF testing of urbanization in levels under two specifications.

**In progress**
- Testing the stationarity of all explanatory variables.
- Reviewing ADF lag selection and deterministic specifications.
- Investigating serial correlation.
- Assessing possible cointegration and the appropriate final model.

## Limitations

The analysis currently uses a relatively small annual sample of 35 observations. The initial model has not yet undergone a complete time-series specification and robustness assessment. The geographic coverage, variable definitions, measurement units, and data provenance must be documented explicitly before the results are presented as a completed empirical study.

The findings should therefore be interpreted as preliminary econometric evidence, not as established causal relationships.

## Learning Objectives

This project documents the practical application of econometric concepts, moving from regression estimation to diagnostic testing and critical evaluation of empirical results.

It is also a learning exercise in reproducible analysis: recording specifications, preserving diagnostic outputs, interpreting statistical evidence, and refining a model based on its limitations rather than its apparent fit alone.

---

**Author:** Sama Farouk  
**Field:** International Economics | Applied Econometrics | Quantitative Economic Analysis  
**Software:** EViews

*Part of Mini Quant Lab — a growing portfolio of applied quantitative methods and empirical research in economics, finance, and political economy.*
