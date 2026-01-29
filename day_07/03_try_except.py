# 예외가 아니고 정상 흐름
# operand_a = int(input('a: '))
# operand_b = int(input('b: '))

# if operand_b == 0:
#     print(f'몫: {operand_a // operand_b}, 니머지: {operand_a % operand_b}')
# else:
#     print(f'몫: {operand_a // operand_b}, 니머지: {operand_a % operand_b}')

# 문제가 발생할 수 있는 코드를 묶어서 예외를 잡아주기 위한 구역
try:
    # operator = input().strip()
    # print(f'input str: "{operator}"')
    operand_a = int(input('a: '))
    operand_b = int(input('b: '))
    print(f'몫: {operand_a // operand_b}, 니머지: {operand_a % operand_b}')
# 실제로 문제가 발생했을 때 어떻게 처리를 할 지를 결정하는 구역
except ZeroDivisionError:
    print('0으로 나누는 건 허용되지 않습니다.')
except ValueError:
    print('정수를 입력하세요')
except BaseException as exception:
    print(exception)
    pass
