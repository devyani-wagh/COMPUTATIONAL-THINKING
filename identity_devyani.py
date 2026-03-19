x = 10
print("Before:", id(x))

x = 15
print("After:", id(x))


name = "Devyani"
print("Before:", id(name))

name = "Wagh"
print("After:", id(name))


nums = [28, 30]
print("Before:", id(nums))

nums.append(30)
print("After:", id(nums))
