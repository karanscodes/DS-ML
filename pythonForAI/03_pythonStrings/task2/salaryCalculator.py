def taxDeduction(salary):
  if(salary < 5_00_000):
    return 0
  if(salary < 10_00_000):
    return salary * 0.1
  if(salary < 20_00_000): 
    return salary * 0.2
  return salary * 0.3

# take salary from the user
salary = int(input("Enter Your CTC: "))
HRA = salary * 0.1
DA = salary * 0.05
PF = salary * 0.03

inhandSalary = salary - (HRA + DA + PF + taxDeduction(salary))
print(round(inhandSalary/12, 2))
