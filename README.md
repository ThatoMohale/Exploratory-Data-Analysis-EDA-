### Student Performance Exploratory Data Analysis (EDA) Summary

This document outlines the exploratory data analysis (EDA) performed on the **Week-5-Student-Scores.csv** dataset, part of the "Performing EDA in Python" group project. The aim of this analysis is to explore patterns in learner performance to guide potential educational interventions.

---

### Q1 — Data Readiness & Quality Checks

#### 1. Initial Data Assessment

* **Dataset Overview:**

  * The dataset initially contained **121 rows** and **10 columns**.

* **Column Data Types:**

  * The dataset contained a mix of object (categorical) and float64 (numerical) data types.
  * Numerical columns: `Study_Hours_per_Week`, `Attendance_Rate`, `Previous_Score`, `Quiz1`, `Quiz2`, `Quiz3`, `Final_Score`.

* **Number of Duplicates:**

  * 1 duplicate row was detected.

#### 2. Diagnostics Table

| Column               | Data Type | Missing Values |
| -------------------- | --------- | -------------- |
| Student_ID           | object    | 0              |
| Gender               | object    | 0              |
| Subject              | object    | 0              |
| Study_Hours_per_Week | float64   | 5              |
| Attendance_Rate      | float64   | 5              |
| Previous_Score       | float64   | 0              |
| Quiz1                | float64   | 0              |
| Quiz2                | float64   | 5              |
| Quiz3                | float64   | 0              |
| Final_Score          | float64   | 0              |

* **Missing Values:**

  * A total of **15 missing values** were spread across three columns: `Study_Hours_per_Week`, `Attendance_Rate`, and `Quiz2`.

#### 3. Data Cleaning Decisions

* **Handling Missing Values:**

  * The decision was made to **drop all rows** with missing values, resulting in the removal of **14 rows**, reducing the dataset size from **121** to **107 records**.

* **Handling Duplicates:**

  * The 1 duplicate row was handled by the same process (`dropna()`), ensuring a clean dataset without duplicates.

* **Justification for Dropping Rows:**

  * Given the **small percentage of missing data** (~4.1% for affected columns), dropping incomplete rows was considered the best approach to maintain data integrity, especially for critical variables such as scores.

* **Final Quality:**

  * After cleaning, the dataset contains **0 missing values** and **0 duplicate rows**.

---

### Q2 — Descriptive Statistics & Distributions

#### 1. Compact Table of Descriptive Statistics

| Column               | Mean  | Median | Std Dev | Min   | 25th Percentile | 75th Percentile | Max   |
| -------------------- | ----- | ------ | ------- | ----- | --------------- | --------------- | ----- |
| Final_Score          | 48.23 | 47.00  | 9.39    | 26.00 | 41.50           | 55.00           | 73.00 |
| Study_Hours_per_Week | 8.21  | 8.20   | 2.90    | 2.10  | 6.05            | 10.05           | 19.60 |
| Attendance_Rate      | 0.89  | 0.89   | 0.07    | 0.74  | 0.83            | 0.95            | 1.00  |
| Previous_Score       | 60.29 | 60.00  | 11.86   | 34.00 | 52.00           | 68.50           | 98.00 |
| Quiz1                | 49.11 | 49.00  | 12.11   | 18.00 | 41.00           | 55.50           | 84.00 |
| Quiz2                | 49.70 | 50.00  | 13.30   | 18.00 | 41.50           | 58.00           | 81.00 |
| Quiz3                | 51.90 | 51.00  | 10.89   | 29.00 | 44.00           | 60.00           | 77.00 |

#### 2. Data Visualizations

* **Histograms** were created to visualize the distribution of key variables:

  * **Final_Score**: The distribution is roughly **bimodal**, with two main peaks: one around 40-45 and another around 50-55.
  * **Study_Hours_per_Week**: The distribution is slightly **positively skewed**, with a peak around 8 hours and one outlier at 19.6 hours.
  * **Attendance_Rate**: The distribution is slightly **negatively skewed**, with most students having excellent attendance (above 0.90).

#### 3. Interpretation of Distributions

* **Final_Score**:

  * The bimodal distribution suggests that students may fall into two distinct performance groups:

    * **Lower Performers**: Scores clustered around 40-45.
    * **Higher Performers**: Scores around 50-55.
    * **Implication**: Interventions could be tailored to these groups, offering targeted support to improve overall performance.

* **Study_Hours_per_Week**:

  * The slight positive skew indicates that most students spend around 8 hours per week studying, with a small number dedicating significantly more time (outlier at 19.6 hours).
  * **Implication**: This highlights the potential influence of study time on performance and suggests a possible area for further investigation.

* **Attendance_Rate**:

  * The near-normal distribution with a high concentration at or above 0.90 suggests that most students maintain good attendance.
  * **Implication**: Strong attendance could be a positive factor for performance, but the impact of attendance on performance needs to be explored further.

---

### 📦 Deliverable

The final, cleaned dataset has been prepared and exported for further analysis. The dataset contains **107 records** with no missing values and no duplicates.

* **File Name:** `Cleaned_Student_Data.xlsx`

This cleaned dataset is now ready for advanced analysis, including predictive modeling or intervention design to improve student outcomes.
