import csv
# RTS-CBT
time = [];
f_len = [];  counting = []; ctArr = []
f_type = []
f_stype = []
datarate = []
timer = []; f_styper = []
rt = 0; rtArr = []
count = 0

# CTS-CBT
timec = []; f_stypec = []; ctArr = []; counting1 = []
ct = 0; count1 = 0

# ACK-CBT
timea = []; f_stypea = []; atArr = []; counting2 = []
at = 0; count2 = 0

# Beacon CBT
timeb = []; f_stypeb = []; btArr = []; counting3 = []
bt = 0; count3 = 0

# Data CBT
time4 = []; suming4 = []; counting4 = []; datarate4 = []; f_len4 = []
d =0; d1 = []; sum4 =0; count4 =0

CBTtotal = []; Ut = []

with open('ch1_2019-05-03_11.05.00.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        # print(row)
        time.append(float(row[0]))
        f_len.append(int(row[1]))
        f_type.append(int(row[2]))
        f_stype.append(int(row[3]))
        # print(f_stype)
        datarate.append(float(row[4]))
#
with open('Utilization.csv', 'w', newline='') as csvFile:
    csv_writer = csv.writer(csvFile)
    # csv_writer.writerow(["Second", "Utilization"])

#rt is the counter when f_stype = 27 in 1 sec
    for i in range(len(f_stype) -1):
        if(f_stype[i]== 27):
            timer.append(time[i])
            # print(timer)
            f_styper.append(f_stype[i])

    for i in range(len(timer) -2):
        if (abs(int(timer[i]) - int(timer[i + 1])) < 1):
            rt = rt + 1
            # print(rt)
            rtArr.append(rt * 352)
        else:
            rt = 0
            count = count + 1
            counting.append(count)
            # print(counting)

# CTS-CBT
    for i in range(len(f_stype) - 1):
        if(f_stype[i] == 28):
            timec.append(time[i])
            f_stypec.append(f_stype[i])
            # print(f_stypec)

    for i in range(len(timec) - 2):
        if (abs(int(timec[i]) - int(timec[i + 1])) < 1):
            ct = ct + 1
            # print(ctArr)
            ctArr.append(ct * 314)
        else:

            ct = 0
            count1 = count1 + 1
            counting1.append(count1)
            # print(counting1)

# ACK-CBT
    for i in range(len(f_stype) - 1):
        if(f_stype[i] == 29):
            timea.append(time[i])
            f_stypea.append(f_stype[i])
            # print(f_stypea)

    for i in range(len(timea) - 2):
        if (abs(int(timea[i]) - int(timea[i + 1])) < 1):
            at = at + 1
            # print(atArr)
            atArr.append(at * 314)
        else:

            at = 0
            count2 = count2 + 1
            counting2.append(count2)

# Beacon CBT
    for i in range(len(f_stype) - 1):
        if(f_stype[i] == 8):
            timeb.append(time[i])
            f_stypeb.append(f_stype[i])
            # print(f_stypea)

    for i in range(len(timeb) - 2):
        if (abs(int(timeb[i]) - int(timeb[i + 1])) < 1):
            bt = bt + 1
            # print(btArr)
            btArr.append(bt * 354)
        else:

            bt = 0
            count3 = count3 + 1
            counting3.append(count3)

# Data CBT
    for i in range(len(f_type) -1):
        if(f_type[i] == 2):
            time4.append(time[i])
            datarate4.append(datarate[i])
            f_len4.append(f_len[i])
            # print(datarate1)

    for j in range(len(datarate4) -1):
        d = 50 + (192 + (8 * (float((34 + f_len4[j]) / datarate4[j]))))
        # print(d)
        # print(datarate1)
        d1.append(d)


    for i in range(len(time4) -2):
        if (abs(int(time4[i]) - int(time4[i + 1])) < 1):
            sum4 = sum4 + d1[i]
            # print(sum)
            suming4.append(sum4)
            # print(suming4)
        else:
            count4 = count4 + 1
            # print(count)
            counting4.append(count4)
            sum4=0
            # print(counting4)
        # print(suming4)
# Total CBT
    for i in range(len(counting4) -1):
        # total = rtArr[i] + ctArr[i] + atArr[i] + btArr[i] + suming4[i]
        CBTtotal.append(rtArr[i] + ctArr[i] + atArr[i] + btArr[i] + suming4[i])
        # print(CBTtotal)

# Utilization
    for i in range(len(CBTtotal) -1):
        Ut.append((CBTtotal[i] / 1000000) * 100)
        # print(Ut)

    utilization = dict(zip(counting4, Ut))

    # print(goodput)
    for key, value in utilization.items():
        csv_writer.writerow([key, value])



