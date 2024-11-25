import cards

d = cards.Deck(1)
d.shuffle()
dealer = cards.Hand()
player1 = cards.Hand()

players = [player1, dealer]

play = True
while play:

    for deal in range(2):
        #2 cards initially to each player + dealer
        for idx, hand in enumerate(players):
            #each player
            hand.draw_card(d)

    dealer.hand[0].hideCard(True)

    print("dealer: ", end='\t')
    dealer.print_hand()

    print("player 1: ", end='\t')
    player1.print_hand()    

    for idx, hand in enumerate(players):
        #each player gets a chance to hit or stay
        pass

    dealer.hand[0].hideCard(False)

    dealer_value = dealer.value
    while dealer_value < 17:
        #dealer hits until they have a value of at least 17
        dealer.draw_card(d)
        dealer_value = dealer.value

    play = False

print("dealer: ", end='\t')
dealer.print_hand()

print("player 1: ", end='\t')
player1.print_hand()