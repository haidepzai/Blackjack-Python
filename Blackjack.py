import random

# deck = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A')

cards = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}


class Dealer:
    hand = []  # Liste mit Keys-Value Paare
    is_ass = False

    def __init__(self, hand1, hand2):
        self.hand1 = hand1
        self.hand2 = hand2
        Dealer.hand.append(hand1)
        Dealer.hand.append(hand2)
        if 'A' in self.hand:
            self.is_ass = True
            print("Ass True")

    def __str__(self):
        return "Dealer Hand: %s und X" % str(self.hand[0])

    def draw(self):
        new_card = random.choice(list(cards.keys()))
        print("Dealer hat " + str(new_card) + " gezogen")
        Dealer.hand.append(new_card)  # Karte in Array hinzufügen
        if 'A' in self.hand:
            self.is_ass = True
            print("Ass True")

    def print_hand(self):
        print("Dealer Hand: " + ", ".join(self.hand))

    def sum_of_cards(self):
        return sum([cards[key] for key in self.hand])

    def kalk_wert(self):
        if self.is_ass is True and self.sum_of_cards() < 12:
            return self.sum_of_cards() + 10
        else:
            return self.sum_of_cards()


class Player:
    hand = []  # Liste mit Keys z.B ['2', 'K', '5']
    is_ass = False

    def __init__(self):
        Player.hand.append(random.choice(list(cards.keys())))  # Typecasting in List
        Player.hand.append(random.choice(list(cards.keys())))  # Random Key
        if 'A' in self.hand:
            self.is_ass = True
            print("Ass True")

    def __str__(self):
        return "Deine Hand: %s und %s" % (self.hand[0], self.hand[1])

    def draw(self):
        new_card = random.choice(list(cards.keys()))
        print("Du hast " + str(new_card) + " gezogen")
        Player.hand.append(new_card)  # Karte in Array hinzufügen
        if 'A' in self.hand:
            self.is_ass = True
            print("Ass True")

    def print_hand(self):
        print("Deine Hand: " + ", ".join(self.hand))  # macht aus der Liste -> 2, k, 5

    def sum_of_cards(self):  # Summe der Karten in der Hand
        return sum([cards[key] for key in self.hand])
        # Erstelle eine Liste -> Für jede Key in Hand -> Appende den Value und addiere

    def kalk_wert(self):  # Berechnet je nachdem, ob man ein Ass gezogen hat
        if self.is_ass is True and self.sum_of_cards() < 12:  # Falls Summe der Karten unter 12 ist und man Ass zieht
            return self.sum_of_cards() + 10                   # Ass = 11
        else:
            return self.sum_of_cards()


k = random.choice(list(cards.keys()))  # random Key aus dict
pair1 = (k)
k = random.choice(list(cards.keys()))
pair2 = (k)

dealer = Dealer(pair1, pair2)
player = Player()

print("Willkommen bei Blackjack")
print(dealer)
print(player)
print("Die Summe deiner Hand beträgt: " + str(player.kalk_wert()))

busted = False

while True:
    player_choice = input("Was möchtest du tun? Hit (H) oder Stand (S)?").lower()

    if player_choice == 'h':
        player.draw()
    elif player_choice == 's':
        break
    else:
        print("Ungültige Eingabe")
        continue

    player.print_hand()
    print("Die Summe deiner Hand beträgt: " + str(player.kalk_wert()))
    if player.kalk_wert() == 21:
        print("Blackjack!")
        break
    elif player.kalk_wert() > 21:
        print("Du hast überzogen!")
        busted = True
        break

if not busted:
    dealer.print_hand()
    print("Summe Dealer: " + str(dealer.kalk_wert()))
    while dealer.kalk_wert() <= 17:
        dealer.draw()
        dealer.print_hand()
        print("Summe Dealer: " + str(dealer.kalk_wert()))

    if dealer.kalk_wert() > 21:
        print("Dealer bustet")
    elif dealer.kalk_wert() > player.kalk_wert():
        print("Dealer hat gewonnen")
    else:
        print("Glückwunsch, du hast geownnen")
