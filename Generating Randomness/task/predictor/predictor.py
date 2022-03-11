from random import randint, choice

def gen_kades(k=3):
    kades = [[]]
    for i in range(0, k):
        new_kades = []
        for kade in kades:
            new_kades.append(kade + ['1'])
            kade.append('0')
        kades += new_kades
    kades.sort()
    return kades

def count_kades(s, k=3):
    counters = {}
    kades = gen_kades(k)
    for kade in kades:
        counters[''.join(kade)] = [0, 0]
    #print(counters)
    for i in range(0, len(s) - k):
        counters[s[i:i + k]][int(s[i + k])] += 1
    return counters

def read_data_str():
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

def predict_str(ts, counters, k=3):
    ps = []
    for i in range(k):
        ps.append(str(randint(0, 1)))
    for i in range(k, len(ts)):
        #print(ts[i - k:i])
        #print(counters[ts[i-k:i]])
        if counters[ts[i - k:i]][0] > counters[ts[i - k:i]][1]:
            ps.append('0')
        elif counters[ts[i - k:i]][0] < counters[ts[i - k:i]][1]:
            ps.append('1')
        else:
            ps.append(str(randint(0, 1)))
    ps = ''.join(ps)
    return ps

def print_accuracy(ts, ps, k=3):
    right_guesses = 0
    for i in range(k, len(ts)):
        if ps[i] == ts[i]:
            right_guesses += 1
    percent = (right_guesses / (len(ts) - k)) * 100
    print(f'Computer guessed right {right_guesses} '
          f'out of {len(ts) - k} symbols ({round(percent, 2)} %)')

ds = read_data_str()
print('Final data string:')
print(ds)

counters = count_kades(ds)
#for key in counters.keys():
    #print(f'{key}: {counters[key][0]},{counters[key][1]}')

print('Please enter a test string containing 0 or 1:')
ts = input().strip()
ps = predict_str(ts, counters)
print('prediction')
print(ps)

print_accuracy(ts, ps)






