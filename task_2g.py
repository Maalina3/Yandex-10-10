def main(): #НЕ РЕШЕНА!!!!!!!!!!!!!!!!
    heap = []

    def insert(heap, n):
        n_index = len(heap)
        heap.append(int(n))
        while True:
            if n_index == 0:
                break
            if heap[n_index] > heap[(n_index - 1) // 2]:
                heap[n_index], heap[(n_index - 1) // 2] = heap[(n_index - 1) // 2], heap[n_index]
                n_index = (n_index - 1) // 2
            else:
                break
        return heap
    
    def extract(heap):
        extracted = heap[0]    
        now_index = 0
        heap[0] = heap[-1]
        while True:
            if len(heap) == 1:
                break        
            if now_index * 2 + 2 < len(heap):                       
                if heap[now_index] > heap[now_index * 2 + 1] and heap[now_index] > heap[now_index * 2 + 2]:
                    break
                elif heap[now_index * 2 + 1] > heap[now_index * 2 + 2]:
                    heap[now_index * 2 + 1], heap[now_index] = heap[now_index], heap[now_index * 2 + 1]
                    now_index = now_index * 2 + 1
                elif heap[now_index * 2 + 2] > heap[now_index * 2 + 1]:
                    heap[now_index * 2 + 2], heap[now_index] = heap[now_index], heap[now_index * 2 + 2]
                    now_index = now_index * 2 + 2
            elif now_index * 2 + 1 > len(heap):
                break
            elif now_index * 2 + 2 == len(heap):
                if heap[now_index] >= heap[now_index * 2 + 1]:
                    break
                elif heap[now_index] < heap[now_index * 2 + 1]:
                    heap[now_index * 2 + 1], heap[now_index] = heap[now_index], heap[now_index * 2 + 1]
                    now_index = now_index * 2 + 1      
        heap.pop()
        return heap, extracted
    
    for i in range(int(input())):
        input_data = input().split()
        if input_data[0] == '0':
            heap = insert(heap, input_data[1])
        else:
            heap, extracted = extract(heap) 
            print(extracted)

main()


#НЕ РЕШЕНА!!!!!!!!!!!!!!!!