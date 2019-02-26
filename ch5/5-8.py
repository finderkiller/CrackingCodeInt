#! /usr/bin/python3
import sys



def sol(screen, w, x1, x2, y):
    start_offset = x1 % 8
    start_full_byte = x1 / 8
    if (start_offset != 0):
        start_full_byte += 1

    end_offset = x2 % 8
    end_full_byte = x2 / 8
    if (end_offset != 7):
        end_full_byte -= 1

    for i in range(start_full_byte, end_full_byte + 1)
        screen[w/8 * y + i] = int('ff', 16)

    start_mask = int('ff', 16) >> start_offset
    end_mask = ~(int('ff', 16) >> (end_offset + 1))

    if (x1 / 8 == x2 / 8):
        mask = start_mask & end_mask
        screen[w/8 * y + x1/8] |= mask
    else:
        if (start_offset != 0):
            byte_num = w/8 * y + start_full_byte - 1
            screen[byte_num] |= start_mask
        if (end_offset != 7):
            byte_num = w/8 * y + end_full_byte + 1
            screen[byte_num] |= end_mask
def main(argv):
    screen = []
    width = 4
    sol(screen, width, int(argv[1]), int(argv[2]), int(argv[3]))

if __name__ == "__main__":
    main(sys.argv)
