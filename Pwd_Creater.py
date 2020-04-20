import string
import itertools
import hashlib


def check_input(info):
    if not info['MAX_LENTH'].isdigit():
        return 'MAX_LENTH is NOT a number!'
    elif not info['MIN_LENTH'].isdigit():
        return 'MIN_LENTH is NOT a number!'
    elif int(info['MIN_LENTH']) > int(info['MAX_LENTH']):
        return 'The MIN_LENTH is GREATER than the MAX_LENTH!'
    elif not (info['is_lower'] or info['is_upper'] or info['is_digit']):
        return 'Did NOT choose any string to combine!'
    else:
        return False


def f_name(info):
    task_str = ''
    file_name = 'combine_{}-{}-lud.txt'.format(info['MIN_LENTH'], info['MAX_LENTH'])
    if info['is_lower'].lower() == 'y':
        task_str = task_str + string.ascii_lowercase
    else:
        file_name = file_name.replace('l', '_')
    if info['is_upper'].lower() == 'y':
        task_str = task_str + string.ascii_uppercase
    else:
        file_name = file_name.replace('u', '_')
    if info['is_digit'].lower() == 'y':
        task_str = task_str + string.digits
    else:
        file_name = file_name.replace('d', '_')
    times = 0
    for length in range(int(info['MIN_LENTH']), int(info['MAX_LENTH']) + 1):
        times = times + len(task_str) ** length
    print('I will compute %s times!' % format(times, ','))

    proceed_on = input('Confirm proceed? (yes/no):')
    return proceed_on, file_name, task_str


while 1:
    MIN_LENTH = input('Min Length is:').strip()
    MAX_LENTH = input('Max Length is:').strip()
    is_lower = input('Include lower letters? (y/n):').strip()
    is_upper = input('Include upper letters? (y/n):').strip()
    is_digit = input('Include numbers? (y/n):').strip()
    input_info = {
        'MIN_LENTH': MIN_LENTH,
        'MAX_LENTH': MAX_LENTH,
        'is_lower': is_lower,
        'is_upper': is_upper,
        'is_digit': is_digit
    }
    res = check_input(input_info)
    if res:
        print(res)
    else:
        proceedOn, fileName, taskStr = f_name(input_info)
        break

if proceedOn.lower() == 'yes':
    with open(fileName, 'w') as f:
        print('Initialization has Done, Start Writing!\n The file name is %s', fileName)
        for t in range(int(MIN_LENTH), int(MAX_LENTH) + 1):
            print('Current Mission:', t)
            for i in itertools.combinations_with_replacement(taskStr, t):
                i = ''.join(i)
                i_md5 = hashlib.md5(i.encode(encoding='utf-8')).hexdigest()
                f.write(i + '\t' + i_md5 + '\n')
    print('Done!!!')
else:
    print('The task was not be proceeded.')
