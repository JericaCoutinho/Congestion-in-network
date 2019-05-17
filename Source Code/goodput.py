import csv

time = []
f_len = []
f_type = []
time1 = []
f_len1 = []
f_type1 = []
sum = 0
count = 0
counting = []
suming = []
with open('ch1_2019-05-03_11.05.00.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        # print(row)
        time.append(float(row[0]))
        f_len.append(int(row[1]))
        f_type.append(int(row[2]))

with open('goodputoutput.csv', 'w', newline='') as csvFile:
    csv_writer = csv.writer(csvFile)
    # csv_writer.writerow(["Second", "Goodput"])

    for i in range(len(f_type) - 1):
        if (f_type[i] == 2):
            print(time[i])
            f_type1.append(f_type[i])
            time1.append(time[i])
            f_len1.append(f_len[i])

    for i in range(len(time1) -2):
        if (abs(int(time1[i]) - int(time1[i + 1])) < 1):
            sum = sum + f_len1[i]
            suming.append(8*(sum / 1000000)) 
            # print(f_type[i])
            # print(sum)
        else:
            count = count + 1
            # print(count)
            counting.append(count)
            sum=0

    goodput = dict(zip(counting, suming))

    # print(goodput)
    for key, value in goodput.items():
        csv_writer.writerow([key, value])