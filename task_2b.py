import sys

def main():

    def one_round(first_player, fir_start, fir_stop, second_player, sec_start, sec_stop, count):
        flag = True
        if first_player[fir_start] == '9' and second_player[sec_start] == '0':
            flag = False            
        if first_player[fir_start] > second_player[sec_start] and flag or first_player[fir_start] == '0' and second_player[sec_start] == '9':
            first_player.extend([first_player[fir_start], second_player[sec_start]])
            fir_stop += 2
        else:
            second_player.extend([first_player[fir_start], second_player[sec_start]])
            sec_stop += 2
        return first_player, fir_start + 1, fir_stop, second_player, sec_start + 1, sec_stop, count + 1

    first_player = input().split()
    second_player = input().split()
    fir_start, fir_stop, sec_start, sec_stop = 0, 5, 0, 5 #start указывает на индекс первого элемента, stop - индекс первого "свободного" места
    count = 0
    
    while fir_start < fir_stop and sec_start < sec_stop and count < 10**6:
        first_player, fir_start, fir_stop, second_player, sec_start, sec_stop, count = one_round(first_player, fir_start, fir_stop, second_player, sec_start, sec_stop, count)
    
    if fir_start == fir_stop:
        print('second', count)
    elif sec_start == sec_stop:
        print('first', count)
    else:
        print('botva')


if __name__ == '__main__':
    main()