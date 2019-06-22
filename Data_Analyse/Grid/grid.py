#Write by Jess.S 25/1/2019

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

def draw_point(x,y):
    plt.scatter(x, y)
    plt.title('点分布图')#显示图表标题
    plt.xlabel('x轴')#x轴名称
    plt.ylabel('y轴')#y轴名称
    plt.grid(True)#显示网格线
    plt.show()

def draw_route(route_list,x,y):
    plt.scatter(x, y)
    for route in route_list:
        route= np.array(route)
#         print(route.shape)
        plt.plot(route[:,0],route[:,1])
    plt.title('路径图')#显示图表标题
    plt.xlabel('x轴')#x轴名称
    plt.ylabel('y轴')#y轴名称
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
    # print(node_sort)
    #另一种利用numpy的排序方法
   
    # node = np.array(node)
    # node = node[np.lexsort(node[:,::-1].T)]
    # print(node)
    return node_sort,x,y
#判断前沿面的点是否被更新
# def dominant(prev,current):
#     if prev[0]<current[0] & prev[1]<current[1]:
#         return True
#     return False
# 
# #判断两条路径是否有重叠部分
# def judge_line(origin,n1,n2):
#     if((n1[1]-origin[1])/(n1[0]-origin[0])==(n2[1]-origin[1])/(n2[0]-origin[0])):
#         return True
#     return False

def init_routing(route_number,route_list,leading_edge,node_sort):       
    for n in node_sort:
        if(n == node_sort[0]):
            continue
        route = []
        route.append(node_sort[0])
        route.append(n)
        route_list.append(route)
        leading_edge.append(n)
        if(len(route_list)>=route_number):
            return route_list
    return
    
def expand(route_list,leading_edge,node_sort,route_number):
    for i in range(len(node_sort)):
        if(i<=route_number):
            continue
        y_min = 0
        max_index = 0
        for a in range(len(leading_edge)):
            if(leading_edge[a][1]>y_min):
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
        leading_edge[index] = node_sort[i]
    return route_list    

if __name__=='__main__':
    path = 'coordinates v1.csv'
    node = []#所有点的坐标信息，下面进行排序
    route_list = []#存储现有的路径信息
    leading_edge = []#存储路径最前沿延续的路径index
    route_number = 6
    node_sort,x,y = read_data(path, node)
    route_list = init_routing(route_number, route_list, leading_edge,node_sort)
    route_list = expand(route_list, leading_edge, node_sort, route_number)
    route_list = np.array(route_list)
    draw_route(route_list,x,y)
    print(route_list)
