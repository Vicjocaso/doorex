# doorex

exercises of doors

Door: Open, Closed, Locked, Unlocked
	Open -> Closed
	Closed -> Open
	Unlocked -> Locked
	Locked -> Unlocked
	
	Open -> Open : error
	Closed -> Closed : error
	...
	
--------------------------------------------
Door.OpenAndUnlocked(key: guid)
Door.OpenAndLocked(key: guid)
Door.ClosedAndUnlocked(key: guid)
Door.ClosedAndLocked(key: guid)

val door = Door.xyz

door.Open() //when Locked error 
door.Close()
door.Lock()
door.Unlock(key)

door.IsOpen, IsClosed, IsLocked, IsUnlocked -> boolean
