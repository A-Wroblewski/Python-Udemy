import itertools

cities = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states = ['BA', 'SP', 'MG', 'RJ']
cities_and_states = []
interval = min(len(cities), len(states))

for i in range(interval):
    cities_and_states.append((cities[i], states[i]))

print(cities_and_states)

print(list(zip(cities, states)), '\n')  # mesma coisa que o for (junta os elementos de cada lista)

a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']
c = [True, False]

print(list(zip(a, b, c)))  # sempre usa todos os valores da menor lista

print(list(itertools.zip_longest(a, b, c)))  # sempre usa todos os valores da maior lista
