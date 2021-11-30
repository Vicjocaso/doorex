class Door:

    def __init__(open, close, locked, unlock):
        Door.open = open
        Door.close = close
        Door.lock = locked
        Door.unlock = unlock

    def Open(door):
        if door == isOpen:
            return "Open door"
        else:
            return "close door"

    def close(door):
        if door == isClose:
            return "Open door"
        else:
            return "close door"

    def locked(door):
        if door == isOpen:
            return "Open door"
        else:
            return "close door"

    def unlock(door):
        if door == isOpen:
            return "Open door"
        else:
            return "close door"


door = ""
print(Door.Open(door))
