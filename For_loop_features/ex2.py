from timeit import timeit
#能用builtin函数写，不要用python代码去实现，builtin是通过c去写好封装起来的，相比python会少很多字节码上overload的损耗
lst =[i for i in range(100)]

def with_for():
    max_num=0
    for num in lst:
        if num>max_num:
            max_num=num
    return max_num

def without_for():
    return max(lst)

print(f"with: {timeit(with_for,number=10000)}")
print(f"without: {timeit(without_for,number=10000)}")

'''
result:
with: 0.016311799990944564
without: 0.012182100035715848
'''