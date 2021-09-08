my_set1 = {17, 76, 49, 57, 31, 5, 82, 91, 89, 33, 44, 48, 46, 54, 79, 53, 6, 80, 24}
my_set2 = {83, 95, 7, 99, 94, 31, 64, 74, 45, 49, 96, 90, 57, 67, 40, 13, 45, 21, 86}


my_union = my_set1 | my_set2
print(f"my_union: {my_union}")

my_intersection = my_set1 & my_set2
print(f"my_intersection: {my_intersection}")

my_difference = my_set1 - my_set2
my_difference_v2 = my_set2 - my_set1
print(f"my_difference: {my_difference}")
print(f"my_difference_v2: {my_difference_v2}")

my_symmetric_difference = my_set1 ^ my_set2
print(f"my_symmetric_difference: {my_symmetric_difference}")