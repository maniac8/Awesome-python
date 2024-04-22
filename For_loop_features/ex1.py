from timeit import timeit
'''
todo: 
    2 different way to show whether we choose for or directly using python features to achieve for performance 
    evaluate the methods by their running time 
    
    The reason is  when you using the lst.append, python cant know whether you use the list append method ,it need to find 
    but you use [i for i in range(n)] ,python will directly to using the list.append methods.
'''
def with_for():
    lst =[]
    for i in range(100):
        lst.append(i)
    return lst

def without_for1():
    return [i for i in range(100)]  #directly 

def without_for2():
    return (i for i in range(100))  #using generator method 

print(f"with: {timeit(with_for,number=10000)}")
print(f"without1: {timeit(without_for1,number=10000)}")
print(f"without2: {timeit(without_for2,number=10000)}")

'''
result 
with: 0.022044200042728335
without1: 0.012421199993696064
without2: 0.0027667999966070056
'''
