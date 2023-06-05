import numpy as np
from timeit import default_timer as timer

try:
    CSVData = open("graph.csv")
    res = np.genfromtxt(CSVData, delimiter=" ", dtype='int')
    res = np.delete(res, (2,3), axis=1)
    for i in res:
        for j in i:
            if (int(j) < 0):
                raise ValueError
    n,m = res[0]
    ress = np.delete(res, 0 ,0)
except ValueError:
    print("Wrong data")
    quit()

def sumj(re):
    mat =np.zeros((n,n), dtype ='int')
    for i in re:
        mat[i[0]-1][i[1]-1] = 1
        mat[i[1]-1][i[0]-1] = 1
    return mat

def ssum(mat):
    dic = {}
    for i in range(0,n):
        for j in range(0,n):
            if i+1 not in dic.keys():
                dic[i+1]=[]
                if mat[i][j]==1:
                     dic[i+1].append(j+1)
            else:
                if mat[i][j]==1:
                     dic[i+1].append(j+1)
    return dic


def dfs(graph, start, end, visited=list()):
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited and end not in visited:
            dfs(graph, neighbor, end, visited)
    return visited

matsum = sumj(ress)

def main():
    try:
        start =  int(input("Введіть вершину з якої починати пошук: "))
        end = int(input("Введіть вершину, в яку треба прийти: "))
        assert 1<= start and end <= 18
    except Exception:
        print("Wrong data")
        quit()
    start_time = timer()
    dfs_search = dfs(ssum(matsum), start, end)
    end_time = timer()
    print('DFS обхід графу:', *dfs_search)
    print('Час на виконання програми:', (end_time - start_time)*1000, 'мс')

if __name__ == '__main__':
    main()

