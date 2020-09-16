'''
    Milestone Project 2

    Game Play
        To play a hand of Blackjack the following steps must be followed:

        1. Create a deck of 52 cards
        2. Shuffle the deck
        3. Ask the Player for their bet
        4. Make sure that the Player's bet does not exceed their available chips
        5. Deal two cards to the Dealer and two cards to the Player
        6. Show only one of the Dealer's cards, the other remains hidden
        7. Show both of the Player's cards
        8. Ask the Player if they wish to Hit, and take another card
        9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
        10.If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
        11.Determine the winner and adjust the Player's chips accordingly
        12.Ask the Player if they'd like to play again

    Playing Cards
        A standard deck of playing cards has four suits (Hearts, Diamonds, Spades and Clubs) and thirteen ranks (2 through 10,
        then the face cards Jack, Queen, King and Ace) for a total of 52 cards per deck. Jacks, Queens and Kings all have a rank of 10.
        Aces have a rank of either 11 or 1 as needed to reach 21 without busting. As a starting point in your program,
         you may want to assign variables to store a list of suits, ranks, and then use a dictionary to map ranks to values.
'''
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}
playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"Card with rank {self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has  : "+deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.values = 0
        self.aces = 0

    def add_cards(self, card):
        self.cards.append(card)
        self.values += values[card.rank]

        # track  aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.values > 21 and self.aces:
            self.values -= 10
            self.aces -= 1


class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:

        try:
            chips.bet = int(input("How many chips you like to bet ?"))
        except:
            print("Sorry please provide an integer .")
        else:
            if chips.bet > chips.total:
                print("Sorry you do not have enough chips! You have: {}".format(
                    chips.total))
            else:
                break


def hit(deck, hand):

    single_card = deck.deal()
    hand.add_cards(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Hit or stand? Enter h or s ')
        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False
        else:
            print("Sorry , I did no understand that, please h or s only!")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.values)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.values)


def player_busts(player, dealer, chips):
    print("BUST PLAYER")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("PLAYER WINS")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("PLAYER WINS! DEALER BUSTED")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("DEALER WINS")
    chips.lose_bet()


def push():
    print("Dealer and player tie! PUSH")


# game Play
while True:

    print("\t**WELCOME TO BLACK JACK**")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_cards(deck.deal())
    player_hand.add_cards(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_cards(deck.deal())
    dealer_hand.add_cards(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.values > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.values <= 21:

        while dealer_hand.values < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.values > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.values > player_hand.values:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.values < player_hand.values:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push()

    print("\n Player's total chips are {} ".format(player_chips.total))

    new_game = input("Would you like to play another hand ? y/n ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playig!!")
        break
