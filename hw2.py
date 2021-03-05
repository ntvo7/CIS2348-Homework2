def extractdate(date):
    correctdate = 0
    new_date = ''
    if date.find(",") != -1:
        mnth_day, year = date.split(',')

        if mnth_day.find(" ") != 1:
            month, day = mnth_day.split(' ')

        correctdate = 1

        day = day.strip()
        month = month.strip()
        year = year.strip()

        if month == "January":
            new_date = '1' + '/'
        elif month == "February":
            new_date = '2' + '/'
        elif month == "March":
            new_date = '3' + '/'
        elif month == "April":
            new_date = '4' + '/'
        elif month == "May":
            new_date = "5" + "/"
        elif month == "June":
            new_date = "6" + "/"
        elif month == "July":
            new_date = "7" + "/"
        elif month == "August":
            new_date = "8" + "/"
        elif month == "September":
            new_date = "9" + "/"
        elif month == "October":
            new_date = "10" + "/"
        elif month == "November":
            new_date = "11" + "/"
        elif month == "December":
            new_date = "12" + "/"
        else:
            correctdate = 0

        new_date += day + '/'
        new_date += year

    if correctdate == 1:
        return new_date
    else:
        return ""
#Part a, remove this main driver to get part b
date = input()
while date != "-1":
    new_date = extractdate(date)
    if new_date != "":
        print(new_date)
    print()
    date = input()

#Part b
f = open('inputDates.txt','r')
f_dates = []
f_dates = f.readlines()
f.close()

for i in range(len(f_dates)-1):
    f_dates[i] = f_dates[i][:-1]
for i in f_dates:
    print(i)
    if i == "-1":
        break
        new_date = extractdate(i)
        if new_date != "":
            print(new_date)
#part c
f2 = open('parsedDates.txt','w')
for i in f_dates:
    if i == "-1":
        break
    else:
        new_date = extractdate(i)
        if new_date != "":
            file.write(new_date + "\n")
f2.close()