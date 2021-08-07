# Card ordering
# Separate according to shade, then arrange the shades
# F < S < D < H < JOKER
# A < 2 < 3 < .. < 9 < 10 < J < Q < K

# [10F, KD, JOKER, 2H, 4H, 5S, AS, QH, 7D]
# [10F][KD, 7D][ JOKER][2H, 4H, QH][5S, AS]
# [10F][7D, KD][JOKER][2H, 4H, QH][AS, 5S]
# [10F, AS, 5S, 7D, KD, 2H, 4H, QH, JOKER]

CARDS_RANK = {
    'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13
}

# 'R' - for Joker
SHADES_LIST = ['F', 'S', 'D', 'H', 'R']


def is_lower_rank(card_1: str, card_2: str) -> bool:
    rank_1 = card_1[:-1]
    rank_2 = card_2[:-1]

    return CARDS_RANK[rank_1] < CARDS_RANK[rank_2]


def sort_cards_by_rank(cards: list):

    for i in range(1, len(cards)):
        key_card = cards[i]
        j = i - 1

        while j >= 0 and is_lower_rank(cards[i], cards[j]):
            cards[j + 1] = cards[j]
            j -= 1

        cards[j + 1 ] = key_card


def sort_cards(deck: list):
    # print(deck)
    # [10F, KD, JOKER, 2H, 4H, 5S, AS, QH, 7D]

    shades = {}
    for card in deck:
        shade = card[-1]
        if shade in shades:
            shades[shade].append(card)
        else:
            shades[shade] = [card]

    # print(shades)
    # [10F][KD, 7D][ JOKER][2H, 4H, QH][5S, AS]

    for shade in shades:
        if shade != 'R':
            sort_cards_by_rank(shades[shade])

    # print(shades)
    # [10F][7D, KD][JOKER][2H, 4H, QH][AS, 5S]

    i = 0
    for shade in SHADES_LIST:
        if shade in shades:
            for card in shades[shade]:
                deck[i] = card
                i += 1

    # print(deck)
    # [10F, AS, 5S, 7D, KD, 2H, 4H, QH, JOKER]


# Test
cards = ['10F', 'KD', 'JOKER', '2H', '4H', '5S', 'AS', 'QH', '7D']

sort_cards(cards)
print(cards)