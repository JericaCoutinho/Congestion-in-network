import csv

time = []
f_len = []
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

with open('tpt_new.csv', 'w', newline='') as csvFile:
    csv_writer = csv.writer(csvFile)
    # csv_writer.writerow(["Second", "Throughput"])

    for i in range(len(time) -2):
        if(abs(int(time[i]) - int(time[i+1])) < 1):
            sum = sum + f_len[i]
            suming.append(8*(sum / 1000000))

        else:
            count = count + 1
            # sum = 0
            counting.append(count)
            suming.append(0)
            # print(suming)

    throughput = dict(zip(counting, suming))

    # print(throughput)
    for key, value in throughput.items():
        csv_writer.writerow([key, value])


