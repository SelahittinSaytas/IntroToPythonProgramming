import statistics

example_list = [1,2,3,4,5,6,7,8,9,10,11]

x = statistics.mean(example_list)
y = statistics.median(example_list)
z = statistics.variance(example_list)
q = statistics.stdev(example_list)
p = statistics.mode(example_list)

print(x)
print(y)
print(z)
print(q)
print(p)
