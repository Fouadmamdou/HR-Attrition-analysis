import pandas as pd

# 1) Load the dataset (the data sheet is the second sheet in the workbook)
file_path = "C:\\Users\\dell\\Desktop\\case\\HR_Attrition_Fouad Mamdouh\\01_Power BI\\GBS BI HUB - BI Developer - HR Attrition Case Study (1).xlsx"
df = pd.read_excel(file_path, sheet_name=1)

# 2) Classify employees by TotalWorkingYears
#    Junior: < 5 | Mid: 5-9 | Senior: 10+
def classify_experience(years):
    if years < 5:
        return "Junior"
    elif years < 10:
        return "Mid"
    else:
        return "Senior"

df["ExperienceLevel"] = df["TotalWorkingYears"].apply(classify_experience)

# 3) Summary table: ExperienceLevel | EmployeeCount
order = ["Junior", "Mid", "Senior"]
summary = (
    df.groupby("ExperienceLevel")
      .size()
      .reindex(order)
      .reset_index(name="EmployeeCount")
)

print(summary.to_string(index=False))
print("Total:", summary["EmployeeCount"].sum())