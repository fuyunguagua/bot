from mergescore import dump_sorted_result
a = {}
b = {}
final = {}
# with open('./oddball_16_9_scores_p') as f:
with open('./sum.csv') as f:
    for line in f:
        id = line[0:-1].split(',')[0]
        score = float(line[0:-1].split(',')[1])
        a[id] = score

with open('./cv.csv') as f:
    for line in f:
        id = line[0:-1].split(',')[0]
        score = float(line[0:-1].split(',')[1])
        b[id] = score

for key in a:
    final[key] = a[key] + b[key]

sorted_result = sorted(final.iteritems(),key = lambda c:c[1])

dump_sorted_result(sorted_result,'finalscore.csv')

def dump_ip(sorted_result):
    import csv
    ip_map = {}
    ips = []
    with open('ip_map.csv') as f:
        for line in f:
            id = int(line[0:-1].split(' ')[0])
            ip = line[0:-1].split(' ')[1]
            ip_map[id] = ip

    top1in10 = len(sorted_result) / 10
    for index,item in enumerate(sorted_result):
        if index > top1in10-1:
            break
        ips.append(ip_map[int(item[0])])

    with open('iptop1in10.csv','wb') as f:
        writer = csv.writer(f,delimiter = ' ')
        for ip in ips:
            writer.writerow([ip])
dump_ip(sorted_result)