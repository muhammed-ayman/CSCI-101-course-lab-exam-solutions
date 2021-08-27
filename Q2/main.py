from module import *

poly_terms = input('Enter Polynomial terms: ').split()
poly_terms = [float(i) for i in poly_terms]
operation_choice = input('Choose Operation 1 derivative -1 antiderivative: ')
if operation_choice == '-1':
    integ_const = input('Enter integration constant: ')
result = diff_int(poly_terms, int(operation_choice))
if operation_choice == '-1':
        print(f'Resulting polynomial terms: {integ_const} {result[0]}')
else:
    print(f'Resulting polynomial terms: {result[0]}')
que = input('Do you need to show as a polynomial?').lower()
if que == 'yes':
    if operation_choice == '-1':
        print(f'Resulting polynomial terms: {integ_const} + {result[1]}')
    else:
        print(f'Resulting polynomial terms: {result[1]}')
