firm_revenue = float(input("Введите выручку фирмы"))
company_costs = float(input("Введите издержки фирмы"))
staff = int(input("Введите количество сотрудников фирмы"))
if firm_revenue > company_costs:
    print(f"Фирма приносит прибыль. Рентабельность выручки {firm_revenue / company_costs:.2f}")
    print(f"Прибыль на одного сотрудника {firm_revenue / staff:.2f}")
elif firm_revenue == company_costs:
     print("Фирма работает в ноль")
else:
    print("Фирма приносит убыток")
