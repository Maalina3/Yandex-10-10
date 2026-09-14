import sys
import math

def main():
    
    s = input()
    alpf = "qwertyuiopasdfghjklzxcvbnm"
    def count_symbol(s, res):
        if s.count('<') % 2 == 1:
            return (s, 'Impossible')
        if s.count('>') % 2 == 1:
            return (s, 'Impossible')
        if s.count('<') // 2 != s.count('/'):
            return (s, 'Impossible')
        
        if s.count('<') != s.count('>'):
            return (s, 'Impossible')
        
        alteg = [ch for ch in s if ch in alpf]
        for i in alteg:
            if s.count(i) % 2 == 1:
                return (s, 'Impossible')

        return (s, True)
            
    
    res = 0
    s, res = count_symbol(s, res)
  
    if res == True:
        
        
        alteg = [ch for ch in s if ch in alpf]
        alteg.sort()
        alteg = "".join([ch for ch in alteg[::2]])
        
        tegs = s.count('/')
        step = math.ceil(len(alteg) / tegs)
        
        start = 0
        buk = []
        for i in range(tegs):
            buk.append(alteg[start:start+step])
            start += step
            
        
        for i in buk:
            print(f'<{i}></{i}>', end='')
        
        
    else: 
        print(res)


if __name__ == '__main__':
    main()
