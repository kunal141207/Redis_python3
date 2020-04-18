import numpy as np
import asyncio

class Store:
    data = dict()
    
    def set(self, key, val):
        self.data[key] = val
        return "OK"
        
    def get(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return "NULL"
            
    def delete(self, key):
        if key in self.data:
            del self.data[key]
            return "OK"

    async def expire(self, key, value):
        await asyncio.sleep(value)
        self.delete(key)
        return str(key)+"EXPIRED" 
        
    def zadd(self, key, *items):
        a = [[],[]]
        if key in self.data:
            a = self.data.get(key)
        
        data = zip(items[::2], items[1::2])

        for name , value in data:
            if name in set(a[0]):
                a[1][a[0].index(name)] = float(value)
            else:
                a[0].append(name)
                a[1].append(value)
        
        self.data[key] = a
        return "OK"


    def zrank(self, key, value):
        a = self.data.get(key)
        if key in set(a[0]):
            val = a[1][a[0].index(value)]
            np_a = np.array(a[1])
            np_a = np.sort(np_a)
            return min(np.where(np_a == val)[0])+1
        
        return -1


    def zrange(self, key, mn, mx):
        ans = []
        a = self.data.get(key)
        for i in range(len(a[0])):
            if a[1][i] <= mx and a[1][i] >= mn:
                ans = ans + a[0][i]
                
        return ans

            
    def lpush(self, key, val):
        if key in self.data and isinstance(self.data[key], list):
            self.data[key].insert(0, val)
        else:
            self.data[key] = [val]
        return "OK"
            
    def rpush(self, key, val):
        if key in self.data and isinstance(self.data[key], list):
            self.data[key].append(val)
        else:
            self.data[key] = [val]
        return "OK"
            
    def lpop(self, key):
        if key in self.data and isinstance(self.data[key], list):
            return self.data[key].pop(0)
        else:
            return "NULL"
    
    def rpop(self, key):
        if key in self.data and isinstance(self.data[key], list):
            return self.data[key].pop()
        else:
            return "NULL"
            
    def llen(self, key):
        if key in self.data and isinstance(self.data[key], list):
            return str(len(self.data[key]))
        else:
            return "0"
            
