#Input and Conditions Weather Program
temp = 0
print('Please enter the current temperature:')
temp = int(input(''))
if temp > 90:
    print('Wear Shorts')
elif temp > 70:
    print('Short sleeves are fine')
elif temp > 50:
    print('Wear a jacket')
elif temp > 32:
    print('Wear a heavy coat')
elif temp <= 32:
    print('Stay Inside')
while temp < 999:
    temp = 0
    print('Please enter the current temperature:')
    temp = int(input(''))
    if temp > 90:
        print('Wear Shorts')
    elif temp > 70:
        print('Short sleeves are fine')
    elif temp > 50:
        print('Wear a jacket')
    elif temp > 32:
        print('Wear a heavy coat')
    elif temp <= 32:
        print('Stay Inside')
