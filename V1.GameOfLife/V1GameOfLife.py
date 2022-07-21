import random
print('Hello , Welcome to the GAME OF LIFE.')
r=input('Are you ready to play ? (Y/N) ')
money=500
knowledge=0
happiness=0
loans=0
spouse=0
child=0
place=0
if r.upper()=='Y':
    print()
    print('OK, you have started with 500 credits. over the course of the game you can spend and earn money so use it wisely.')
    print()
    print('you have two stats called knowledge and happiness both start at 0 , over the course of the game you can earn them for bonus points. ')
    print()
    print('Ok then , lets start')
    print()
    def T1():
        global money
        global happiness
        print('ACTION')
        print('1) Get Guitar Lessons. (200 credits)')
        print('2) build a tree house. (happiness +1)')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You got some guitar lessons.')
            print(' -200 credits ')
            print('next turn')
            money=money-200
        elif a1==2:
            print('You built a Tree house. ')
            print(' happiness + 1')
            print('next turn')
            happiness=happiness+1
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
    def T2():
        global money
        global happiness
        global knowledge
        print('ACTION')
        print('1) Get a PC upgrade. (200 credits & knowledge +2)')
        print('2) Go to the amusement park. (100 credits & happiness +1)')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You got a PC upgrade.')
            print(' -200 credits & knowledge + 2 ')
            print('next turn')
            money=money-200
            knowledge=knowledge+2
        elif a1==2:
            print('You went to the amusement park. ')
            print('-100 credits & happiness + 1')
            print('next turn')
            happiness=happiness+1
            money=money-100
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
    def T3():
        global money
        print('TAXES')
        print('Pay 50 credits to the gov. as taxes.')
        print('next turn')
        money=money-50
    def T4():
        global money
        global happiness
        print('ACTION')
        print('1) Win a lottery. (+200 credits)')
        print('2) build a tree house. (happiness +1)')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You won a lottery.')
            print(' +200 credits ')
            print('next turn')
            money=money+200
        elif a1==2:
            print('You built a Tree house. ')
            print(' happiness + 1')
            print('next turn')
            happiness=happiness+1
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
    def T5():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+150 credits')
        print('next turn')
        money=money+150
    def T6():
        global money
        global knowledge
        global loans
        print('ACTION')
        print('1) Go to college. (200 credits & knowledge +2)')
        print('2) work as a lawn mower for neighbour. (+50 credits)')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You went to the college.')
            print(' -200 credits & knowledge + 2')
            print('next turn')
            money=money-200
            knowledge=knowledge+2
        elif a1==2:
            print('You mowed a lawn. ')
            print(' +50 credits')
            print('next turn')
            money=money+50
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T7():
        global money
        global happiness
        global loans
        print('ACTION')
        print('1) buy an art piece. (100 credits & happiness +1)')
        print('2) do nothing.')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You bought an art piece.')
            print(' -100 credits & happiness + 1')
            print('next turn')
            money=money-100
            happiness=happiness+1
        elif a1==2:
            print('You did nothing. ')
            print('next turn')
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T8():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+150 credits')
        print('next turn')
        money=money+150
    def T9():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+100 credits')
        print('next turn')
        money=money+100
    def T10():
        global money
        print('TAXES')
        print('Pay 100 credits to the gov. as taxes.')
        print('next turn')
        money=money-100
    def T11():
        global money
        global happiness
        global loans
        print('EVENT')
        print('YOU GOT ROBBED')
        print(' -200 credits & happiness -2')
        print('next turn')
        money=money-200
        happiness=happiness-2
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T12():
        global money
        global happiness
        global knowledge
        print('ACTION')
        print('1) Get a PC upgrade. (200 credits & knowledge +2)')
        print('2) Go to the amusement park. (100 credits & happiness +1)')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You got a PC upgrade.')
            print(' -200 credits & knowledge + 2 ')
            print('next turn')
            money=money-200
            knowledge=knowledge+2
        elif a1==2:
            print('You went to the amusement park. ')
            print('-100 credits & happiness + 1')
            print('next turn')
            happiness=happiness+1
            money=money-100
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T13():
        global loans
        global money
        global happiness
        print('ACTION')
        print('1) start video blogs. (50 credits & happiness +1)')
        print('2) do nothing.')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You got some guitar lessons.')
            print(' -50 credits & happiness +1 ')
            print('next turn')
            money=money-50
            happiness=happiness+1
        elif a1==2:
            print('You did nothing. ')
            print('next turn')
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T14():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+150 credits')
        print('next turn')
        money=money+150
    def T15():
        global money
        print('TAXES')
        print('Pay 100 credits to the gov. as taxes.')
        print('next turn')
        money=money-100
    def T16():
        global money
        global happiness
        global loans
        print('ACTION')
        print('1) buy an art piece. (100 credits & happiness +1)')
        print('2) do nothing.')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You bought an art piece.')
            print(' -100 credits & happiness + 1')
            print('next turn')
            money=money-100
            happiness=happiness+1
        elif a1==2:
            print('You did nothing. ')
            print('next turn')
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T17():
        global money
        global happiness
        global loans
        print('EVENT')
        print('YOU GOT ROBBED')
        print(' -200 credits & happiness -2')
        print('next turn')
        money=money-200
        happiness=happiness-2
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T18():
        global money
        global happiness
        print('EVENT')
        print('YOU WON A MEGA LOTTERY')
        print(' +1000 credits & happiness +4')
        print('next turn')
        money=money+1000
        happiness=happiness+4
    def T19():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+150 credits')
        print('next turn')
        money=money+150
    def T20():
        global money
        global spouse
        global happiness
        print('EVENT')
        print('you got married')
        print('+400 credits & happiness +4')
        print('next turn')
        money=money+400
        spouse=spouse+1
        happiness=happiness+4
    def T21():
        global money
        global happiness
        global loans
        print('EVENT')
        print('YOU GOT ROBBED')
        print(' -200 credits & happiness -2')
        print('next turn')
        money=money-200
        happiness=happiness-2
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T22():
        global money
        global happiness
        global knowledge
        print('ACTION')
        print('1) Get a PC upgrade. (200 credits & knowledge +2)')
        print('2) Go to the amusement park. (100 credits & happiness +1)')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You got a PC upgrade.')
            print(' -200 credits & knowledge + 2 ')
            print('next turn')
            money=money-200
            knowledge=knowledge+2
        elif a1==2:
            print('You went to the amusement park. ')
            print('-100 credits & happiness + 1')
            print('next turn')
            happiness=happiness+1
            money=money-100
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
    def T23():
        global money
        global loans
        print('FATE')
        print('roll a random number and get a reward/penalty.')
        input('Press enter to roll...')
        n = random.randint(1,10)
        if 1<=n<=5:
            print('you recieved 50 credits via a lucky draw')
            money=money+50
        elif 6<=n<=10:
            print('you recieved a 50 credit penalty.')
            money=money-50
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T24():
        global money
        global happiness
        global loans
        print('ACTION')
        print('1) buy an art piece. (100 credits & happiness +1)')
        print('2) do nothing.')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You bought an art piece.')
            print(' -100 credits & happiness + 1')
            print('next turn')
            money=money-100
            happiness=happiness+1
        elif a1==2:
            print('You did nothing. ')
            print('next turn')
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T25():
        global money
        global happiness
        global knowledge
        print('ACTION')
        print('1) Get a PC upgrade. (200 credits & knowledge +2)')
        print('2) Go to the amusement park. (100 credits & happiness +1)')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You got a PC upgrade.')
            print(' -200 credits & knowledge + 2 ')
            print('next turn')
            money=money-200
            knowledge=knowledge+2
        elif a1==2:
            print('You went to the amusement park. ')
            print('-100 credits & happiness + 1')
            print('next turn')
            happiness=happiness+1
            money=money-100
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T26():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+150 credits')
        print('next turn')
        money=money+150
    def T27():
        global money
        global happiness
        print('EVENT')
        print('YOU LOST A BET')
        print(' -100 credits & happiness -2')
        print('next turn')
        money=money-100
        happiness=happiness-2
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T28():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+150 credits')
        print('next turn')
        money=money+150
    def T29():
        global money
        global spouse
        global happiness
        print('EVENT')
        print('you got married')
        print('+400 credits & happiness +4')
        print('next turn')
        money=money+400
        spouse=spouse+1
        happiness=happiness+4
    def T30():
        global money
        global happiness
        global loans
        print('EVENT')
        print('YOU GOT ROBBED')
        print(' -200 credits & happiness -2')
        print('next turn')
        money=money-200
        happiness=happiness-2
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T31():
        global money
        global loans
        print('FATE')
        print('roll a random number and get a reward/penalty.')
        input('Press enter to roll...')
        n = random.randint(1,10)
        if 1<=n<=5:
            print('you recieved 50 credits via a lucky draw')
            money=money+50
        elif 6<=n<=10:
            print('you recieved a 50 credit penalty.')
            money=money-50
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T32():
        global money
        global loans
        global happiness
        print('FATE')
        print('roll a random number and get a reward/penalty.')
        input('Press enter to roll...')
        n = random.randint(1,10)
        if 1<=n<=3:
            print('you recieved 50 credits via a lucky draw')
            money=money+50
        elif 4<=n<=6:
            print('you recieved a 50 credit penalty.')
            money=money-50
        elif 7<=n<=10:
            print('You helped an old lady cross the road. happiness +1')
            happiness=happiness+1
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T33():
        global money
        global loans
        print('FATE')
        print('roll a random number and get a reward/penalty.')
        input('Press enter to roll...')
        n = random.randint(1,10)
        if 1<=n<=5:
            print('you recieved 50 credits via a lucky draw')
            money=money+50
        elif 6<=n<=10:
            print('you recieved a 50 credit penalty.')
            money=money-50
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T34():
        global money
        global loans
        global happiness
        print('FATE')
        print('roll a random number and get a reward/penalty.')
        input('Press enter to roll...')
        n = random.randint(1,10)
        if 1<=n<=3:
            print('you recieved 50 credits via a lucky draw')
            money=money+50
        elif 4<=n<=6:
            print('you recieved a 50 credit penalty.')
            money=money-50
        elif 7<=n<=10:
            print('You found 200 credits on the ground. +200 credits & happiness -1')
            money=money+200
            happiness=happiness-1
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T35():
        global money
        global loans
        print('FATE')
        print('roll a random number and get a reward/penalty.')
        input('Press enter to roll...')
        n = random.randint(1,10)
        if 1<=n<=5:
            print('you recieved 50 credits via a lucky draw')
            money=money+50
        elif 6<=n<=10:
            print('you recieved a 50 credit penalty.')
            money=money-50
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T36():
        global money
        global happiness
        global loans
        print('EVENT')
        print('YOU GOT ROBBED')
        print(' -200 credits & happiness -2')
        print('next turn')
        money=money-200
        happiness=happiness-2
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T37():
        global money
        global happiness
        global loans
        print('EVENT')
        print('YOU GOT ROBBED')
        print(' -200 credits & happiness -2')
        print('next turn')
        money=money-200
        happiness=happiness-2
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T38():
        global money
        global happiness
        global knowledge
        print('ACTION')
        print('1) Get a PC upgrade. (200 credits & knowledge +2)')
        print('2) Go to the amusement park. (100 credits & happiness +1)')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You got a PC upgrade.')
            print(' -200 credits & knowledge + 2 ')
            print('next turn')
            money=money-200
            knowledge=knowledge+2
        elif a1==2:
            print('You went to the amusement park. ')
            print('-100 credits & happiness + 1')
            print('next turn')
            happiness=happiness+1
            money=money-100
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T39():
        global loans
        global money
        global happiness
        print('ACTION')
        print('1) start video blogs. (50 credits & happiness +1)')
        print('2) do nothing.')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You got some guitar lessons.')
            print(' -50 credits & happiness +1 ')
            print('next turn')
            money=money-50
            happiness=happiness+1
        elif a1==2:
            print('You did nothing. ')
            print('next turn')
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T40():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+150 credits')
        print('next turn')
        money=money+150
    def T41():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+150 credits')
        print('next turn')
        money=money+150
    def T42():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+150 credits')
        print('next turn')
        money=money+150
    def T43():
        global money
        global happiness
        global knowledge
        print('ACTION')
        print('1) Get a PC upgrade. (200 credits & knowledge +2)')
        print('2) Go to the amusement park. (100 credits & happiness +1)')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You got a PC upgrade.')
            print(' -200 credits & knowledge + 2 ')
            print('next turn')
            money=money-200
            knowledge=knowledge+2
        elif a1==2:
            print('You went to the amusement park. ')
            print('-100 credits & happiness + 1')
            print('next turn')
            happiness=happiness+1
            money=money-100
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T44():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+150 credits')
        print('next turn')
        money=money+150
    def T45():
        global money
        global happiness
        print('EVENT')
        print('YOU LOST A BET')
        print(' -100 credits & happiness -2')
        print('next turn')
        money=money-100
        happiness=happiness-2
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T46():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+150 credits')
        print('next turn')
        money=money+150
    def T47():
        global money
        global spouse
        global happiness
        print('EVENT')
        print('you got married')
        print('+400 credits & happiness +4')
        print('next turn')
        money=money+400
        spouse=spouse+1
        happiness=happiness+4
    def T48():
        global money
        global happiness
        global loans
        print('EVENT')
        print('YOU GOT ROBBED')
        print(' -200 credits & happiness -2')
        print('next turn')
        money=money-200
        happiness=happiness-2
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T49():
        global money
        global child
        global happiness
        print('EVENT')
        print('you adopted a kid')
        print('+400 credits & happiness +4')
        print('next turn')
        money=money+400
        child=child+1
        happiness=happiness+4
    def T50():
        global money
        global happiness
        global loans
        print('EVENT')
        print('YOU GOT ROBBED')
        print(' -200 credits & happiness -2')
        print('next turn')
        money=money-200
        happiness=happiness-2
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T51():
        global money
        global happiness
        global loans
        print('ACTION')
        print('1) Get Guitar Lessons. (200 credits)')
        print('2) build a tree house. (happiness +1)')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You got some guitar lessons.')
            print(' -200 credits ')
            print('next turn')
            money=money-200
        elif a1==2:
            print('You built a Tree house. ')
            print(' happiness + 1')
            print('next turn')
            happiness=happiness+1
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T52():
        global money
        global happiness
        global knowledge
        global loans
        print('ACTION')
        print('1) Get a PC upgrade. (200 credits & knowledge +2)')
        print('2) Go to the amusement park. (100 credits & happiness +1)')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You got a PC upgrade.')
            print(' -200 credits & knowledge + 2 ')
            print('next turn')
            money=money-200
            knowledge=knowledge+2
        elif a1==2:
            print('You went to the amusement park. ')
            print('-100 credits & happiness + 1')
            print('next turn')
            happiness=happiness+1
            money=money-100
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T53():
        global money
        print('TAXES')
        print('Pay 50 credits to the gov. as taxes.')
        print('next turn')
        money=money-50
    def T54():
        global money
        global happiness
        print('ACTION')
        print('1) Win a lottery. (+200 credits)')
        print('2) build a tree house. (happiness +1)')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You won a lottery.')
            print(' +200 credits ')
            print('next turn')
            money=money+200
        elif a1==2:
            print('You built a Tree house. ')
            print(' happiness + 1')
            print('next turn')
            happiness=happiness+1
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
    def T55():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+150 credits')
        print('next turn')
        money=money+150
    def T56():
        global money
        global knowledge
        global loans
        print('ACTION')
        print('1) Go to college. (200 credits & knowledge +2)')
        print('2) work as a lawn mower for neighbour. (+50 credits)')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You went to the college.')
            print(' -200 credits & knowledge + 2')
            print('next turn')
            money=money-200
            knowledge=knowledge+2
        elif a1==2:
            print('You mowed a lawn. ')
            print(' +50 credits')
            print('next turn')
            money=money+50
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T57():
        global money
        global happiness
        global loans
        print('ACTION')
        print('1) buy an art piece. (100 credits & happiness +1)')
        print('2) do nothing.')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You bought an art piece.')
            print(' -100 credits & happiness + 1')
            print('next turn')
            money=money-100
            happiness=happiness+1
        elif a1==2:
            print('You did nothing. ')
            print('next turn')
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T58():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+150 credits')
        print('next turn')
        money=money+150
    def T59():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+100 credits')
        print('next turn')
        money=money+100
    def T60():
        global money
        print('TAXES')
        print('Pay 100 credits to the gov. as taxes.')
        print('next turn')
        money=money-100
    def T61():
        global money
        global happiness
        global loans
        print('EVENT')
        print('YOU GOT ROBBED')
        print(' -200 credits & happiness -2')
        print('next turn')
        money=money-200
        happiness=happiness-2
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T62():
        global money
        global happiness
        global knowledge
        print('ACTION')
        print('1) Get a PC upgrade. (200 credits & knowledge +2)')
        print('2) Go to the amusement park. (100 credits & happiness +1)')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You got a PC upgrade.')
            print(' -200 credits & knowledge + 2 ')
            print('next turn')
            money=money-200
            knowledge=knowledge+2
        elif a1==2:
            print('You went to the amusement park. ')
            print('-100 credits & happiness + 1')
            print('next turn')
            happiness=happiness+1
            money=money-100
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T63():
        global loans
        global money
        global happiness
        print('ACTION')
        print('1) start video blogs. (50 credits & happiness +1)')
        print('2) do nothing.')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You got some guitar lessons.')
            print(' -50 credits & happiness +1 ')
            print('next turn')
            money=money-50
            happiness=happiness+1
        elif a1==2:
            print('You did nothing. ')
            print('next turn')
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T64():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+150 credits')
        print('next turn')
        money=money+150
    def T65():
        global money
        print('TAXES')
        print('Pay 100 credits to the gov. as taxes.')
        print('next turn')
        money=money-100
    def T66():
        global money
        global happiness
        global loans
        print('ACTION')
        print('1) buy an art piece. (100 credits & happiness +1)')
        print('2) do nothing.')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You bought an art piece.')
            print(' -100 credits & happiness + 1')
            print('next turn')
            money=money-100
            happiness=happiness+1
        elif a1==2:
            print('You did nothing. ')
            print('next turn')
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T67():
        global money
        global happiness
        global loans
        print('EVENT')
        print('YOU GOT ROBBED')
        print(' -200 credits & happiness -2')
        print('next turn')
        money=money-200
        happiness=happiness-2
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T68():
        global money
        global happiness
        print('EVENT')
        print('YOU WON A MEGA LOTTERY')
        print(' +1000 credits & happiness +4')
        print('next turn')
        money=money+1000
        happiness=happiness+4
    def T69():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+150 credits')
        print('next turn')
        money=money+150
    def T70():
        global money
        global spouse
        global happiness
        print('EVENT')
        print('you got married')
        print('+400 credits & happiness +4')
        print('next turn')
        money=money+400
        spouse=spouse+1
        happiness=happiness+4
    def T71():
        global money
        global happiness
        global loans
        print('EVENT')
        print('YOU GOT ROBBED')
        print(' -200 credits & happiness -2')
        print('next turn')
        money=money-200
        happiness=happiness-2
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T72():
        global money
        global happiness
        global knowledge
        print('ACTION')
        print('1) Get a PC upgrade. (200 credits & knowledge +2)')
        print('2) Go to the amusement park. (100 credits & happiness +1)')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You got a PC upgrade.')
            print(' -200 credits & knowledge + 2 ')
            print('next turn')
            money=money-200
            knowledge=knowledge+2
        elif a1==2:
            print('You went to the amusement park. ')
            print('-100 credits & happiness + 1')
            print('next turn')
            happiness=happiness+1
            money=money-100
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
    def T73():
        global money
        global loans
        print('FATE')
        print('roll a random number and get a reward/penalty.')
        input('Press enter to roll...')
        n = random.randint(1,10)
        if 1<=n<=5:
            print('you recieved 50 credits via a lucky draw')
            money=money+50
        elif 6<=n<=10:
            print('you recieved a 50 credit penalty.')
            money=money-50
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T74():
        global money
        global happiness
        global loans
        print('ACTION')
        print('1) buy an art piece. (100 credits & happiness +1)')
        print('2) do nothing.')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You bought an art piece.')
            print(' -100 credits & happiness + 1')
            print('next turn')
            money=money-100
            happiness=happiness+1
        elif a1==2:
            print('You did nothing. ')
            print('next turn')
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T75():
        global money
        global happiness
        global knowledge
        print('ACTION')
        print('1) Get a PC upgrade. (200 credits & knowledge +2)')
        print('2) Go to the amusement park. (100 credits & happiness +1)')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You got a PC upgrade.')
            print(' -200 credits & knowledge + 2 ')
            print('next turn')
            money=money-200
            knowledge=knowledge+2
        elif a1==2:
            print('You went to the amusement park. ')
            print('-100 credits & happiness + 1')
            print('next turn')
            happiness=happiness+1
            money=money-100
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T76():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+150 credits')
        print('next turn')
        money=money+150
    def T77():
        global money
        global happiness
        print('EVENT')
        print('YOU LOST A BET')
        print(' -100 credits & happiness -2')
        print('next turn')
        money=money-100
        happiness=happiness-2
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T78():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+150 credits')
        print('next turn')
        money=money+150
    def T79():
        global money
        global spouse
        global happiness
        print('EVENT')
        print('you got married')
        print('+400 credits & happiness +4')
        print('next turn')
        money=money+400
        spouse=spouse+1
        happiness=happiness+4
    def T80():
        global money
        global happiness
        global loans
        print('EVENT')
        print('YOU GOT ROBBED')
        print(' -200 credits & happiness -2')
        print('next turn')
        mmoney=money-200
        happiness=happiness-2
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T81():
        global money
        global loans
        print('FATE')
        print('roll a random number and get a reward/penalty.')
        input('Press enter to roll...')
        n = random.randint(1,10)
        if 1<=n<=5:
            print('you recieved 50 credits via a lucky draw')
            money=money+50
        elif 6<=n<=10:
            print('you recieved a 50 credit penalty.')
            money=money-50
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T82():
        global money
        global loans
        global happiness
        print('FATE')
        print('roll a random number and get a reward/penalty.')
        input('Press enter to roll...')
        n = random.randint(1,10)
        if 1<=n<=3:
            print('you recieved 50 credits via a lucky draw')
            money=money+50
        elif 4<=n<=6:
            print('you recieved a 50 credit penalty.')
            money=money-50
        elif 7<=n<=10:
            print('You helped an old lady cross the road. happiness +1')
            happiness=happiness+1
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T83():
        global money
        global loans
        print('FATE')
        print('roll a random number and get a reward/penalty.')
        input('Press enter to roll...')
        n = random.randint(1,10)
        if 1<=n<=5:
            print('you recieved 50 credits via a lucky draw')
            money=money+50
        elif 6<=n<=10:
            print('you recieved a 50 credit penalty.')
            money=money-50
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T84():
        global money
        global loans
        global happiness
        print('FATE')
        print('roll a random number and get a reward/penalty.')
        input('Press enter to roll...')
        n = random.randint(1,10)
        if 1<=n<=3:
            print('you recieved 50 credits via a lucky draw')
            money=money+50
        elif 4<=n<=6:
            print('you recieved a 50 credit penalty.')
            money=money-50
        elif 7<=n<=10:
            print('You found 200 credits on the ground. +200 credits & happiness -1')
            money=money+200
            happiness=happiness-1
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T85():
        global money
        global loans
        print('FATE')
        print('roll a random number and get a reward/penalty.')
        input('Press enter to roll...')
        n = random.randint(1,10)
        if 1<=n<=5:
            print('you recieved 50 credits via a lucky draw')
            money=money+50
        elif 6<=n<=10:
            print('you recieved a 50 credit penalty.')
            money=money-50
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T86():
        global money
        global happiness
        global loans
        print('EVENT')
        print('YOU GOT ROBBED')
        print(' -200 credits & happiness -2')
        print('next turn')
        money=money-200
        happiness=happiness-2
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T87():
        global money
        global happiness
        global loans
        print('EVENT')
        print('YOU GOT ROBBED')
        print(' -200 credits & happiness -2')
        print('next turn')
        money=money-200
        happiness=happiness-2
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T88():
        global money
        global happiness
        global knowledge
        print('ACTION')
        print('1) Get a PC upgrade. (200 credits & knowledge +2)')
        print('2) Go to the amusement park. (100 credits & happiness +1)')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You got a PC upgrade.')
            print(' -200 credits & knowledge + 2 ')
            print('next turn')
            money=money-200
            knowledge=knowledge+2
        elif a1==2:
            print('You went to the amusement park. ')
            print('-100 credits & happiness + 1')
            print('next turn')
            happiness=happiness+1
            money=money-100
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T89():
        global loans
        global money
        global happiness
        print('ACTION')
        print('1) start video blogs. (50 credits & happiness +1)')
        print('2) do nothing.')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You got some guitar lessons.')
            print(' -50 credits & happiness +1 ')
            print('next turn')
            money=money-50
            happiness=happiness+1
        elif a1==2:
            print('You built a Tree house. ')
            print(' happiness + 1')
            print('next turn')
            happiness=happiness+1
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T90():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+150 credits')
        print('next turn')
        money=money+150
    def T91():
        global money
        global child
        global happiness
        print('EVENT')
        print('you adopted a kid')
        print('+400 credits & happiness +4')
        print('next turn')
        money=money+400
        child=child+1
        happiness=happiness+4
    def T92():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+150 credits')
        print('next turn')
        money=money+150
    def T93():
        global money
        global happiness
        global knowledge
        print('ACTION')
        print('1) Get a PC upgrade. (200 credits & knowledge +2)')
        print('2) Go to the amusement park. (100 credits & happiness +1)')
        a1=int(input('1 or 2 ?'))
        if a1==1:
            print('You got a PC upgrade.')
            print(' -200 credits & knowledge + 2 ')
            print('next turn')
            money=money-200
            knowledge=knowledge+2
        elif a1==2:
            print('You went to the amusement park. ')
            print('-100 credits & happiness + 1')
            print('next turn')
            happiness=happiness+1
            money=money-100
        else:
            print('SKIP')
            print('No action occured. ')
            print('next turn')
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T94():
        global money
        print('BANK')
        print('you landed on a bank')
        print('+150 credits')
        print('next turn')
        money=money+150
    def T95():
        global money
        global happiness
        print('EVENT')
        print('YOU LOST A BET')
        print(' -100 credits & happiness -2')
        print('next turn')
        money=money-100
        happiness=happiness-2
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T96():
        global money
        global loans
        global happiness
        print('FATE')
        print('roll a random number and get a reward/penalty.')
        input('Press enter to roll...')
        n = random.randint(1,10)
        if 1<=n<=3:
            print('you recieved 50 credits via a lucky draw')
            money=money+50
        elif 4<=n<=6:
            print('you recieved a 50 credit penalty.')
            money=money-50
        elif 7<=n<=10:
            print('You helped an old lady cross the road. happiness +1')
            happiness=happiness+1
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T97():
        global money
        global loans
        global happiness
        print('FATE')
        print('roll a random number and get a reward/penalty.')
        input('Press enter to roll...')
        n = random.randint(1,10)
        if 1<=n<=3:
            print('you recieved 50 credits via a lucky draw')
            money=money+50
        elif 4<=n<=6:
            print('you recieved a 50 credit penalty.')
            money=money-50
        elif 7<=n<=10:
            print('You helped an old lady cross the road. happiness +1')
            happiness=happiness+1
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T98():
        global money
        global happiness
        global loans
        print('EVENT')
        print('YOU GOT ROBBED')
        print(' -200 credits & happiness -2')
        print('next turn')
        money=money-200
        happiness=happiness-2
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50
    def T99():
        global money
        global happiness
        global loans
        print('EVENT')
        print('YOU GOT ROBBED')
        print(' -200 credits & happiness -2')
        print('next turn')
        money=money-200
        happiness=happiness-2
        if money<0:
            print('Looks like you ran out of money .. you need to take a loan.')
            while money<0:
                loans=loans+1
                money=money+50

    while place<100:
        print()
        print('You are currently at the ',place,' place on the board. ')
        input('press ENTER to roll the die ...')
        dr = random.randint(1,10)
        place=place+dr
        print()
        print(' You rolled a ',dr,' on the die')
        print('moving ahead ', dr,' places.')
        print()
        if place==1:
            T1()
        elif place==2:
            T2()
        elif place==3:
            T3()
        elif place==4:
            T4()
        elif place==5:
            T5()
        elif place==6:
            T6()
        elif place==7:
            T7()
        elif place==8:
            T8()
        elif place==9:
            T9()
        elif place==10:
            T10()
        elif place==11:
            T11()
        elif place==12:
            T12()
        elif place==13:
            T13()
        elif place==14:
            T14()
        elif place==15:
            T15()
        elif place==16:
            T16()
        elif place==17:
            T17()
        elif place==18:
            T18()
        elif place==19:
            T19()
        elif place==20:
            T20()
        elif place==21:
            T21()
        elif place==22:
            T22()
        elif place==23:
            T23()
        elif place==24:
            T24()
        elif place==25:
            T25()
        elif place==26:
            T26()
        elif place==27:
            T27()
        elif place==28:
            T28()
        elif place==29:
            T29()
        elif place==30:
            T30()
        elif place==31:
            T31()
        elif place==32:
            T32()
        elif place==33:
            T33()
        elif place==34:
            T34()
        elif place==35:
            T35()
        elif place==36:
            T36()
        elif place==37:
            T37()
        elif place==38:
            T38()
        elif place==39:
            T39()
        elif place==40:
            T40()
        elif place==41:
            T41()
        elif place==42:
            T42()
        elif place==43:
            T43()
        elif place==44:
            T44()
        elif place==45:
            T45()
        elif place==46:
            T46()
        elif place==47:
            T47()
        elif place==48:
            T48()
        elif place==49:
            T49()
        elif place==50:
            T50()
        elif place==51:
            T51()
        elif place==52:
            T52()
        elif place==53:
            T53()
        elif place==54:
            T54()
        elif place==55:
            T55()
        elif place==56:
            T56()
        elif place==57:
            T57()
        elif place==58:
            T58()
        elif place==59:
            T59()
        elif place==60:
            T60()
        elif place==61:
            T61()
        elif place==62:
            T62()
        elif place==63:
            T63()
        elif place==64:
            T64()
        elif place==65:
            T65()
        elif place==66:
            T66()
        elif place==67:
            T67()
        elif place==68:
            T68()
        elif place==69:
            T69()
        elif place==70:
            T70()
        elif place==71:
            T71()
        elif place==72:
            T72()
        elif place==73:
            T73()
        elif place==74:
            T74()
        elif place==75:
            T75()
        elif place==76:
            T76()
        elif place==77:
            T77()
        elif place==78:
            T78()
        elif place==79:
            T79()
        elif place==80:
            T80()
        elif place==81:
            T81()
        elif place==82:
            T82()
        elif place==83:
            T83()
        elif place==84:
            T84()
        elif place==85:
            T85()
        elif place==86:
            T86()
        elif place==87:
            T87()
        elif place==88:
            T88()
        elif place==89:
            T89()
        elif place==90:
            T90()
        elif place==91:
            T91()
        elif place==92:
            T92()
        elif place==93:
            T93()
        elif place==94:
            T94()
        elif place==95:
            T95()
        elif place==96:
            T96()
        elif place==97:
            T97()
        elif place==98:
            T98()
        else:
            T99()
    
    print('Aight thats the end of the game. ')
    print('lets count your final stats now.')
    print()
    ts=0
    print(' you had ',money,' credits and as such that has been added to your total score.')
    ts=ts+money
    input('press ENTER to continue ...')
    print()
    print('You had ',happiness,' happiness points and as such are awarded 100 points for each of them.')
    ts=ts+(happiness*100)
    input('press ENTER to continue ...')
    print()
    print('You had ', knowledge,' knowledge points and as such are awarded 100 points for each of them.')
    ts=ts+(knowledge*100)
    input('press ENTER to continue ...')
    print()
    print('You had married ', spouse,' times and as such are awarded 200 points for each of them.')
    ts=ts+(spouse*200)
    input('press ENTER to continue ...')
    print()
    print(' You had ',child,' amount of children and are as such awarded 200 points for each of them. ')
    ts=ts+(child*200)
    input('press ENTER to continue ...')
    print()
    print('P.S. for each of your child/children we are deducting 100 points each as their study fund etc.')
    ts=ts-(child*100)
    input('press ENTER to continue ...')
    print()
    print('And finally, you had ',loans,' amount of loans and are as such deducted 50 points for each of them.')
    ts=ts-(loans*50)
    input('press ENTER to continue ...')
    print()
    print('That brings your final score to ',ts,' Points.')
    print()
    print(' THANKS FOR PLAYING ')
    print()
    print('now you can watch other users play this game and compare your results to the rest of them.')
elif r.upper()=='N':
    print('QUIT GAME ?')
    input('press ENTER to continue ...')
    print()
    print('PROGRAM OVER')
else:
    print('PROGRAM OVER')