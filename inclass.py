
obj = [1,2,3]

print(obj)

len(obj)

# function
# syntax
# def [name](parameters):

def talk():
    print("...")
    print("ya ya ya")
    print("...")
    print("done talking")

def blender(fruit_1, fruit_2):
    print("...blending...")
    smoothie = "You made a " + fruit_1 + " and " + fruit_2 + " smoothie!"
    return smoothie


s1 = blender("straberry","banana")
s2 = blender("kiwi","mango")
s3 = blender("blueberry","raspberry")

print (s1)
print (s2)
print (s3)

print(blender("passion fruit","watermelon"))

def print_up_to(num):
    for num in range (num + 1):
        print(num)
   
print_up_to(15)

def area(length, width):
    return length * width

print (area(10,20))
print (area(11,11))