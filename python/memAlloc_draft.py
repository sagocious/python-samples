class Block:
    def __init__(self, pid, start, size):
        self.startAddr = start
        self.size = size
        self.isFree = False
        self.pid = pid
        self.next = None

    def endAddr(self):
        return self.startAddr + self.size

    def makeFree(self):
        self.isFree = True
        self.pid = -1

    def setPID(self, pid):
        self.pid = pid
        self.isFree = False

class Memory:
    def __init__(self, size):
        self.head = Block(-1, 0, size)
        self.head.makeFree()

    def isExists(self, pid):
        cur = self.head
        while cur!=None:
            if cur.pid == pid:
                return True
            cur = cur.next
        return False

    def allocate(self, pid, size):
        if self.isExists(pid):
            print("processId" + pid + " is already exists")
            return
        
        cur = self.head
        prev = None
        found = False
        while cur != None and not found:
            if cur.isFree and (size <= cur.size):
                found = True
            else:
                prev = cur
                cur = cur.next

        if found:
            if cur.size == size:
                cur.setPID(pid)
            else:
                b = Block(pid, cur.startAddr, size)
                if prev != None:
                    prev.next = b
                else:
                    self.head = b
                b.next = cur
                cur.size -= size
                cur.startAddr += size
            print("Allocated!")
        else:
            print("No space")

    def terminate(self, pid):
        cur = self.head
        while cur!=None:
            if cur.pid == pid:
                cur.makeFree()
                print("process {0} terminated!".format(pid))
                return
            cur = cur.next
            
    def show(self):
        print('')
        cur = self.head
        while cur != None:
            print("pid:{0}\trange:{1}-{2}\tsize:{3}".format(cur.pid, cur.startAddr, cur.endAddr(), cur.size))
            cur = cur.next
        print(" (-1 is free space)")

print(" Allocation:\t[A <pid> <size>]\n Termination:\t[T <pid>]\n Show:\t\t[show]")

m = Memory(2560)
m.allocate(400, 'OS')

while True:
    s = raw_input("Command: ").split()

    if s[0]=="A":
        m.allocate(s[1], int(s[2]))
    elif s[0]=="T":
        m.terminate(s[1])
    elif s[0]=="show":
        m.show()
    elif s[0] == "exit":
        exit()

