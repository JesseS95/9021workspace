#Write by Jess.S 26/1/2019

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
from operator import itemgetter 

def draw_point(x,y):
    plt.scatter(x, y)
    plt.title('Point')#显示图表标题
    plt.xlabel('x')#x轴名称
    plt.ylabel('y')#y轴名称
    plt.grid(True)#显示网格线
    plt.show()

def draw_route(route_list,x,y):
    plt.scatter(x, y)
    for route in route_list:
        route= np.array(route)
#         print(route.shape)
        plt.plot(route[:,0],route[:,1])
    plt.title('Route')#显示图表标题
    plt.xlabel('x')#x轴名称
    plt.ylabel('y')#y轴名称
    plt.grid(True)#显示网格线
    plt.show()
    
def read_data(path,node):
    csv_data = pd.read_csv(path)  # 读取训练数据
    # print(csv_data)
    x = csv_data['Easting']
    y = csv_data['Southing']
    # print(x)
    # print(y)
    for i in range(len(x)):
        xy = []
        xy.append(x[i])
        xy.append(y[i])
        node.append(xy)
    # print(node)
    node_sort =sorted(node, key=lambda x: (x[0], x[1]))
#     print(node_sort)
#    另一种利用numpy的排序方法
#     node = np.array(node)
#     node = node[np.lexsort(node[:,::-1].T)]
#     print(node)
    return node_sort,x,y

def init_routing(route_number,route_list,leading_edge,node_sort):  
    for n in range(route_number):
        route = []
        route.append(node_sort[n])
        route_list.append(route)
        leading_edge.append(node_sort[n])
    return route_list 

#顺应点的趋势方向
def expand_real(route_list,leading_edge,node_sort,route_number):
    for i in range(len(node_sort)):
        if(i<route_number):
            continue
        y_min = 0.0
        max_index = 0
        for a in range(len(leading_edge)):
            if(leading_edge[a][1] > y_min):
                y_min = leading_edge[a][1]
                max_index = a
        index = -1
        for n in range(len(leading_edge)):
            delta_y = leading_edge[n][1] - node_sort[i][1]
            if((delta_y>=0) & (delta_y<y_min)):
                y_min = delta_y
                index = n
        if(index < 0):
            index = max_index 
        route_list[index].append(node_sort[i])
        origin = leading_edge[index]
        modify = []
        add = []
        cross = []
        for s in range(len(leading_edge)):
            sub = leading_edge[s] 
            if(sub[1]<origin[1]):
                continue
            if(origin[0]-sub[0]==0):
                leading_edge[s] = node_sort[i]
                route_list[s].append(node_sort[i])
                continue
            delta_fo = (origin[1]-sub[1])/(origin[0]-sub[0])
            delta_new = (node_sort[i][1]-origin[1])/(node_sort[i][0]-origin[0])
            if(delta_fo>0):
                cross.append(sub)
            if((delta_new<0)&(delta_fo<0)&(delta_new<delta_fo)):
                modify.append([s,leading_edge[s][0],leading_edge[s][1]])
                add.append(leading_edge[s])
                leading_edge[s] = origin
#                 route_list[s].append(origin)
        #根据modify中将每个s均稳健更新
#         print(modify)
        add.append(origin)
        if(len(modify)>0):
            cross = sorted(cross,key = lambda x: (x[1]),reverse = True)
            modify = sorted(modify,key=itemgetter(2),reverse = True)
            add = sorted(add,key = lambda x: (x[1]),reverse = True)
            for mo in modify:
                cross_if = False
                for cr in cross:
                    if(cr[1]<mo[2]):
                        leading_edge[mo[0]]=cr
                        route_list[mo[0]].append(cr)
                        cross_if = True
                        break
                if(cross_if):
                    continue
                for ad in add:
                    if(mo[2]<=ad[1]):
                        continue
                    route_list[mo[0]].append(ad)
                    mo[2] = ad[1]  
        leading_edge[index] = node_sort[i]
        
    return route_list 

if __name__=='__main__':
    path = 'coordinates v1.csv'
    node = []#所有点的坐标信息，下面进行排序
    route_list = []#存储现有的路径信息
    leading_edge = []#存储路径最前沿延续的路径index
    route_number = 3
    node_sort,x,y = read_data(path, node)
    route_list = init_routing(route_number, route_list, leading_edge,node_sort)
    route_list = expand_real(route_list, leading_edge, node_sort, route_number)
    route_list = np.array(route_list)
    draw_route(route_list,x,y)
