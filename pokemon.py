from collections import *
from typing import List

from move import Move

class Pokemon:
    def __init__(self, name: str, nickname: str, dex_number: int, type1: str, type2: str):
        self.name = name
        self.nickname = nickname
        self.dex_number = dex_number
        self.type1 = type1
        self.type2 = type2
        self.moves_list = [None, None, None, None]

    def __iter__(self):
        yield 'name', self.name
        yield 'nickname', self.nickname
        yield 'dex_number', self.dex_number
        yield 'type1', self.type1
        yield 'type2', self.type2
        yield 'moves_list', self.moves_list

    def set_move(self, index: int, move: Move):
        self.moves_list[index] = move

    def set_all_moves (self, moves_list: List[Move]) -> List[Move]:
        self.moves_list = moves_list
        return self.moves_list