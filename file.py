from time import sleep
def ice_cream(ic):
    def wrapper():
        print("Machine started")
        flavor = ic()
        for t in range(5,0,-1):
            print(t)
            sleep(5)
        print(f"Your {flavor} ice cream is ready")
        print("Machine shutdown!")
    return wrapper