from timeit import default_timer as timer
import numbers

def input_validation(array_of_cities_values):
    for i in array_of_cities_values:
        if isinstance(i, numbers.Number) == False or i < 0:
            raise ValueError
        else:
            return array_of_cities_values

def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)

def city(dict_of_cities, sorted_array):
    cities = []
    for i in sorted_array:
        cities.append(list(dict_of_cities.keys())[list(dict_of_cities.values()).index(i)])
    return list(zip(cities, sorted_array))

def main():
    cities = {'Київ':30.54834, 
              'Ірпінь':29.99026, 
              'Бородянка':29.91848,
              'Васильків':30.34881, 
              'Біла Церква': 30.08658, 
              'Бровари':30.87664, 
              'Бориспіль':30.93379, 
              'Березань':31.41119, 
              'Драбов':32.17099, 
              'Черкаси':32.08022, 
              'Пирятин':32.50719, 
              'Лубни':33.00140, 
              'Семенівка':33.18967, 
              'Глобіно':33.27035, 
              'Миргород':33.62672, 
              'Решетіловка':33.95619, 
              'Полтава':34.56647, 
              'Нові Санжари':34.31256}
    array = input_validation(list(cities.values()))
    start_time = timer()
    quicksort(array)
    end_time = timer()
    print('\n'.join(str(x) for x in city(cities, array)))
    print('\nЧас на виконання програми:', (end_time - start_time)*1000, 'мс')
    
if __name__ == '__main__':
    main()