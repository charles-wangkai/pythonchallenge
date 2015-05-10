#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/return/bull.html
# A: http://www.pythonchallenge.com/pc/return/5808.html

def look_and_say(number):
    result = ''
    current = None
    count = 0
    for i in range(len(number)):
        if number[i] == current:
            count += 1
        else:
            if current:
                result += str(count) + current
            count = 1
        current = number[i]
    result += str(count) + current
    return result

def main():
    number = '1'
    for i in range(30):
        number = look_and_say(number)
    print(len(number))

if __name__ == '__main__':
    main()
