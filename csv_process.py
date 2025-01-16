import csv

# File path for the employee data
file_path = "employee_data.csv"

# Create a new CSV file with headers
def create_csv():
    headers = ["Name", "Age", "Department"]
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    print("Employee data created successfully.")

def add_detail(name, age, department):
    """Append a single record to the CSV file."""
    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, department])
    print(f"Record for {name}, {age} and {department} added successfully.")

def generate_employee_data(num_records):
    names = ["Jack", "Zulip", "Siya", "Mina"]
    ages = [26, 33, 29, 44]
    departments = ["IT", "HR", "Finance", "Marketing"]

    # Generate and add num_records worth of employee data
    for _ in range(num_records):
        for name, age, department in zip(names, ages, departments):
            add_detail(name, age, department)  # Add each record to the CSV file

    print(f"Generated and saved {len(names) * num_records} employee records to '{file_path}'.")

def print_employees_above_30():
    """Print names of employees whose age is above 30."""
    with open(file_path, mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            name, age, department = row
            if int(age) > 30:
                print(name)  # Print the name if the age is greater than 30

create_csv()
generate_employee_data(1)
print("\nEmployees above 30 years of age:")
print_employees_above_30()

