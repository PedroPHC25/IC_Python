def num_romanos(num):
    if num <= 3:
        res = num * 'I'
    elif num == 4:
        res = 'IV'
    elif 5 <= num <= 8:
        res = 'V' + (num - 5) * 'I'
    elif num == 9:
        res = 'IX'
    elif 10 <= num <= 13:
        res = 'X' + (num - 10) * 'I'
    else:
        print(f'Não sei converter {num}!')
    return res
