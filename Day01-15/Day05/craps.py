from random import randint

money = 1000

while money > 0:
    print('總資產為%d:' %(money))
    needs_go_on = False
    while True:
        debt = int(input('請下注'))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家骰出%d點' % (first))
    if first == 7 or first == 11:
        print('player win')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('banker win')
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('玩家骰出%d點' % (current))
        if current == 7:
            print('banker win')
            money -= debt
        elif current == first:
            print('player win')
            money += debt
        else:
            needs_go_on = True
print('你破產了')