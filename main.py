class Door:

    def __init__(open, close, locked, unlock):
        Door.open = open
        Door.close = close
        Door.lock = locked
        Door.unlock = unlock

    def isOpen(door):
        if door == Door.open:
            print("Open Door")

    def isClose(door):
        if door == Door.close:
            print("Close Door")

    def isLocked(door):
        if door == Door.locked:
            print("Locked Door")

    def isUnlock(door):
        if door == Door.unlock:
            print("Unlock Door")


door = ""
print(Door.Open(door))

