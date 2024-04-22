from timeit import timeit
'''
any && all using 
'''
lst=[i for i in range(100)]
#any 
# def with_for():
#     for num in lst:
#         if num >50:
#             return True
#     return False

# def without_for():
#     return any(num>50 for num in lst)  #using a generator to get ,it will spent lots of time
#all 
def with_for():
    for num in lst:
        if num >100:
            return False
    return True

def without_for():
    return all(num<100 for num in lst)  #using a generator to get ,it will spent lots of time

print(f"with: {timeit(with_for,number=10000)}")
print(f"without: {timeit(without_for,number=10000)}")

'''
result1:
with: 0.007183100038673729
without: 0.019139799987897277
result2:
with: 0.019261700042989105
without: 0.04243430000497028
'''