import random

SUITS = ["Diamonds", "Hearts", "Clubs", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Quenn", "King", "Ace"]

class Card():
  def __init__(self, new_rank, new_suit):
    self.rank = new_rank
    self.suit = new_suit

  def __repr__(self):
    return self.rank + " of " + self.suit
  
deck = []
for suit in SUITS:
  for rank in RANKS:
    deck.append(Card(rank, suit))
random.shuffle(deck)

p1 = deck[0:5]

rank_list = {}
for rank in RANKS:
    rank_list[rank] = 0

for card in p1:
    rank_list[card.rank] += 1
flush = True
for card in p1:
    if p1[0].suit == card.suit:
        pass
    else: flush = False
rank_list = list(rank_list.values())
if rank_list == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1] and flush:
    print("Cheater or extremely lucky but its more likely that you cheat so die")

elif str(rank_list).count("11111")== 1 and flush:
    print("straeight flooooooooosh")

elif rank_list.count(4) == 1:
    print("4 ov an kined")

elif rank_list.count(3) == 1 and rank_list.count(2) == 1:
    print("ful howse")

elif flush:
    print("flooooooooosh")

elif str(rank_list).count("11111")== 1:
    print("straeight")

elif rank_list.count(3) == 1:
    print("threee")

elif rank_list.count(2) == 2:
    print("tuo piar")

elif rank_list.count(2) == 1:
    print("onae pair")
else:
    print("you and your hand are garbage")
#mispelled and no ending aka besst