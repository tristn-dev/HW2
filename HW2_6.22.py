'''
Tristan Deveyra
2057603
'''


a = int(input())
b = int(input())
c = int(input())

d = int(input())
e = int(input())
f = int(input())

solution_found = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if (a * x) + (b * y) != c:
            continue
        if (d * x) + (e * y) == f:
            print(x, y)
            solution_found = True
            break  # Break out of the inner loop if a solution is found
if not solution_found:
    print("No solution")

      
    
      
