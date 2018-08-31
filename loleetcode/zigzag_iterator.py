class ZigzagIterator(object):
    def __init__(self, v1, v2):
        self.queue = [x for x in (v1, v2) if x]
        
    def next(self):
        v = self.queue.pop(0)
        ret = v.pop(0)
        if v: 
            self.queue.append(v)
        return ret
        
    def hasNext(self):
        if self.queue: return True
        return False
        
if __name__ == '__main__':
    test1 = [1,2,3]
    test2 = [4,5,6]
    i, v = ZigzagIterator(test1, test2), []
    while i.hasNext():
        v.append(i.next())