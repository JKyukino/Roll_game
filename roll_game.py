import random
def roll():
    point=[]
    for i in range(1,4):
        point.append(random.randrange(1,7))
    point.append(point[0]+point[1]+point[2])
    return point
def game_result(x):
    print('<<<<< ROLE THE DICE!>>>>>')
    if (x >= 11 and x <= 18):
       y = 'Big'
    else:
       y = 'Small'
    return y
coin=1000
while coin > 0:
    print('<<<<< GAME START! >>>>>')
    choice = input('Big or Small:')
    bet_coin = int(input('How much you wanna bet ? -'))
    while coin-bet_coin<0:
        print('error')
        bet_coin = int(input('How much you wanna bet ? -'))
    coin=coin-bet_coin
    point=roll()
    y=game_result(point[3])
    if choice == y:
       print('The points are [{},{},{}] You Win!'.format(point[0],point[1],point[2]))
       coin = coin + 2 * bet_coin
       print('You gained {},you have {} now'.format(bet_coin, coin))
    else:
       print('The points are [{},{},{}] You Lose!'.format(point[0],point[1],point[2]))
       print('You lost {},you have {} now'.format(bet_coin, coin))
