def count_kades(s, k=3):
    kades = [[]]
    for i in range(0, k):
        new_kades = []
        for kade in kades:
            new_kades.append(kade + ['1'])
            kade.append('0')
        kades += new_kades
    kades.sort()
    counters = {}
    for kade in kades:
        counters[''.join(kade)] = [0, 0]
    #print(counters)
    for i in range(0, len(s) - k):
        counters[s[i:i + k]][int(s[i + k])] += 1
    return counters



def read_str():
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
            return ''.join(all_chars)
            #print('Final data string:')
            #print(''.join(all_chars))

s = read_str()
print('Final data string:')
print(s)

counters = count_kades(s)
for key in counters.keys():
    print(f'{key}: {counters[key][0]},{counters[key][1]}')




