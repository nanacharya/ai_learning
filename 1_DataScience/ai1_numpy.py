import numpy as np

array = np.array([1,2,3,4,5,6])
print(array)

zeroDiamnos = np.zeros((5,5))
print(zeroDiamnos)
print("test")


oneDimenstion = np.ones((5,4))
print(oneDimenstion)


rangeArrya = np.arange(10, 100, 5)
print(rangeArrya)

lineSpan = np.linspace(10, 100, 4)
print(lineSpan)


# reshape diamansion
arr = np.array([1,2,3,4,5,6])
reshape = arr.reshape(2, 3)
print("---------><---------")
print(reshape)
reshape1 = arr.reshape(3,2)
print(reshape1)

print("---------><---------")
arr = np.array([1,2,3,4,5,6])
expanded = arr[1:, np.newaxis]
print(expanded)

print("---------><---------")
expanded = arr[3:, np.newaxis]
print(expanded)


##Mathmatical Operation
print("---------><---------")
a = np.array([1,2,3,4,5,6])
b = np.array([7,8,9,10,11,12])

print((a + b))
print("---------><---------")
print(a-b)
print(a*b)
print((b/a))

print((np.sqrt(a)))
print(np.max(a))
print(np.min(a))
print(np.sum(b))

print("---------><---------")

arr = np.array([1,2,3,4,5,6])
print(arr[2])
print((arr[2:3]))
print(arr[:2])


print("---------><---------")

arr = np.array([[1,2,3], [5,6,7]])
print(arr)
print((arr + 10))
vector = np.array([1,5,6])

print(arr+ vector)


print("---------><---------")

print ("sum  " ,  np.sum(arr))
print("min  " , np.min(arr))
print("max  " , np.max(arr))
print("mean  " , np.mean(arr))


# Random generation

arr = np.random.randn(5,5)
print(arr)

randomIntger = np.random.random_integers(0,10, size=(5,5))
print(randomIntger)
print(randomIntger)

np.random.seed(42)
print(randomIntger)
print(randomIntger)

