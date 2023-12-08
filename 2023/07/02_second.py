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
            if card == 'J':
                pass
            else:
                count = hand_str.count(card)            
                counts.append(count)
        wildcards = hand_str.count('J')
        self.wildcards = wildcards
        wild_counts = list(map(lambda c: c+wildcards, counts))
        self.wild_counts = wild_counts
        #counts.append(hand_str.count('J'))

        self.counts = counts

        self.cardValues = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':1,'Q':12,'K':13,'A':14}

        self.value = 0
        self.setValue()

    def isFiveOfKind(self):
        if 5 in self.counts or 5 in self.wild_counts or self.hand_str.count('J') == 5:
            return True
        else:
            return False
       
    def isFourOfKind(self):
        if 4 in self.counts or 4 in self.wild_counts:
            return True
        else:
            return False
       
    def isFullHouse(self):
        if 3 in self.counts and 2 in self.counts:
            return True
        elif self.counts.count(2) == 2 and self.wildcards > 0:
            return True
        elif self.counts.count(2) == 1 and self.wildcards > 1:
            return True
        else:
            return False
       
    def isThreeOfKind(self):
        if 3 in self.counts or 3 in self.wild_counts:
            return True
        else:
            return False
       
    def isTwoPairs(self):
        if self.counts.count(2) == 2:
            return True
        elif self.counts.count(2) == 1 and self.wild_counts.count(2) == 2:
            return True
        else:
            return False
       
    def isOnePair(self):
        if 2 in self.counts or 2 in self.wild_counts:
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
    #if 'J' in h.hand_str:
    print ("%s %4d %13s %d"%(h.hand_str, bet, h.type, h.value))
    sum += bet * x

print ("Sum:", sum)

# 247751666 is too low