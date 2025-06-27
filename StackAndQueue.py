L1= []
L1.append(20)
L1.append(30)
L1.append(50)
L1.append(60)
L1.append(90)
L1.append(40)

print(L1)
L1.pop(5)

print(L1)

# Queue

queue = ["Amar", "Aniket", "Yogesh"]
queue.append("Ram")
queue.append("Aman")
print("Initial Queue:",queue)

# Removes the first item at index 0 which is Amar
print("After removing first element",queue.pop(0))

print(queue)

# Removes the first item at index 0 which is Aniket 
print(queue.pop(0))

print(queue)
