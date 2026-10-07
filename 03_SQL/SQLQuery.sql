SELECT
    dd.Department,
    dj.JobRole,
    SUM(CAST(f.AttritionFlag AS INT)) AS AttritionCount,
    ROUND(AVG(CAST(f.MonthlyIncome AS DECIMAL(10,2))), 2) AS AvgMonthlyIncome
FROM dbo.Fact_Employee f
INNER JOIN dbo.Dim_Department dd ON f.DepartmentID = dd.DepartmentID
INNER JOIN dbo.Dim_JobRole    dj ON f.JobRoleID    = dj.JobRoleID
GROUP BY dd.Department, dj.JobRole
ORDER BY AttritionCount DESC, dd.Department, dj.JobRole;