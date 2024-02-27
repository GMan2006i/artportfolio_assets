import random
import re
def lb():print('')
deck = ['A*','A$','A^','A@', '2*','2$','2^','2@', '3*','3$','3^','3@', '4*','4$','4^','4@', '5*','5$','5^','5@', '6*','6$','6^','6@', '7*','7$','7^','7@', '8*','8$','8^','8@', '9*','9$','9^','9@', '10*','10$','10^','10@', 'J*','J$','J^','J@', 'Q*','Q$','Q^','Q@', 'K*','K$','K^','K@']
yourHand = []
oppsHand = []
def augh(penis):
    penis = str(penis)
    penis=re.sub('[*$^@]',"",penis)
    return penis
def draw(player,amount=1):
    if len(deck) > 0:
        for i  in range(int(amount)):
            if player == 1:
                yourHand.append(str(deck[random.randint(0,(len(deck)-1))]))
                deck.remove(str(yourHand[-1]))
                if len(deck) > 0:
                            lb()
                            print('No more cards to deal!')
                            lb()
                            break
            else:
                oppsHand.append(str(deck[random.randint(0,(len(deck)-1))]))
                deck.remove(str(oppsHand[-1]))
                if len(deck) > 0:
                            lb()
                            print('No more cards to deal!')
                            lb()
                            break
    else:
        lb()
        print('No more cards to deal!')
draw(1,7)
draw(2,7)
playing = True
def winner(player):
    if player == 1:
        print('You win the hand. Opponent draws 2 cards.')
        draw(2,2)
    else:
        print('You lost the hand. You draw 2 cards.')
        draw(1,2)
    lb()
while playing == True:
    print("Opponent's First Card:")
    print(oppsHand[0])
    lb()
    print('Your Hand:')
    print(yourHand)
    choicePlayer = input('Choose a Card\n')
    yourHand.remove(choicePlayer)
    oppsChoice = str(oppsHand[random.randint(0,(len(oppsHand)-1))])
    oppsHand.remove(oppsChoice)
    lb()
    print('You played: '+choicePlayer)
    print('Your Opponent played: '+oppsChoice)
    lb()
    if choicePlayer[:1] == 'K':
        choicePlayer=choicePlayer.replace('K','13')
    elif choicePlayer[:1] == 'Q':
        choicePlayer=choicePlayer.replace('Q','12')
    elif choicePlayer[:1] == 'J':
        choicePlayer=choicePlayer.replace('J','11')
    elif choicePlayer[:1] == 'A':
        choicePlayer=choicePlayer.replace('A','1')
    if oppsChoice[:1] == 'K':
        oppsChoice=oppsChoice.replace('K','13')
    elif oppsChoice[:1] == 'Q':
        oppsChoice=oppsChoice.replace('Q','12')
    elif oppsChoice[:1] == 'J':
        oppsChoice=oppsChoice.replace('J','11')
    elif oppsChoice[:1] == 'A':
        oppsChoice=oppsChoice.replace('A','1')
    ##win logic shit
    if int(augh(choicePlayer)) > int(augh(oppsChoice)):
        winner(1)
    elif int(augh(choicePlayer)) < int(augh(oppsChoice)):
        winner(2)
    elif int(augh(choicePlayer)) == int(augh(oppsChoice)):
        e = choicePlayer[-1]
        d = oppsChoice[-1]
        cum=['*','$','^','@']
        if int(cum.index(e)) > int(cum.index(d)):
            winner(1)
        else:
            winner(2)
    else:
        print('ERROR!!!')
        exit()
    if len(yourHand) == 0:
        playing = False
        lb()
        print('A Winner is You!')
        exit()
    if len(oppsHand) == 0:
        playing = False
        lb()
        print('You Suck!')
        exit()