def diff_int(operation_list, operation_type):
    if operation_type not in [1,-1]:
        return False
    if operation_type == 1:
        result = ''
        result_poly = ''
        for i in range(len(operation_list)):
            res = f'{i*operation_list[i]} '
            res_poly = f'{res[:-1]} x^{i-1} + '
            if i == 0:
                res = ''
                res_poly = ''
            if i == 1:
                res_poly = f'{res[:-1]} + '
            if i == len(operation_list)-1:
                res_poly = res_poly[:-3]
            result += res
            result_poly += res_poly
    else:
        result = ''
        result_poly = ''
        for i in range(len(operation_list)):
            res = f'{round(operation_list[i]/(i+1),2)} '
            res_poly = f'{res[:-1]} x^{i+1} + '
            if i == len(operation_list)-1:
                res_poly = res_poly[:-3]
            result += res
            result_poly += res_poly

    return result, result_poly
