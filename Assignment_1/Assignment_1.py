def do_it(a, b, fun):
    if fun == 'add':
        return a + b
    elif fun == 'sub':
        return a - b
    elif fun == 'mult':
        return a * b
    elif fun == 'div':
        if b != 0:
            return a / b
        else:
            return "Division by zero!"
    else:
        return "Not suitable function"


print(do_it(10, 5, 'add'))   
print(do_it(10, 5, 'sub'))   
print(do_it(10, 5, 'mult'))  
print(do_it(10, 5, 'div'))   
print(do_it(10, 5, 'mod'))   

print("--------------------------")


def add_some(num, step):
    if step <= 0:
        return 'step should be greater than zero.'
    if num <= 0:
        return 0
    return num + add_some(num - step, step)


print(add_some(4, 2))   
print(add_some(10, 3))  
print(add_some(10, 0))  
print(add_some(3, 1))   
print(add_some(-3, 1))  
print(add_some(10, -1)) 