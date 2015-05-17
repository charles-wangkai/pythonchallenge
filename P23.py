#!/usr/bin/env python3

# Q: http://www.pythonchallenge.com/pc/hex/bonus.html
# A: http://www.pythonchallenge.com/pc/hex/ambiguity.html

def main():
    import this
    print()
    
    cipher = 'va gur snpr bs jung?'
    print("".join([this.d.get(c, c) for c in cipher]))

if __name__ == '__main__':
    main()
