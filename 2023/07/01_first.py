import os

script_path = os.path.dirname(os.path.abspath(__file__))

filename = '_sample.txt'
filename = '_input.txt'

input_file = open(os.path.join(script_path, filename))

class hand:
    def __init__(self, hand_str):
        self.hand_str = hand_str
        self._sorted_unique_hand = sorted(set(self.hand_str))

        counts = []
        for card in self._sorted_unique_hand:
            counts.append(hand_str.count(card))
        self.counts = counts

        self.cardValues = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}

        self.value = 0
        self.setValue()

    def isFiveOfKind(self):
        if 5 in self.counts:
            return True
        else:
            return False
       
    def isFourOfKind(self):
        if 4 in self.counts:
            return True
        else:
            return False
       
    def isFullHouse(self):
        if 3 in self.counts and 2 in self.counts:
            return True
        else:
            return False
       
    def isThreeOfKind(self):
        if 3 in self.counts and not 2 in self.counts:
            return True
        else:
            return False
       
    def isTwoPairs(self):
        if self.counts.count(2) == 2:
            return True
        else:
            return False
       
    def isOnePair(self):
        if 2 in self.counts and not 3 in self.counts:
            return True
        else:
            return False
   
    def setValue(self):
        if self.isFiveOfKind():
            self.value += 60000000
            self.type = "FiveOfKind"
        elif self.isFourOfKind():
            self.value += 50000000
            self.type = "FourOfKind"
        elif self.isFullHouse():
            self.value += 40000000
            self.type = "FullHouse"
        elif self.isThreeOfKind():
            self.value += 30000000
            self.type = "ThreeOfKind"
        elif self.isTwoPairs():
            self.value += 20000000
            self.type = "TwoPairs"
        elif self.isOnePair():
            self.value += 10000000
            self.type = "OnePair"
        else:
            self.type = "HighCard"
        for x in range(len(self.hand_str)):
            card = self.hand_str[x]
            cardvalue = self.cardValues[card]
            factor = pow(14,5-x)
            self.value += self.cardValues[card] * factor

    def __cmp__(self, other):
        return self.value - other.value
    def __lt__(self, other):
        return self.value < other.value

hands = []

for line in input_file:
    hand_str, bet = line.strip().split()
    hands.append((hand(hand_str), bet))

sorted_hands = sorted(hands, key=lambda h: h[0])

# for h in sorted_hands:
#     print (h[0].hand_str, h[0].value)

sum = 0
for x in range(1,len(sorted_hands)+1):
    h = sorted_hands[x-1][0]
    bet = int(sorted_hands[x-1][1])
    print ("%s %4d %13s %d"%(h.hand_str, bet, h.type, h.value))
    sum += bet * x
print ("Len hands:", len(hands))
print ("Len sorted:", len(sorted_hands))

print ("Sum:", sum)

# 249773625 is too high
# 249748283