employee_salaries = {}
while True:
    name = input("Enter employe name or (no) to exit: ")

    if name.lower() == 'no':
        break
    salary = int(input("Enter Salary: "))

    employee_salaries[name] = salary
    printing = input("if you want to print type (p) to continue type anything else")
    if printing == 'p':
        print(employee_salaries)