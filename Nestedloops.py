# A nested loop is a loop inside a loop.
#The "inner loop" will be executed one time for each iteration of the "outer loop"
adj = ["red", "big", "tasty"]#adj=ajective
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
for x in [0, 1, 2]:#for loop cannot be empty, insome cases, forloop with no content put pass to avoid errors
    pass