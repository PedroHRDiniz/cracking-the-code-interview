import time

#first, define the linked list
class Node:
  next = None
  def __init__(self,data):
    self.data = data
    self.timestamp = time.time()
    
class SinglyLinkedList:
  
  def __init__(self):
    self.head = None

  def setChild(self, node):
    if self.isEmpty():
      self.head = node
      return
    parent = self.head
    while parent.next is not None:
      parent = parent.next
    parent.next = node
  
  def isEmpty(self):
    return self.head is None
  
  def removeHead(self):
    if self.isEmpty():
      return None
    oldHead = self.head
    newHead = self.head.next    
    self.head = newHead
    return oldHead

#using a class to distinguish between types and names
class Animal:
  def __init__(self, animalType, name):
    self.animalType = animalType
    self.name = name

enumAnimalType = dict(dog=1, cat=2)

def enqueue(animal):
  if animal.animalType is enumAnimalType['dog']:
    dog = Node(animal)
    dogList.setChild(dog)
  elif animal.animalType is enumAnimalType['cat']:
    cat = Node(animal)
    catList.setChild(cat)

def dequeueDog():
  return dogList.removeHead()

def dequeueCat():
  return catList.removeHead()

def dequeueAny():
  oldestCat = catList.head
  oldestDog = dogList.head
  if oldestCat is None and oldestDog is None:
    return None
  elif oldestCat is None:
    return dequeueDog()
  elif oldestDog is None:
    return dequeueCat()
  else:
    oldestCatTimestamp = oldestCat.timestamp
    oldestDogTimestamp = oldestDog.timestamp 
    if oldestDogTimestamp <= oldestCatTimestamp:
      return dequeueDog()
    else:
      return dequeueCat()

#proving that it works, hehe
catList = SinglyLinkedList()
dogList = SinglyLinkedList()

dog1 = Animal(enumAnimalType['dog'], 'Belinha')
dog2 = Animal(enumAnimalType['dog'], 'Caramelo')
cat1 = Animal(enumAnimalType['cat'], 'Marie')
cat2 = Animal(enumAnimalType['cat'], 'Oliver')
cat3 = Animal(enumAnimalType['cat'], 'Garfield')

enqueue(dog2)
enqueue(dog1)
enqueue(cat2)
enqueue(cat1)
enqueue(cat3)

print(dequeueAny().data.name)
print(dequeueDog().data.name)
print(dequeueCat().data.name)
print(dequeueAny().data.name)