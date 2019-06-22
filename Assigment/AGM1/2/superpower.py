import sys
super_power = []
super_power3 = []
super_power4 = []
powers = input('Please input the heroes\' powers: ').split()
if not powers:
    print ( 'Sorry, these are not valid power values.' )
    sys.exit ( )
try:
    for i in powers:
        super_power.append(int(i))
        super_power3.append(int(i))
        super_power4.append ( int ( i ) )
except ValueError:
    print('Sorry, these are not valid power values.')
    sys.exit ( )
try:
    nb_of_switches  = int(input('Please input the number of power flips: '))
    if nb_of_switches > len(super_power):
        print('Sorry, this is not a valid number of power flips.')
        sys.exit()
except ValueError:
    print('Sorry, this is not a valid number of power flips.')
    sys.exit ( )
fushu_power = []
feifushu_power = []
fushu_power1 = []
feifushu_power1 = []
fushu_power2 = []
feifushu_power2 = []

for i in super_power:
    if i < 0:
        fushu_power.append(i)
        fushu_power1.append(i)
        fushu_power2.append ( i )
    else:
        feifushu_power.append(i)
        feifushu_power1.append ( i )
        feifushu_power2.append ( i )
fushu_power.sort()
feifushu_power.sort()
fushu_power1.sort()
feifushu_power1.sort()
fushu_power2.sort()
feifushu_power2.sort()

first_power = 0
second_power = 0
third_power = float('-inf')
forth_power = float('-inf')

if nb_of_switches == 0:
    for i in super_power:
        first_power += i
    second_power = third_power = forth_power = first_power
else:
    if not fushu_power:
        if nb_of_switches % 2 == 0:
            for i in feifushu_power1:
                first_power += i
        else:
            feifushu_power1[0] = - feifushu_power1[0]
            for i in feifushu_power1:
                first_power += i
    else:
        if nb_of_switches <= len(fushu_power):
            for i in range(0,nb_of_switches):
                fushu_power1[i] = - fushu_power1[i]
            for i in fushu_power1:
                first_power += i
            for i in feifushu_power1:
                first_power += i
        else:
            fake_flip = nb_of_switches - len(fushu_power)
            if fake_flip %2 == 0:
                for i in fushu_power1:
                    first_power += (-i)
                for i in feifushu_power1:
                    first_power += i
            else:
                feifushu_power1[ 0 ] = - feifushu_power1[ 0 ]
                for i in fushu_power1:
                    first_power += (-i)
                for i in feifushu_power1:
                    first_power += i

    if not fushu_power:
            for i in range ( 0 , nb_of_switches ):
                feifushu_power2[i] = - feifushu_power2[i]
            for i in feifushu_power2:
                second_power += i
    else:
        if nb_of_switches <= len ( fushu_power ):
            second_power = first_power
        else:
            for i in fushu_power2:
                second_power += (-i)
            for i in range(0,fake_flip):
                feifushu_power2[i] = - feifushu_power2[i]
            for i in feifushu_power2:
                second_power += i

    nb3 = int(nb_of_switches)
    third = 0
    while nb3 <= len(super_power):
        for i in range(nb3-nb_of_switches,nb3):
            super_power3[ i ] = - super_power3[ i ]
        for i in super_power3:
            third += i
        if third_power < third:
            third_power = int(third)
        for i in range ( nb3 - nb_of_switches , nb3 ):
            super_power3[ i ] = - super_power3[ i ]
        nb3 += 1
        third = 0

    forth = 0
    forth_sum = 0
    nb4 = 1
    while nb4 <= len ( super_power ):
        for j in range(0,len(super_power)-nb4+1):
            for i in range ( j , j+nb4 ):
                super_power4[ i ] = - super_power4[ i ]
            for i in super_power4:
                forth += i
            if forth_power < forth:
                forth_power = int ( forth )
            for i in range ( j , j+nb4 ):
                super_power4[ i ] = - super_power4[ i ]
            forth = 0
        nb4 += 1
    for i in super_power:
        forth_sum += i
    if forth_sum >= forth_power:
        forth_power = int(forth_sum)








print(f'Possibly flipping the power of the same hero many times, the greatest achievable power is {first_power}.')
print(f'Flipping the power of the same hero at most once, the greatest achievable power is {second_power}.')
print(f'Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {third_power}.')
print(f'Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is {forth_power}.')