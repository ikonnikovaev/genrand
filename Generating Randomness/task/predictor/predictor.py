from random import randint, choice

def gen_kades(k=3):
    # generate all triades -- or, possibly, k-ades :)
    kades = [[]]
    for i in range(0, k):
        new_kades = []
        for kade in kades:
            new_kades.append(kade + ['1'])
            kade.append('0')
        kades += new_kades
    kades.sort()
    return [''.join(kade) for kade in kades]

def count_kades(s, kades):
    counters = {}
    # kades = gen_kades(k)
    k = len(kades[0])
    for kade in kades:
        counters[kade] = [0, 0]
    #print(counters)
    for i in range(0, len(s) - k):
        counters[s[i:i + k]][int(s[i + k])] += 1
    return counters

def read_data_str():
    MIN_LEN = 100
    all_chars = []
    cur_len = 0
    while cur_len < MIN_LEN:
        print(f'The current data length is {cur_len}, {MIN_LEN - cur_len} symbols left')
        print('Print a random string containing 0 or 1:')
        chars = [ch for ch in input() if ch == '0' or ch == '1']
        all_chars += chars
        cur_len += len(chars)
    return ''.join(all_chars)

def read_test_str():
    s = input()
    if s.strip() == 'enough':
        return s
    chars = [ch for ch in s if ch == '0' or ch == '1']
    return ''.join(chars)

def predict_str(ts, counters):
    k = len(list(counters.keys())[0])
    ps = []
    for i in range(k):
        ps.append(str(randint(0, 1)))
    for i in range(k, len(ts)):
        if counters[ts[i - k:i]][0] > counters[ts[i - k:i]][1]:
            ps.append('0')
        elif counters[ts[i - k:i]][0] < counters[ts[i - k:i]][1]:
            ps.append('1')
        else:
            ps.append(str(randint(0, 1)))
    ps = ''.join(ps)
    return ps

def find_accuracy(ts, ps, k=3):
    right_guesses = 0
    all_guesses = len(ts) - k
    for i in range(k, len(ts)):
        if ps[i] == ts[i]:
            right_guesses += 1
    return (right_guesses, all_guesses)


def play(counters):
    k = len(list(counters.keys())[0])
    print('You have $1000. '
          'Every time the system successfully predicts your next press, '
          'you lose $1.\n Otherwise, you earn $1. '
          'Print "enough" to leave the game. Let\'s go!')
    balance = 1000
    print('Print a random string containing 0 or 1:')
    ts = read_test_str()
    #print(ts)

    while (ts != 'enough'):
        if len(ts) > 3:
            ps = predict_str(ts, counters)
            print('prediction')
            print(ps)

            right_guesses, all_guesses = find_accuracy(ts, ps, k)
            wrong_guesses = all_guesses - right_guesses
            percent = (right_guesses / all_guesses) * 100
            print(f'Computer guessed right {right_guesses} '
                  f'out of {all_guesses} symbols ({round(percent, 2)} %)')

            balance -= right_guesses
            balance += wrong_guesses
            print(f'Your balance is now ${balance}')
        print('Print a random string containing 0 or 1:')
        ts = read_test_str()

    print('Game over!')



print('Please give AI some data to learn...')
ds = read_data_str()
print('Final data string:')
print(ds)

kades = gen_kades(3)
counters = count_kades(ds, kades)
#for key in counters.keys():
    #print(f'{key}: {counters[key][0]},{counters[key][1]}')

play(counters)





