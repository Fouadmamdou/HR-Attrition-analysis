

# HR Attrition Analysis: BI Developer Case Study

**Author:** Fouad Mamdouh 
**Date:** oct/7/2026

## Overview
Analysis of 1,470 employees to identify where, why, and how to reduce attrition.
Headline: 237 employees left (16.1%).

## Deliverables

| Task | Deliverable | Location |
|---|---|---|
| 1. Star schema model | Fact_Employee + 5 dimensions | 01_PowerBI/ (Model view) |
| 2. DAX measures (with variables) | Core, income, decision-support, risk measures | 01_PowerBI/ (_Measures table) |
| 3. Outliers and trends | IQR-based outlier flags; trend charts | 01_PowerBI/ |
| 4. Dashboards | Home, Overview, Demographics, Role Details, At-Risk, Root Cause | 01_PowerBI/, 06_Screenshots/ |
| 5. Recommendations | 4 prioritised actions | 02_Presentation/ (slide 7) |
| 6. Presentation | 8-slide deck | 02_Presentation/ |
| 7. SQL query | Join + aggregation | 03_SQL/ |
| 8. Python classification | Experience levels | 04_Python/ |

## Data Model
- Fact: Fact_Employee (1 row per employee)
- Dimensions: Dim_Department, Dim_JobRole, Dim_EducationField, Dim_Demographics, Dim_WorkCondition
- Relationships: many-to-one, single direction
- No date dimension: the dataset has no date column

## Key Assumptions and Decisions
- Removed constant columns (EmployeeCount, StandardHours, Over18).
- Outliers flagged with the IQR rule and retained (they reflect real senior employees).
- Satisfaction labels (Low/Medium/High/Very High) follow the standard coding of this dataset.
- Findings are associations, not proof of causation.

## Key Findings
- Overtime: 30.5% attrition vs 10.4% (2.93x more likely).
- Sales Representatives: 39.8% attrition.
- Job Level 1 with overtime: 52.6%.

## How to Run
- Power BI: open the .pbix in Power BI Desktop.
- SQL: run attrition_query.sql on tables exported from the model.
- Python: place the Excel file beside the script, run `python experience_levels.py`.
