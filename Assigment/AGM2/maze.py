#written by ZH Sheng
#z5159288
import sys
import os

class MazeError(Exception):
    pass
class Maze:
    def __init__(self,input_maze = ''):
        ###########################################################################
        ##读文件
        self.input_maze = input_maze
        origin_data = []
        maze_data = []
        data = []
        row_data = []
        niubi_data = []
        temp_maze_data = []
        with open(input_maze) as opened_maze:
            for row in opened_maze:
                origin_data.append(row)
        for line in origin_data:
            maze_data.append ( line.strip ( '\n' ).split ( ' ' ) )

        for i in maze_data:
            for j in i:
                if j.isdigit():
                    data.append(j)
            row_data.append(list(data))
            data.clear()

        for i in row_data:
            if i :
                niubi_data.append(i)
        for i in niubi_data:
            if len(i) == 1:
                i = list(str(i[0]))
                i = [int(j) for j in i]
                temp_maze_data.append(i)
                niubi_data=temp_maze_data

        newbee_data = []
        for i in niubi_data:
            new_line = [ ]
            for j in i:
                new_line.append(int(j))
            newbee_data.append(new_line)

        if 2 <= len ( newbee_data ) <= 41:
            pass
        else:
            raise MazeError('Incorrect input.')
        for i in newbee_data:
            if 2 <= len ( i ) <= 31:
                pass
            else:
                raise MazeError('Incorrect input.')
        for i in newbee_data:
            for j in i :
                if 0 <= j <= 3:
                    pass
                else:
                    raise MazeError('Incorrect input.')

        chang = len(newbee_data[0])
        for i in newbee_data:
            if len(i) == chang:
                pass
            else:
                raise MazeError('Incorrect input.')
        for i in newbee_data:
            if i[-1] == 1 :
                raise MazeError('Input does not represent a maze.')
            if i[-1] == 3 :
                raise MazeError('Input does not represent a maze.')
        for i in newbee_data[-1]:

            if i == 2:
                raise MazeError('Input does not represent a maze.')
            if i == 3:
                raise MazeError('Input does not represent a maze.')

        ##构建迷宫
        def kuangzi(laoda,laoer,laosan):
            sunzi = [0,0,0,0]
            if laoda == 1:
                sunzi[1] = 1
            if laoda == 3:
                sunzi[1] = 1
            if laoer == 2:
                sunzi[2] = 1
            if laoer == 3:
                sunzi[2] = 1
            if laosan == 1:
                sunzi[3] = 1
            if laosan == 3:
                sunzi[3] = 1
            if laoda == 2:
                sunzi[0] = 1
            if laoda == 3:
                sunzi[0] = 1
            return sunzi

        sunzimen = []
        tuzi = []
        for i in range(len(newbee_data)-1):
            for j in range(len(newbee_data[i])- 1):
                sunzimen.append(kuangzi(newbee_data[i][j],newbee_data[i][j+1],newbee_data[i+1][j]))

        for i in range(len(newbee_data)-1):
            tuzi.append(sunzimen[i*(len(newbee_data[0])-1):i*(len(newbee_data[0])-1)+len(newbee_data[0])-1])
        ###########################################################################
        #分析迷宫
        ###########################################################################
        #gate
        gate = []
        if len(tuzi) == 1:
            if len(tuzi[0]) == 1:
                for i in tuzi[0][0]:
                    if i == 0:
                        gate.append((0,0))

            else:
                for i in tuzi[ 0 ][ 0 ]:
                    if i == 0:
                        gate.append ( (0 , 0) )
                if tuzi[0][0][2] == 0:
                    gate.remove((0,0))

                for i in tuzi[ 0 ][ -1 ]:
                    if i == 0:
                        gate.append ( (0 , len(tuzi[0])-1))
                if tuzi[0][-1][0] == 0:
                    gate.remove((0,len(tuzi[0])-1))

                for i in range(1,len(tuzi[0])-1):
                    for j in tuzi[0][i]:
                        if j[1] == 0:
                            gate.append((0,i))
                        if j[3] == 0:
                            gate.append((0,i))
        else:
            if len(tuzi[0]) == 1:
                for i in tuzi[ 0 ][ 0 ]:
                    if i == 0:
                        gate.append ( (0 , 0) )
                if tuzi[ 0 ][ 0 ][ 3 ] == 0:
                    gate.remove ( (0 , 0) )

                for i in tuzi[ -1 ][ 0 ]:
                    if i == 0:
                        gate.append ( (len(tuzi)-1 , 0) )
                if tuzi[ -1 ][ 0 ][ 1 ] == 0:
                    gate.remove ( (len ( tuzi) - 1,0) )

                for i in range(1,len(tuzi)-1):
                    for j in tuzi[i][0]:
                        if j[0] == 0:
                            gate.append((i,0))
                        if j[2] == 0:
                            gate.append((i,0))

            else:
                if tuzi[0][0][0] == 0:
                    gate.append((0,0))
                if tuzi[0][0][1] == 0:
                    gate.append((0,0))

                if tuzi[0][-1][1] == 0:
                    gate.append((0,len(tuzi[0])-1))
                if tuzi[0][-1][2] == 0:
                    gate.append((0,len(tuzi[0])-1))

                if tuzi[-1][0][0] == 0:
                    gate.append((len ( tuzi) - 1,0))
                if tuzi[ -1 ][ 0 ][3] == 0:
                    gate.append((len ( tuzi) - 1,0))

                if tuzi[-1][-1][2] == 0:
                    gate.append((len ( tuzi) - 1,len(tuzi[0])-1))
                if tuzi[-1][-1][3] == 0:
                    gate.append((len ( tuzi) - 1,len(tuzi[0])-1))

                for i in range(1,len(tuzi[0])-1):
                    if tuzi[0][i][1] == 0:
                        gate.append((0,i))
                    if tuzi[-1][i][3] == 0:
                        gate.append((len ( tuzi) - 1,i))
                for i in range(1,len(tuzi)-1):
                    if tuzi[i][0][0] == 0:
                        gate.append((i,0))
                    if tuzi[i][-1][2] == 0:
                        gate.append((i,len(tuzi[0])-1))
        gate_count = len(gate)
        #print(f'gate = {gate_count}')
        ###########################################################################
        # wall
        wall = []
        pangzi = []
        for i in range(0,len(newbee_data)):
            pangzi_row = [ ]
            for j in range(0,len(newbee_data[0])):
                pangzi_row.append([0,0,0,0])
            pangzi.append ( pangzi_row )

        for i in range ( len ( newbee_data ) ):
            for j in range ( len ( newbee_data[ 0 ] ) ):
                if newbee_data[i][j] ==1:
                    pangzi[i][j][2] =1
                elif newbee_data[i][j] ==2:
                    pangzi[i][j][3] =1
                elif newbee_data[i][j] ==3:
                    pangzi[i][j][2] =1
                    pangzi[i][j][3] =1
        for i in range ( 0,len ( newbee_data ) ):
            for j in range ( 0,len ( newbee_data[ 0 ] ) ):
                if pangzi[i-1][j][3] == 1:
                    pangzi[i][j][1] = 1
                if pangzi[i][j-1][2] ==1:
                    pangzi[i][j][0] =1

        reach_wall=[]
        def link(a,b):
            if (a,b) not in reach_wall:
                reach_wall.append ( (a , b) )
                if pangzi[a][b][0] == 1:
                    link_wall.append((a,b))
                    link(a,b-1)
                if pangzi[a][b][1] == 1:
                    link_wall.append ( (a , b) )
                    link(a-1,b)
                if pangzi[a][b][2] == 1:
                    link_wall.append ( (a , b) )
                    link(a,b+1)
                if pangzi[a][b][3] == 1:
                    link_wall.append ( (a , b) )
                    link(a+1,b)
        for i in range(len(pangzi)):
            for j in  range(len(pangzi[0])):
                if (i,j) not in reach_wall and pangzi[i][j].count(1)!=0:
                    link_wall = []
                    link(i,j)
                    wall.append(link_wall)
                    link_wall = []
        wall_number = len(wall)
        #print(f'connected walls ={wall_number}')
        ###########################################################################
        #accessible areas
        area = []
        reach_area = [ ]
        def biubiubiu (a , b):
            if 0 <= a < len(tuzi) and 0 <= b < len(tuzi[0]):
                if (a , b) not in reach_area:
                    reach_area.append ( (a , b) )
                    if tuzi[ a ][ b ][ 0 ] == 0:
                        link_area.append ( (a , b) )
                        biubiubiu ( a , b - 1 )
                    if tuzi[ a ][ b ][ 1 ] == 0:
                        link_area.append ( (a , b) )
                        biubiubiu ( a - 1 , b )
                    if tuzi[ a ][ b ][ 2 ] == 0:
                        link_area.append ( (a , b) )
                        biubiubiu ( a , b + 1 )
                    if tuzi[ a ][ b ][ 3 ] == 0:
                        link_area.append ( (a , b) )
                        biubiubiu ( a + 1 , b )
        for i in range ( len ( tuzi ) ):
            for j in range ( len ( tuzi[ 0 ] ) ):
                if (i , j) not in reach_area and (i,j) in gate:
                    link_area = [ ]
                    biubiubiu ( i , j )
                    area.append ( link_area )
                    link_area = [ ]
        area_number = len ( area )
        #print ( f'connected areas ={area_number}' )
        ###########################################################################
        #inaccessible inner point
        inaccessible_inner_point = []
        for i in range ( len ( tuzi ) ):
            for j in range ( len ( tuzi[ 0 ] ) ):
                if (i,j) not in reach_area:
                    inaccessible_inner_point.append((i,j))
        inner_point_number  = len(inaccessible_inner_point)
        #print ( f'inner point ={inner_point_number}' )
        ###########################################################################
        #死胡同
        sihutong = []
        for i in range(len(tuzi)):
            for j in range(len(tuzi[0])):
                if tuzi[i][j].count(1) == 3:
                    if (i,j) in reach_area:
                        sihutong.append((i,j))
        qiangshu = []
        for i in range(len(tuzi)):
            qiangshu_row = [ ]
            for j in range(len(tuzi[0])):
                qiangshu_row.append(tuzi[i][j].count(1))
            qiangshu.append(qiangshu_row)
        def jiaqiang(i,j):
            if 0 <= i < len(qiangshu) and 0 <= j < len(qiangshu[0]):
                if qiangshu[i][j] == 3:
                    qiangshu[ i ][ j ] = 10
                    if tuzi[i][j][0] == 0 and 0 <= i < len(qiangshu) and 0 <= j-1 < len(qiangshu[0]):
                        qiangshu[i][j-1] += 1
                        jiaqiang (i,j-1 )
                    if tuzi[i][j][1] == 0 and 0 <= i-1 < len(qiangshu) and 0 <= j < len(qiangshu[0]):
                        qiangshu[i-1][j] += 1
                        jiaqiang (i-1,j)
                    if tuzi[i][j][2] == 0 and 0 <= i < len(qiangshu) and 0 <= j+1 < len(qiangshu[0]):
                        qiangshu[i][j+1] += 1
                        jiaqiang (i,j+1 )
                    if tuzi[i][j][3] == 0 and 0 <= i+1 < len(qiangshu) and 0 <= j < len(qiangshu[0]):
                        qiangshu[i+1][j] += 1
                        jiaqiang (i+1,j )
        for _ in sihutong:
            jiaqiang(_[0],_[1])
        xx = []
        for i in range(len(qiangshu)):
            for j in range(len(qiangshu[0])):
                if qiangshu[i][j] > 4:
                    xx.append((i,j))
        xx_area = [ ]
        reach_xx_area = [ ]
        def biubiubiuxx (a , b):
            if 0 <= a < len ( tuzi ) and 0 <= b < len ( tuzi[ 0 ] ):
                if (a , b) not in reach_xx_area and (a,b) in xx:
                    reach_xx_area.append ( (a , b) )
                    if tuzi[ a ][ b ][ 0 ] == 0:
                        link_xx_area.append ( (a , b) )
                        biubiubiuxx ( a , b - 1 )
                    if tuzi[ a ][ b ][ 1 ] == 0:
                        link_xx_area.append ( (a , b) )
                        biubiubiuxx ( a - 1 , b )
                    if tuzi[ a ][ b ][ 2 ] == 0:
                        link_xx_area.append ( (a , b) )
                        biubiubiuxx ( a , b + 1 )
                    if tuzi[ a ][ b ][ 3 ] == 0:
                        link_xx_area.append ( (a , b) )
                        biubiubiuxx ( a + 1 , b )
        for i in range ( len ( tuzi ) ):
            for j in range ( len ( tuzi[ 0 ] ) ):
                if (i , j) not in reach_xx_area and (i , j) in sihutong:
                    link_xx_area = [ ]
                    biubiubiuxx ( i , j )
                    xx_area.append ( link_xx_area )
                    link_xx_area = [ ]
        xx_area_number = len ( xx_area )
        #print(qiangshu)
        #print(xx)
        #print ( f'xx areas ={xx_area}' )
        ###########################################################################
        #一条路走到通

        oo_area = [ ]
        reach_oo_area = [ ]

        def biubiubiuoo (a , b):
            if 0 <= a < len ( tuzi ) and 0 <= b < len ( tuzi[ 0 ] ):
                if (a , b) not in reach_oo_area and (a , b) not in xx:
                    reach_oo_area.append ( (a , b) )
                    if tuzi[ a ][ b ][ 0 ] == 0:
                        link_oo_area.append ( (a , b) )
                        biubiubiuoo ( a , b - 1 )
                    if tuzi[ a ][ b ][ 1 ] == 0:
                        link_oo_area.append ( (a , b) )
                        biubiubiuoo ( a - 1 , b )
                    if tuzi[ a ][ b ][ 2 ] == 0:
                        link_oo_area.append ( (a , b) )
                        biubiubiuoo ( a , b + 1 )
                    if tuzi[ a ][ b ][ 3 ] == 0:
                        link_oo_area.append ( (a , b) )
                        biubiubiuoo ( a + 1 , b )

        for i in range ( len ( tuzi ) ):
            for j in range ( len ( tuzi[ 0 ] ) ):
                if (i , j) not in reach_oo_area and (i , j) in gate:
                    link_oo_area = [ ]
                    biubiubiuoo ( i , j )
                    oo_area.append ( link_oo_area )
                    link_oo_area = [ ]

        path = []
        for i in oo_area:
            if i:
                t = list(set(i))
                path.append(t)


        for i in path:
            baba = 0
            for j in i:
                if j in gate:
                    baba += 1
            if baba > 2 :
                path.remove(i)
        path_number = len ( path )
        #print ( f'path number ={path_number}' )
        ###########################################################################
        self.gate_number = gate_count
        self.wall_number = wall_number
        self.inner_point_number=inner_point_number
        self.area_number = area_number
        self.xx_area_number = xx_area_number
        self.path_number = path_number
        ###########################################################################
        # 画图部分
        ###########################################################################
        # 筑墙
        paopao = [ ]
        for i in range ( len ( pangzi ) ):
            for j in range ( len ( pangzi[ 0 ] ) ):
                while pangzi[ i ][ j ][ 2 ] == 1 and (i,j) not in paopao:
                    paopao.append ( (i,j) )
                    j += 1
        #print(paopao)
        paopaowang = []
        for i in range(len(paopao)):
            paopao_row = []
            paopao_row.append( (paopao[ i ][ 1 ] , paopao[ i ][ 0 ]) )
            paopao_row.append(  (paopao[ i ][ 1 ] + 1 , paopao[ i ][ 0 ])  )
            paopaowang.append(paopao_row)
        if paopaowang[0][1] == paopaowang[1][0]:
            paopaowang[1][0] = paopaowang [0][0]
            paopaowang.remove(paopaowang[0])
        i = 1
        while i < len(paopaowang):
            if paopaowang[i-1][1] == paopaowang[i][0]:
                paopaowang[i][0] = paopaowang[i-1][0]
                paopaowang.remove(paopaowang[i-1])
            else:
                i += 1
        #print ( paopaowang )
        maomao = [ ]
        for j in range ( len ( pangzi[ 0 ] ) ):
            for i in range ( len ( pangzi ) ):
                while pangzi[ i ][ j ][ 3 ] == 1 and (i,j) not in maomao:
                    maomao.append ( (i,j) )
                    i += 1
        maomaowang = [ ]
        for i in range ( len ( maomao ) ):
            maomao_row = [ ]
            maomao_row.append ( (maomao[ i ][ 1 ] , maomao[ i ][ 0 ]) )
            maomao_row.append ( (maomao[ i ][ 1 ]  , maomao[ i ][ 0 ] + 1) )
            maomaowang.append ( maomao_row )
        #print ( maomaowang )
        if maomaowang[ 0 ][ 1 ] == maomaowang[ 1 ][ 0 ]:
            maomaowang[ 1 ][ 0 ] = maomaowang[ 0 ][ 0 ]
            maomaowang.remove ( maomaowang[ 0 ] )
        i = 1
        while i < len ( maomaowang ):
            if maomaowang[ i - 1 ][ 1 ] == maomaowang[ i ][ 0 ]:
                maomaowang[ i ][ 0 ] = maomaowang[ i - 1 ][ 0 ]
                maomaowang.remove ( maomaowang[ i - 1 ] )
            else:
                i += 1
        #print ( maomaowang )
        ###########################################################################
       #pillar
        pillar = []
        for i in range(len(pangzi)):
            for j in range(len(pangzi[0])):
                if pangzi[i][j] == [0,0,0,0]:
                    pillar.append((j,i))
        #print(pillar)
        ###########################################################################
        #ooxx
        ooxx = []
        for i in xx:
            ooxx.append((i[1]+0.5,i[0]+0.5))
        #print(ooxx)
        ###########################################################################
        #path
        sixteen = []
        for i in range(len(path)):
            sixteen_row = []
            for j in range(len(path[i])):
                sixteen_row.append((path[i][j][1],path[i][j][0]))
            sixteen.append(sixteen_row)
        #print(f'sixteen = {sixteen}')
        path_point = []
        for i in sixteen:
            for j in i:
                path_point.append(j)
        path_point = sorted(path_point)
        #print(f'path_point = {path_point}')
        xx_point = []
        for i in xx:
            xx_point.append((i[1],i[0]))
        #print(f'xx_point = {xx_point}')
        #print(f'tuzi = {tuzi}')
        hang_line = []
        lie_line = []
        for i in path_point:
            if tuzi[i[1]][i[0]][0] == 0 and (i[0]-1,i[1]) not in xx_point:
                hang_line.append([(i[0]-0.5,i[1]+0.5),(i[0]+0.5,i[1]+0.5)])
            if tuzi[i[1]][i[0]][2] == 0 and (i[0]+1,i[1]) not in xx_point:
                hang_line.append([(i[0]+0.5,i[1]+0.5),(i[0]+1.5,i[1]+0.5)])
            if tuzi[i[1]][i[0]][1] == 0 and (i[0],i[1]-1) not in xx_point:
                lie_line.append([(i[0]+0.5,i[1]-0.5),(i[0]+0.5,i[1]+0.5)])
            if tuzi[i[1]][i[0]][3] == 0 and (i[0],i[1]+1) not in xx_point:
                lie_line.append([(i[0]+0.5,i[1]+0.5),(i[0]+0.5,i[1]+1.5)])
        hang = []
        lie = []
        for i in hang_line:
            if not i in hang:
                hang.append(i)
        for i in lie_line:
            if not i in lie:
                lie.append(i)
        #print(f'hang={hang}')
        #print(f'lie={lie}')
        hang = sorted(hang,key=lambda x:(x[0][1],x[0][0]))
        lie = sorted ( lie , key=lambda x: (x[ 0 ][ 0 ] , x[ 0 ][ 1 ]) )

        if hang[ 0 ][ 1 ] == hang[ 1 ][ 0 ]:
            hang[ 1 ][ 0 ] = hang[ 0 ][ 0 ]
            hang.remove ( hang[ 0 ] )
        i = 1
        while i < len ( hang ):
            if hang[ i - 1 ][ 1 ] == hang[ i ][ 0 ]:
                hang[ i ][ 0 ] = hang[ i - 1 ][ 0 ]
                hang.remove ( hang[ i - 1 ] )
            else:
                i += 1
        #print ( f'h = {hang}' )
        if lie[ 0 ][ 1 ] == lie[ 1 ][ 0 ]:
            lie[ 1 ][ 0 ] = lie[ 0 ][ 0 ]
            lie.remove ( lie[ 0 ] )
        i = 1
        while i < len ( lie ):
            if lie[ i - 1 ][ 1 ] == lie[ i ][ 0 ]:
                lie[ i ][ 0 ] = lie[ i - 1 ][ 0 ]
                lie.remove ( lie[ i - 1 ] )
            else:
                i += 1
        #print(f'l = {lie}')
        ############################################################################
        self.pao = paopaowang
        self.mao = maomaowang
        self.pillar = pillar
        self.ooxx = ooxx
        self.h = hang
        self.l = lie
        ###########################################################################
        #分析输出部分
    def analyse(self):

        if self.gate_number == 0:
            print('The maze has no gate.')
        elif self.gate_number ==1:
            print('The maze has a single gate.')
        else:
            print(f'The maze has {self.gate_number} gates.')

        if self.wall_number == 0:
            print('The maze has no wall.')
        elif self.wall_number ==1:
            print('The maze has walls that are all connected.')
        else:
            print(f'The maze has {self.wall_number} sets of walls that are all connected.')

        if self.inner_point_number == 0:
            print('The maze has no inaccessible inner point.')
        elif self.inner_point_number ==1:
            print('The maze has a unique inaccessible inner point.')
        else:
            print(f'The maze has {self.inner_point_number} inaccessible inner points.')

        if self.area_number == 0:
            print('The maze has no accessible area.')
        elif self.area_number ==1:
            print('The maze has a unique accessible area.')
        else:
            print(f'The maze has {self.area_number} accessible areas.')

        if self.xx_area_number == 0:
            print('The maze has no accessible cul-de-sac.')
        elif self.xx_area_number ==1:
            print('The maze has accessible cul-de-sacs that are all connected.')
        else:
            print(f'The maze has {self.xx_area_number} sets of accessible cul-de-sacs that are all connected.')

        if self.path_number == 0:
            print('The maze has no entry-exit path with no intersection not to cul-de-sacs.')
        elif self.path_number ==1:
            print('The maze has a unique entry-exit path with no intersection not to cul-de-sacs.')
        else:
            print(f'The maze has {self.path_number} entry-exit paths with no intersections not to cul-de-sacs.')
    ###########################################################################
    #显示输出部分
    def display(self):
        tou = self.input_maze.split('.')[0]
        tou += '.tex'
        #print(tou)
        with open (tou,'w') as huahua:
            huahua.write('\\documentclass[10pt]{article}\n'\
                                    '\\usepackage{tikz}\n'\
                                    '\\usetikzlibrary{shapes.misc}\n'\
                                    '\\usepackage[margin=0cm]{geometry}\n'\
                                    '\\pagestyle{empty}\n'\
                                    '\\tikzstyle{every node}=[cross out, draw, red]\n\n'\
                                    '\\begin{document}\n\n'\
                                    '\\vspace*{\\fill}\n'\
                                    '\\begin{center}\n'\
                                    '\\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]\n'\
                                    '% Walls\n')
            for i in self.pao:
                huahua.write ( '    \\draw ' + '(' + str (i[0][0])+','+ str(i[0][1]) + ')' + ' -- ' + '(' + str (i[1][0])+','+ str(i[1][1]) + ')' + ';\n')
            for i in self.mao:
                huahua.write ( '    \\draw ' + '(' + str (i[0][0])+','+ str(i[0][1]) + ')' + ' -- ' + '(' + str (i[1][0])+','+ str(i[1][1]) + ')' + ';\n')

            huahua.write('% Pillars\n')
            for i in self.pillar:
                huahua.write('    \\fill[green] ' +'(' + str (i[0])+','+ str(i[1]) + ')'+ ' circle(0.2);\n' )

            huahua.write ( '% Inner points in accessible cul-de-sacs\n' )
            for i in self.ooxx:
                huahua.write('    \\node at ' +'(' + str (i[0])+','+ str(i[1]) + ')'+' {};\n')

            huahua.write ( '% Entry-exit paths without intersections\n' )
            for i in self.h:
                huahua.write (
                    '    \\draw[dashed, yellow] ' + '(' + str ( i[ 0 ][ 0 ] ) + ',' + str ( i[ 0 ][ 1 ] ) + ')' + ' -- ' + '(' + str (
                        i[ 1 ][ 0 ] ) + ',' + str ( i[ 1 ][ 1 ] ) + ')' + ';\n' )
            for i in self.l:
                huahua.write (
                    '    \\draw[dashed, yellow] ' + '(' + str ( i[ 0 ][ 0 ] ) + ',' + str ( i[ 0 ][ 1 ] ) + ')' + ' -- ' + '(' + str (
                        i[ 1 ][ 0 ] ) + ',' + str ( i[ 1 ][ 1 ] ) + ')' + ';\n' )

            huahua.write ( '\\end{tikzpicture}\n'\
                                    '\\end{center}\n'\
                                    '\\vspace*{\\fill}\n\n'\
                                    '\\end{document}\n')