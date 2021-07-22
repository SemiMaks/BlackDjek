# Функция deal_cards раздает заданное количество карт
# из колоды.

def deal_cards(deck, number):
    # Инициализировать накопитель для количества карт на руках.
    hand_value = 0

    # Убедиться, что количество карт для раздачи
    # не больше количества карт в колоде.
    if number > len(deck):
        number = len(deck)

    # Раздать карты и накопить их значения.
    for count in range(number):
        card, value = deck.popitem()
        print(card)
        hand_value += value

    # Показать величину карт на руках.
    print('Величина карт на руках: ', hand_value)
    return deck, number
