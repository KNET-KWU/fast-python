liner = lambda: print("-" * 10)


def for_else():

    # 중간에 break로 인해 루프를 탈출하지 않은 경우 else 문이 호출됨
    for x in range(5):
        if x > 6:
            break
    else:
        print("all nums are less than 6")

    # 중간에 break로 인해 루프를 탈출할 경우 호출이 안됨
    for x in range(4, 10):
        if x > 6:
            print(f"{x} > 6")
            break
    else:
        print("all nums are less than 6")

    # break가 아니어도 특별한 경우 없이 다 돌면 else 호출
    for x in range(10):
        pass
    else:
        print("모든 루프를 돌았다")


def try_except_else():

    try:
        1 + 2
    except Exception as E:
        print(f"{E=}")
    else:
        print("정상적으로 수행했음")

    try:
        1 + "2"
    except Exception as E:
        print(f"{E=}")
    else:
        print("정상적으로 수행했음")


def if_elif():

    case = 120
    if case == 100:
        pass  # do something...
    elif case == 300:
        pass  # do something...
    else:
        print("케이스 조건절에 해당되는게 없음!")

    a = 10
    b = 12
    # 삼항 연산자
    a_is = "홀수" if a % 2 else "짝수"

    # 삼항 연산자 2개
    b_is_6n = False if b % 2 else (False if b % 3 else True)

    print(f"{a}은(는) {a_is}임")

    print(f"{b}은(는) 6의 배수다 : {b_is_6n}")


def kwargs_args():

    # kwargs : keyword + arguments
    # args : arguments

    def some_func(*args, **kwargs):
        print("변수 이름 없이 대입한 것들")
        for x in args:
            print(x)
        print()
        # kwargs는 key-value로 dict 타입이다.
        print("변수 이름과 함께 대입한 것들")
        [print(f"{key} : {value}") for key, value in kwargs.items()]

    some_func("var", 123, {"hello": "world"}, age=25, name="go_home")


def unpacking():

    # *(Asterik, 별, star)가 있는 경우 길이가 0 이상인 튜플임!!
    first_num, *others = [1, 2, 3, 4, 5]

    print(f"{first_num=}")
    print(f"{others=}")
    print()

    # 이런식으로 앞뒤로 몇 개만 특정지어서 가져올 수 있다.
    first_num, *others, last_num = [1, 2, 3, 4, 5]
    print(f"{first_num=}")
    print(f"{others=}")
    print(f"{last_num=}")

    # 필요없는 것들은 컨벤션으로 언더바( _ )를 사용하자
    _, _, *others, last_num = [x for x in range(1, 6)]
    print(f"{others=}")
    print(f"{last_num=}")


def with_as():

    with open("README.md", mode="r", encoding="utf-8") as fp:
        # do somehting...
        print(f"파일 읽기쓰기 작업이 가능할까요? {not fp.closed}")

    # 코드를 깔끔하기 위해서 맥락에서 (파이썬에서는 인덴트) 나올 경우
    # 정의한 내용을 수행
    print(f"파일 읽기쓰기 작업이 가능할까요? {not fp.closed}")


class HelloWorld(object):
    def __init__(self, name: str) -> None:
        self.name = name

    def print_name(self):
        print(f"내 이름은요 {self.name}")

    def __enter__(self):
        print("컨텍스트 매니저 진입!!")
        return self

    def __exit__(self, type, value, traceback):
        # 만약 네트워크 연결과 같이 리소스를 사용하는 객체는 자원 정리
        print("컨텍스트 밖으로 빠져나온다!!")


def with_as2():

    with HelloWorld("케이넷") as helloworld:
        helloworld.print_name()


if __name__ == "__main__":
    for_else()
    liner()
    try_except_else()
    liner()
    if_elif()
    liner()
    kwargs_args()
    liner()
    unpacking()
    liner()
    with_as()
    liner()
    with_as2()
