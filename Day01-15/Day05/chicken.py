# 100元 買100隻雞 公雞(cock) 5元; 母雞(hen) 3元; 小雞(chick) 3隻一元

for cock in range(0, 20):
    for hen in range(0, 33):
        chick = 100 - cock - hen
        if 5 * cock + 3 * hen + chick / 3 == 100:
            print('公雞: %d隻, 母雞: %d隻, 小雞: %d隻' % (cock, hen, chick))