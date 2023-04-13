import asyncio
import aiohttp
from .html_job import *

ROOM_1 = "http://mobileid.kw.ac.kr/seatweb/roomview5.asp?room_no=1"
ROOM_2 = "http://mobileid.kw.ac.kr/seatweb/roomview5.asp?room_no=2"
ROOM_3 = "http://mobileid.kw.ac.kr/seatweb/roomview5.asp?room_no=3"


async def get_reading_room():
    room = [{}, {}, {}]
    for room_num, x in enumerate([ROOM_1, ROOM_2, ROOM_3]):
        async with aiohttp.ClientSession() as session:
            async with session.get(x) as response:
                html = await response.text()
                # tot_num, using, not_using = total_seat_number(html)
                using_list, not_using_list = get_seats(html)
                room[room_num] = {"in_use": using_list, "not_use": not_using_list}
            await asyncio.sleep(1)
    return room
