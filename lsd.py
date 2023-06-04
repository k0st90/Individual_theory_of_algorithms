from timeit import default_timer as timer
import numbers

def input_validation(array_of_cities_values):
    for i in array_of_cities_values:
        if isinstance(i, numbers.Number) == False or i < 0:
            raise ValueError
        else:
            return array_of_cities_values
			
def radix_sort(source):
	RADIX = 10
	buckets = [[] for i in range(RADIX)]  
	maxLength = False
	tmp = -1; placement = 1
	while not maxLength:
		maxLength = True
		for i in source:
			tmp = i // placement
			buckets[tmp % RADIX].append(i)
			if maxLength and tmp > 0:
				maxLength = False
		a = 0
		for bucket in buckets:
			for i in bucket:
				source[a] = i
				a += 1
			bucket.clear()
		placement *= RADIX

def city(dict_of_cities, sorted_array):
    cities = []
    for i in sorted_array:
        cities.append(list(dict_of_cities.keys())[list(dict_of_cities.values()).index(i)])
    return list(zip(cities, sorted_array))

def main():
	cities = {'Київ':2967360, 
              'Ірпінь':60084, 
              'Бородянка':13215,
              'Васильків':40080, 
              'Біла Церква': 205247, 
              'Бровари':104318, 
              'Бориспіль':56950, 
              'Березань':13669, 
              'Драбов':6358, 
              'Черкаси':269836, 
              'Пирятин':15240, 
              'Лубни':45032, 
              'Семенівка':8052, 
              'Глобіно':9235, 
              'Миргород':38447, 
              'Решетіловка': 9199, 
              'Полтава':284942, 
              'Нові Санжари':7902}
	array = input_validation(list(cities.values()))
	start_time = timer()
	radix_sort(array)
	end_time = timer()
	print('\n'.join(str(x) for x in city(cities, list(reversed(array)))))
	print('\nЧас на виконання програми:', (end_time - start_time)*1000, 'мс')

if __name__ == "__main__":
	main()