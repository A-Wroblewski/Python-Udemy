
#########################################################################################

first_row_input = input("First row input: ").split()
second_row_input = input("Second row input: ").split()
third_row_input = input("Third row input: ").split()

input_matrix = first_row_input, second_row_input, third_row_input

print()

first_row_solution = input("First row solution: ").split()
second_row_solution = input("Second row solution: ").split()
third_row_solution = input("Third row solution: ").split()

solution_matrix = first_row_solution, second_row_solution, third_row_solution

print()

print("User input: ")
print(first_row_input)
print(second_row_input)
print(third_row_input)

print()

print("Expected solution: ")
print(first_row_solution)
print(second_row_solution)
print(third_row_solution)

print()

#########################################################################################

print(input_matrix)
print(solution_matrix)
print()

tries = 0

for line in input_matrix:
    for _ in line:

        temp_first_index = line[0]
        temp_second_index = line[1]
        temp_third_index = line[2]

        # print(temp_first_index, temp_second_index, temp_third_index, 'temp indice')

        if input_matrix == solution_matrix:

            tries += 1
            print(input_matrix, tries)
            break
        # print(line[0], line[1], line[2], 'linhas')
        # print()

        for _ in input_matrix:

            tries += 1

            line[0] = temp_third_index
            line[1] = temp_first_index
            line[2] = temp_second_index

            input_matrix[1]

            if input_matrix == solution_matrix:
                tries += 1
                print(input_matrix, tries)
                break
                
            print(input_matrix, tries)

        # print(line[0], line[1], line[2], 'ultimo print')



for i in range(input_matrix):
    print(i)
    for j in range(1, i):
        print(j, i)
