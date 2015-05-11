#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/return/uzi.html
# A: http://www.pythonchallenge.com/pc/return/mozart.html

import calendar
import webbrowser

def main():
    years = [year for year in range(1006, 2000, 10) if calendar.weekday(year, 1, 1) == 3 and calendar.isleap(year)]
    print(years)
    
    webbrowser.open('http://www.dayoftheweek.org/?m=January&d=27&y={year}&go=Go'.format(year=years[-2]))

if __name__ == '__main__':
    main()
