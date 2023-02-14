#Very often we want to iterate over elements of a sequence
# or enumerate it

total = 0

seq = [ 8,4,3,2,1]

for i in seq:
    total += i

print(total)

# weighted sum

height = [5,4,7,2,3]
weightedsum = 0

for i in range(len(height)):
    weightedsum += i * height[i]

for i,h in enumerate(height):
    weightedsum += i * h

print(weightedsum)
