import string
import itertools
import hashlib

MIN_LENTH = input('Min Length is:')
MAX_LENTH = input('Max Length is:')
is_lower = input('Include lower letters? (y/n):').lower()
is_upper = input('Include upper letters? (y/n):').lower()
is_digit = input('Include numbers? (y/n):').lower()
task_str = ''
file_name = 'combina_{}-{}-lud.txt'.format(MIN_LENTH, MAX_LENTH)
if is_lower == 'y':
    task_str = task_str + string.ascii_lowercase
else:
    file_name = file_name.replace('l', '_')
if is_upper == 'y':
    task_str = task_str + string.ascii_uppercase
else:
    file_name = file_name.replace('u', '_')
if is_digit == 'y':
    task_str = task_str + string.digits
else:
    file_name = file_name.replace('d', '_')
print('I will compute %s times!', format(10 ** len(task_str), ','))

proceedOn = input('Confirm proceed? (yes/no):')

if proceedOn.lower() == 'yes':
    with open(file_name, 'w') as f:
        print('Initializer Done, Start Writing!\n The file name is %s', file_name)
        for t in range(int(MIN_LENTH), int(MAX_LENTH) + 1):
            print('Current Mission:', t)
            for i in itertools.combinations_with_replacement(task_str, t):
                i = ''.join(i)
                i_md5 = hashlib.md5(i.encode(encoding='utf-8')).hexdigest()
                f.write(i + '\t' + i_md5 + '\n')
    print('Done!!!')
else:
    print('The task was not be proceeded.')
