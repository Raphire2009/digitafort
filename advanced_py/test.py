"""
import asyncio
import time 


async def fetch_data(url):
    print(f"start fetching data")
    await asyncio.sleep(2)
    print("keep fetching data ")
    return f"Fetched {url}"


async def main():
    urls  = [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3",
        "https://example.com/4"]
    tasks = [fetch_data(url) for url in urls]

    ll = await asyncio.gather(*tasks)
    print(ll)


asyncio.run(main())

"""




"""
import threading
import time 



def print_numbers():
    for number in range(1,9):
        print(number)
        time.sleep(1)

def print_letters():
    for l in ["a","b","c","d","e"] :
        print(l)
        time.sleep(1.5)



threading_one = threading.Thread(target=print_numbers)
threading_two = threading.Thread(target=print_letters)


threading_one.start()
threading_two.start()


threading_one.join()
threading_two.join()

print(" all thread complete")
"""





"""
class Animal:
    def __init__(self):
        self.limb = 4
        self.eye = 2
        self.stomach = 1
        self.ear = 2
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof")
class Cat(Animal):
    def make_sound(self):
        print("Meow")
def animal_sound(animal):
    animal.make_sound()

dog = Dog()
cat = Cat()



animal_sound(dog)
animal_sound(cat)
"""





d = 17

def add(a:int, b:int)->float :
    return float( a+b)



def sub(n):
    if n == 0:          
        return 0
    sub(n-1) 
    return n 

print(sub(3))