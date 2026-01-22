def make_greeting(name, year):
    """
    사람에게 현재 연도를 바탕으로 나이를 알려주는 문자열을 반환하는 함수 

    :param name: 사람
    :param year: 출생 연도
    """

    return f'Hello, {name}!!! You are {2026 - year + 1} years old.'

# positional argument: 매개변수의 순서에 맞춰 인자를 전달하는 방법
print(make_greeting('Jeeho', 1900))
# print(make_greeting(1900, "Jeeho")) # error 발생

# keyword argument: 매개변수의 이름을 바탕으로 인자를 전달하는 방법
print(make_greeting(year = 1900, name = 'Jeeho')) 

# default parameter; 매개변수에 기본값을 미리 할당하는 방법
def make_greeting(name = 'Anon', year = 2025):
    return f'Hello, {name}!!! You are {2026 - year + 1} years old.'

print(make_greeting())
print(make_greeting(name = 'alex'))
print(make_greeting('brad'))
print(make_greeting(year = 1900))
# bad
# print(make_greeting(year = 1000. 'alex'))

# arbitrary arguments
def calculate_sum(*args):
    return sum(args)

def print_movie_info(*args): # 각 자리에서 바라는 형태가 있는 것이므로 이건 arbitrary하지 않음 -> 안 좋음!
    print(args[0])
    print(args[1])
    print(args[2])
    # -> 필요한 매개변수에 기본 값을 설정해서 사용하는 경우가 많고 arbitray을 직접 쓰는 경우는 많지 않음. 
    # 매개 변수를 하나하나 설정하지 않고 이런 식으로 쓰는 건 좋지 않은 코드임.
    # print_movie_info(title, name, year) 이런 식으로 입력하는 게 맞음.