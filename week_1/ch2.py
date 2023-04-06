import time

# 연산
def add_1(value: int):

    return value + 1


# 지연 연산 / 제너레이터


def add_1_yield(value: int):

    yield value + 1


def 무엇을_반환할까():
    print(type(add_1(10)))
    print(type(add_1_yield(10)))


def very_expensive_func(value: int):
    time.sleep(1)
    return value + 10


if __name__ == "__main__":

    무엇을_반환할까()

    # 시작
    list_item = [very_expensive_func(x) for x in range(10, 50, 10)]
    # 몇 초 걸릴까?

    # 시작
    generator_item = (very_expensive_func(x) for x in range(10, 50, 10))
    # 몇 초 걸릴까?
