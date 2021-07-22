# Эта программа применяет словарь в качестве колоды карт.

from create_deck import create_deck
from deal_cards import deal_cards


def main():
    # Создаём колоду карт.
    deck = create_deck()

    # Получить количество карт для раздачи.
    num_cards = int(input('Сколько карт сдать? '))

    # Раздать карты.
    deal_cards(deck, num_cards)


main()
