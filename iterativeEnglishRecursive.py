def iteRuler(rulerLength, maxxLength ):
    if( maxxLength <= 2 ):
        print("maxxLength can not be lower than 3!")
        return

    rulerIter = 1
    tmpMaxLength = maxxLength
    dash = '-\n--\n-\n'
    for i in range(0, rulerLength):
        for j in range(0, (2 ** ( maxxLength - 3 ))):
            x = j+1/2
            if( j == 0 and i == 0 ):
                print('-' * tmpMaxLength + str(j))
            elif(int(x)%2==1 ):
                print( dash + '-' * 3)
            elif(int(x)%2==0 and j!=0):
                print( dash + '-' * (tmpMaxLength - 1 ))
        print( dash + '-' * maxxLength  + str(rulerIter) )
        rulerIter = rulerIter + 1
iteRuler(1,2)