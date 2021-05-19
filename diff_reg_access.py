import os
import glob

files = glob.glob('./trace/init/*.txt')
pattern = ('read:', 'write:')
traces = []
for f in files:
    trace = []
    out = f + '.out'
    post = open(out, 'w+')
    f = open(f)
    for line in f:
        tmp = line.strip()
        for p in pattern:
            if p in tmp:
                idx = tmp.find(p)
                res = tmp[idx:].split(':')
                to_write = res[0] + ':' + res[1] + ':'
                if res[1] == 'SDDATA':
                    to_write += '00000000'
                else:
                    to_write += res[-1]
                post.write(to_write + '\n')
        if 'end dd' in tmp:
            print("end...")
            break
    post.close()


