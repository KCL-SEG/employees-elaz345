"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type, commission_type, hours=0, hourly_pay=0, monthly_salary=0, fixed_bonus=0, bonus_per_contract=0, contracts_landed=0):
        self.name = name
        self.contract_type = contract_type
        self.commission_type = commission_type
        self.hours = hours
        self.hourly_pay = hourly_pay
        self.monthly_salary = monthly_salary
        self.fixed_bonus = fixed_bonus
        self.bonus_per_contract = bonus_per_contract
        self.contracts_landed = contracts_landed

    def get_pay(self):
        pay = 0

        if self.contract_type == "hourly":
            pay += self.hours * self.hourly_pay
        else:
            pay += self.monthly_salary

        if self.commission_type == "fixed":
            pay += self.fixed_bonus
        elif self.commission_type == "contract":
            pay += self.contracts_landed * self.bonus_per_contract

        return pay

    def __str__(self):
        contract_description = f"{self.name} works on a "
        
        if self.contract_type == "hourly":
            contract_description += f"contract of {self.hours} hours at {self.hourly_pay}/hour"
        else:
            contract_description += f"monthly salary of {self.monthly_salary}"

        if self.commission_type == "fixed":
            contract_description += f" and receives a bonus commission of {self.fixed_bonus}"
        elif self.commission_type == "contract":
            contract_description += f" and receives a commission for {self.contracts_landed} contract(s) at {self.bonus_per_contract}/contract"

        return f"{contract_description}. Their total pay is {self.get_pay()}."


# Examples
billie = Employee('Billie', "Monthly", "None", monthly_salary=4000)
charlie = Employee('Charlie', "hourly", "None", hours=100, hourly_pay=25)
renee = Employee('Renee', "Monthly", "contract", monthly_salary=3000, bonus_per_contract=200, contracts_landed=4)
jan = Employee('Jan', "hourly", "contract", hours=150, hourly_pay=25, bonus_per_contract=220, contracts_landed=3)
robbie = Employee('Robbie', "Monthly", "fixed", monthly_salary=2000, fixed_bonus=1500)
ariel = Employee('Ariel', "hourly", "fixed", hours=120, hourly_pay=30, fixed_bonus=600)