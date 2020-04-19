import numpy as np
import asyncio


class Store:
    data = dict()
    
    @classmethod
    def set(s, key, val):
        s.data[key] = val
        return "OK"
        
    @classmethod
    def get(s, key):
        if key in s.data:
            return str(s.data[key])
        else:
            return "NULL"
            
    @classmethod
    def delete(s, key):
        if key in s.data:
            del s.data[key]
            return "OK"

    @classmethod
    async def expire(s, key, value):
        await asyncio.sleep(float(value))
        s.delete(key)
        
    @classmethod    
    def zadd(s, key, *items):
        a = [[],[]]
        if key in s.data:
            a = s.data.get(key)
        
        data = zip(items[::2], items[1::2])

        for name , value in data:
            if name in set(a[0]):
                a[1][a[0].index(name)] = float(value)
            else:
                a[0].append(name)
                a[1].append(value)
        
        s.data[key] = a
        return "OK"

    @classmethod
    def zrank(s, key, value):
        a = s.data.get(key)
        if str(value) in set(a[0]):
            val = a[1][a[0].index(value)]
            np_a = np.array(a[1])
            np_a = np.sort(np_a)
            return str( min(np.where(np_a == val)[0])+1)
        
        return "NOT FOUND"

    @classmethod
    def zrange(s, key, mn, mx):
        ans = []
        a = s.data.get(key)
        for i in range(len(a[1])):
            if float(a[1][i]) <= float(mx) and float(a[1][i]) >= float(mn):
                ans = ans + [a[0][i]]
                
        return str(ans)
            
    @classmethod
    def lpush(s, key, val):
        if key in s.data and isinstance(s.data[key], list):
            s.data[key].insert(0, val)
        else:
            s.data[key] = [val]
        return "OK"
            
    @classmethod
    def rpush(s, key, val):
        if key in s.data and isinstance(s.data[key], list):
            s.data[key].append(val)
        else:
            s.data[key] = [val]
        return "OK"
            
    @classmethod
    def lpop(s, key):
        if key in s.data and isinstance(s.data[key], list):
            return s.data[key].pop(0)
        else:
            return "NULL"
    
    @classmethod
    def rpop(s, key):
        if key in s.data and isinstance(s.data[key], list):
            return s.data[key].pop()
        else:
            return "NULL"
            
    @classmethod
    def llen(s, key):
        if key in s.data and isinstance(s.data[key], list):
            return str(len(s.data[key]))
        else:
            return "0" 

            