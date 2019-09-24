from Card import Card
from Deck import Deck

def main():
    x = Deck()
    print(x.cards)
    x.shuffle()
    print(x.cards)


if __name__ == '__main__':
    main()
