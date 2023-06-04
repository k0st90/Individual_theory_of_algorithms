import numpy as np
import sys
from timeit import default_timer as timer

try:
    CSVData = open("graph.csv")
    res = np.genfromtxt(CSVData, delimiter=" ", dtype='int')
    for i in res:
        for j in i:
            if (int(j) < 0):
                raise ValueError
    n,m = res[0][0], res[0][1]
    ress = np.delete(res, 0, 0)
except ValueError:
    print("Wrong data")
    quit()

NO_PARENT = -1

def graph_quality(ress, n):
    mat =np.zeros((n,n), dtype ='int')
    for i in ress:
        mat[i[0]-1][i[1]-1] = i[2]
        mat[i[1]-1][i[0]-1] = i[2]
    return(mat)

def graph_length(ress, n):
    mat =np.zeros((n,n), dtype ='int')
    for i in ress:
        mat[i[0]-1][i[1]-1] = i[3]
        mat[i[1]-1][i[0]-1] = i[3]
    return(mat)

def dijkstra(adjacency_matrix, start_vertex):
    n_vertices = len(adjacency_matrix[0])
    shortest_distances = [sys.maxsize] * n_vertices
    added = [False] * n_vertices
    for vertex_index in range(n_vertices):
        shortest_distances[vertex_index] = sys.maxsize
        added[vertex_index] = False
    shortest_distances[start_vertex] = 0
    parents = [-1] * n_vertices
    parents[start_vertex] = NO_PARENT
    for _ in range(1, n_vertices):
        nearest_vertex = -1
        shortest_distance = sys.maxsize
        for vertex_index in range(n_vertices):
            if not added[vertex_index] and shortest_distances[vertex_index] < shortest_distance:
                nearest_vertex = vertex_index
                shortest_distance = shortest_distances[vertex_index]
        added[nearest_vertex] = True
        for vertex_index in range(n_vertices):
            edge_distance = adjacency_matrix[nearest_vertex][vertex_index]
             
            if edge_distance > 0 and shortest_distance + edge_distance < shortest_distances[vertex_index]:
                parents[vertex_index] = nearest_vertex
                shortest_distances[vertex_index] = shortest_distance + edge_distance
 
    return start_vertex, shortest_distances, parents

def print_solution(start_vertex, distances, parents):
    n_vertices = len(distances)
     
    for vertex_index in range(n_vertices):
        if vertex_index != start_vertex:
            print("\n", start_vertex+1, "->", vertex_index+1, "\t\t", distances[vertex_index], "\t\t", end="")
            print_path(vertex_index, parents)

def print_path(current_vertex, parents):
    if current_vertex == NO_PARENT:
        return
    print_path(parents[current_vertex], parents)
    print(current_vertex+1, end=" ")

adjacency_length_matrix = graph_length(ress, n)
adjacency_quality_matrix = graph_quality(ress, n)

def main():
    start_time = timer()
    result = dijkstra(adjacency_length_matrix, 0)
    end_time = timer()
    print_solution(*result)
    print('\nЧас на виконання програми (вага ребер - відстань):', (end_time - start_time)*1000, 'мс')
    start_time = timer()
    result = dijkstra(adjacency_quality_matrix, 0)
    end_time = timer()
    print_solution(*result)
    print('\nЧас на виконання програми (вага ребер - тип дороги):', (end_time - start_time)*1000, 'мс')
    
if __name__ == '__main__':
    main()
   