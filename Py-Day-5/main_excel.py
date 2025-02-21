from my_experience.administration import excel_file_operations

excel_filename = r"F:\ITI\Intake 45 Data\09. Introduction to Python Programming (Python)\Eng. Josephine Boles\Day 5\Labtest_excel.xlsx"

data = [
    ["Name", "Age", "Job"],
    ["Yasmine", 24, "System Admin"],
    ["Yahya", 27, "Software Engineer"],
    ["Yousef", 30, "Data Analyst"]
]

excel_file_operations.write_excel(excel_filename, data)

read_data = excel_file_operations.read_excel(excel_filename)

print("\nExcel File Content:")
for row in read_data:
    print(row)
