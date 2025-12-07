"""
 Exercise2:Thisprogramcountsthedistributionofthehourofthedayforeach
 of themessages.Youcanpull thehour fromthe“From”linebyfindingthetime
 stringandthensplittingthat string intopartsusingthecoloncharacter. Once
 youhaveaccumulatedthecountsforeachhour,printoutthecounts,oneperline,
 sortedbyhourasshownbelow.
 pythontimeofday.py
 Enterafilename: mbox-short.txt
 043
 061
 071
 092
 103
 116
 141
 152
 164
 172
 181
 191
"""
hour_count = dict()
file_name = input("Enter the file name: ")
with open(file_name,"r")as handler:
    for line in handler:
        if line.startswith("From "):
            words = line.split()
            time = words[5]
            hour = time.split(":")[1]
            hour_count[hour] = hour_count.get(hour, 0) + 1

#print(hour_count(x, y) for x, y in hour_count)
for x in sorted(hour_count.keys()):
    print(x, hour_count[x])