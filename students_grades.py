import openpyxl

def create_student_result(file_path):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Student Results"

    sheet.append(["Name", "Grades"])
    sheet.append(["Asmita", 95])
    sheet.append(["Avipsha", 99]) 
    sheet.append(["Anjali", 80]) 
    sheet.append(["Yanji", 85]) 

    workbook.save(file_path)
    print("Students results created successfully.")

file_path = "student_grade.xlsx"
create_student_result(file_path)



