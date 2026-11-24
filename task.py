number_team=int(input("please number of team :"))
number_month=float(input("please enter Number of months the project will take :"))
salary=float(input("please enter Monthly salary : "))
cloud_cost=float(input("please enter Total cloud cost for the whole project:"))
salary_cost=number_team*number_month*salary
sub_total=salary_cost+cloud_cost
vat=sub_total*0.14
total=sub_total+vat
print(f"salary_cost{salary_cost:,.2f}and sub_total{sub_total:,.2f}and vat{vat:,.2f}and total{total:,.2f}: ")