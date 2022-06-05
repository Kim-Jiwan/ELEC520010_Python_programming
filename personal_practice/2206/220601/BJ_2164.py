N = int(input())
cards = [ num for num in range(1, N + 1) ]


while len(cards) > 1:
    cards.pop(0)
    tmp = cards.pop(0)
    cards.append(tmp)

print(cards[0])