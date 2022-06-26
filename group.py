from typing import Tuple, List

from pair import Pair


class Group():
    players = Tuple[str, ...]

    def __init__(self, *players: str):
        self.players = tuple(players)

    def allPairs(self) -> List[Pair]:
        pairs = []
        for idx, x in enumerate(self.players):
            for y in self.players[idx + 1::]:
                pairs.append(Pair(x, y))
        return pairs


def getAvailablePairs(group: Group, excluded_pairs: List[Pair]) -> List[Pair]:
    all_pairs = group.allPairs()
    return list(filter(lambda pair: not pair in excluded_pairs, all_pairs))


def getRatingGames(group: Group, excluded_pairs: List[Pair], available_players: List[str]) -> List[Pair]:
    """
    можно напистать алгоритм поиска максимального паросочетания
    пока здесь перебор для простоты
    """
    pairs = list(filter(
        lambda pair:
        pair.first in available_players
        and pair.second in available_players,
        getAvailablePairs(group, excluded_pairs)))

    result = []
    bound = 2 ** len(pairs)
    for mask in range(0, bound):
        cur_pack = []
        index = 0
        while mask > 0:
            if mask % 2 == 1:
                cur_pack.append(pairs[index])
            mask //= 2
            index += 1

        can_playing = True
        for x in cur_pack:
            for y in cur_pack:
                if x != y and (x.first in y or x.second in y):
                    can_playing = False
        if can_playing and len(cur_pack) > len(result):
            result = cur_pack
    return result
