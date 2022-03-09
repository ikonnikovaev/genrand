MIN_LEN = 100
all_chars = []
cur_len = 0
while cur_len < MIN_LEN:
    print('Print a random string containing 0 or 1:')
    chars = [ch for ch in input() if ch == '0' or ch == '1']
    all_chars += chars
    cur_len += len(chars)
    if cur_len < MIN_LEN:
        print(f'Current data length is {cur_len}, {MIN_LEN - cur_len} symbols left')
    else:
        print('Final data string:')
        print(''.join(all_chars))

