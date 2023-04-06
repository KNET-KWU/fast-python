# 컨프리헨션
def list_comprehension():

    [x for x in range(10)]


def set_comprehension():

    {x for x in range(10)}


def dict_comprehension():

    {x: x for x in range(10)}


def generator_comprehension():

    (x for x in range(10))


def 간단한_실행_함수_한줄로_쓰기():
    def some_function():
        pass

    # for 루프 돌면서 실행하기
    for _ in range(10):
        some_function()

    # 한 줄로 실행하기
    [some_function() for _ in range(10)]


if __name__ == "__main__":
    pass
