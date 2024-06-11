def product_or_sum(x, y):
    product = x * y
    if product < 1000:
        print(product)
    else:
        print(x + y)

product_or_sum(10, 12) 
product_or_sum(50, 60) 

print("--------------------------")


def is_divisible_by_7(num):
    if num % 7 == 0:
        return True
    else:
        return False

print(is_divisible_by_7(14)) 
print(is_divisible_by_7(15)) 
print("--------------------------")




def is_odd(num):
    if num % 2 != 0:
        print(True)
        return True
    else:
        print(False)
        return False

is_odd(4) 
is_odd(7) 
print("--------------------------")





def display_grade(marks):
    if marks > 90:
        return 'A'
    elif marks > 80:
        return 'B'
    elif marks >= 60:
        return 'C'
    else:
        return 'D'


print(display_grade(85)) 
print("--------------------------")


a = 9
if (a > 5 and a <= 10):
    print("Hello")
else:
    print("Bye")
print("--------------------------")





def find_largest(a, b, c):
    return max(a, b, c)


print(find_largest(10, 5, 8))