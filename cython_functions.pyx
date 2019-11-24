
import numpy as np


cpdef double get_income_tax_rate(int salary):
    cdef double tax_rate

    if salary <= 11850:
        tax_rate = 0.
    elif salary <= 46350:
        tax_rate = 0.2
    elif salary <= 150000:
        tax_rate = 0.4
    else:
        tax_rate = 0.45

    return tax_rate


cpdef double[::1] repeat_income_tax_rates(int salary, int n_repeats):
    cdef double[::1] salaries = np.zeros(n_repeats)
    #cdef double salaries[1][n_repeats]
    cdef int i
    for i in range(n_repeats):
        salaries[i] = get_income_tax_rate(salary)

    return salaries
