from bs4 import BeautifulSoup
from functools import partial
from typing import Tuple, List, NewType
import re

__all__ = ["total_seat_number", "get_seats"]

HTML = NewType("HTML", str)


def total_seat_number(htmlstuff: HTML):
    """
    총 사용자 좌석 수 검증하는 용도

    Args:
        htmlstuff (HTML):
            광운대 오픈열람실 좌석 정보 HTML

    Returns:
        총 좌석수(int), 사용 좌석수(int), 잔여 좌석수(int)
    """
    bsObject = BeautifulSoup(htmlstuff, "lxml")
    data = bsObject.select(
        "body > center > table:nth-of-type(2) > tr > td > table > tr"
    )

    SEAT_TOTAL = "총 좌석수"
    SEAT_USED = "사용 좌석수"
    SEAT_UNUSED = "잔여 좌석수"

    total_seats = data[1].select_one("tr > td > table > tr").select("td")

    def get_seat_number_of(type_, partialHTMLs):
        def sibal(target, sss):
            ssss = re.compile(f"^.*{target}.*$")
            return any([ssss.fullmatch(x.string) for x in sss.select("b")])

        findingFunction = partial(sibal, type_)

        for partialHTML in partialHTMLs:
            if partialHTML.find(findingFunction):
                qp = partialHTML.select_one("font:nth-of-type(2) > b").text
                return int(qp)

    return tuple(
        [
            get_seat_number_of(x, total_seats)
            for x in [SEAT_TOTAL, SEAT_USED, SEAT_UNUSED]
        ]
    )


def get_seats(htmlstuff: HTML) -> Tuple[List[int], List[int]]:
    """
    Args:
        htmlstuff (HTML):
            광운대 오픈열람실 좌석 정보 HTML

    Returns:
        (사용중인 좌석 번호 List, 비어있는 좌석 번호 List)
    """
    bsObject = BeautifulSoup(htmlstuff, "lxml")
    data = bsObject.select(
        "body > center > table:nth-of-type(2) > tr > td > table > tr"
    )
    seat_info = data[2].select_one("tr > td > div#maptemp")
    single_seat_info_list = seat_info.find_all("div", id=re.compile("^Layer[0-9].*$"))

    st_used = []
    st_unused = []

    for x in single_seat_info_list:
        a = x.select_one("div > table > tr > td")
        if a["bgcolor"] == "gray":
            st_unused.append(int(a.select_one("font").string))
        elif a["bgcolor"] == "red":
            st_used.append(int(a.select_one("font").string))

    return st_used, st_unused
    print(f"사용중 : {len(st_used)}, 사용 안하는 중 : {len(st_unused)}")
