n, k = map(int, input().split())

people = [i for i in range(1, n+1)]

index = 0

print("<", end="")
while len(people) > 1:
    index = (index + k - 1) % len(people)
    print(people.pop(index), end=', ')
    
print(people[0], end="")
print(">")

    