set_of_result = set ( )
for i in range ( 10 , 99 ):
    if str ( i )[ 0 ] == str ( i )[ 1 ]:
        continue
    for j in range ( 10 , 99 ):
        if (str ( j )[ 0 ] in str ( i )) or (str ( j )[ 1 ] in str ( i )) or (str ( j )[ 0 ] == str ( j )[ 1 ]):
            continue
        for k in range ( 10 , 99 ):
            if str ( k )[ 0 ] == str ( k )[ 1 ]:
                continue
            product = i * j * k
            total_str = str ( i ) + str ( j ) + str ( k )
            if len ( set ( total_str ) ) != 6:
                continue

            else:
                if set ( str ( product ) ) == set ( total_str ):
                    if product in set_of_result:
                        continue
                    else:
                        set_of_result.add ( product )
                        print ('{} x {} x {} = {} is a solution.'.format( i , j , k , product ))