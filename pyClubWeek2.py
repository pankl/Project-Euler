from collections import Counter
import csv

def main():
    d = dict()
    with open('pyClubData.csv', 'rb') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            for i,item in enumerate(row):
                if i not in d.keys():
                    d[i] = list()
                d[i].append(item)
    for k in d.keys():
        dd = Counter(d[k])
        for v in dd.keys():
            print v
            print dd[v] * 1.0 / len(d[k]) * 100


if __name__ == '__main__':
    main()