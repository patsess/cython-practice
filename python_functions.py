
def get_income_tax_rate(salary):
    if salary <= 11850:
        tax_rate = 0.
    elif salary <= 46350:
        tax_rate = 0.2
    elif salary <= 150000:
        tax_rate = 0.4
    else:
        tax_rate = 0.45

    return tax_rate


def repeat_income_tax_rates(salary, n_repeats):
    return [get_income_tax_rate(salary) for _ in range(n_repeats)]
