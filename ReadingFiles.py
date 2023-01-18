employee_file = open("employees.txt", "r")

if employee_file.readable():
    #print(employee_file.read())
    #print(employee_file.readline())
    #print(employee_file.readline())
    #print(employee_file.readlines()[2])
    for employee in employee_file.readlines():
        print(employee)

employee_file.close()
