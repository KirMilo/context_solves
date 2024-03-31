import sys


def encrypt_employee(emp_data: list[str]) -> str:
    fio = ",".join(emp_data[:3])
    day_and_month = emp_data[3] + emp_data[4]

    sum_params = (len(set(fio))
                  + (sum(int(digit) for digit in day_and_month) * 64)
                  + (ord(emp_data[0][0].upper()) - ord("A") + 1) * 256)

    result = hex(sum_params - 1)

    return result[len(result) - 3:]


try:
    amount_employees = int(input())
    output = ""

    for i in range(amount_employees):
        employee = input()
        output += encrypt_employee(employee.split(",")) + " "

    output = output[:len(output) - 1]
    print(output.upper())

finally:
    sys.exit()
