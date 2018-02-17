''' TotalSpam = 0
SpamCounter = 0
SpamAverage = 0
fname = input('Enter File Name:')
try:
    fhand = open(fname)
except:
    print ('File can not be opened:', fname)
    exit()
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        try:
            TotalSpam +=float(line[20:-1])
            SpamCounter +=1
        except:
            continue
SpamAverage = TotalSpam/SpamCounter
print ('Average spam confidence:', str(SpamAverage)) '''

fname = input('Enter File Name:')
if fname ==('na na boo boo'):
    print ('NA NA BOO BOO TO YOU - YOU HAVE BEEN PUNKD!')
    exit()
try:
    fhand = open(fname)
except:
    print ('File can not be opened:', fname)
    exit ()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count +=1
print ('There were', count, 'subject lines in', fname)
