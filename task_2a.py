import sys

def main():
    def queue_processin(line, queue, start, stop):
        if line[:4] == 'push':            
            queue.append(line[5:])
            stop += 1
            return 'ok', queue, start, stop
        if line == 'pop':
            if start < stop:
                start += 1
                return queue[start - 1], queue, start, stop
            else:
                return 'error', queue, start, stop            
        if line == 'front':
            if start < stop:
                return queue[start], queue, start, stop 
            else:
                return 'error', queue, start, stop

        if line == 'size':
            return stop - start, queue, start, stop        
        if line == 'clear':
            start = stop
            return 'ok', queue, start, stop                     
    
    queue = []
    start, stop = 0, 0
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        if line == 'exit':
            print('bye')
            break
        command_result, queue, start, stop = queue_processin(line, queue, start, stop)
        print(command_result)

main()
