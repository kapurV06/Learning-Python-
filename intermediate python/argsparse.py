import sys
import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',type = float, default=1.0, help='please bas krdo')
    parser.add_argument('--y',type = float, default=1.0, help='please bas krdo')
    parser.add_argument('--op',type = str, default=1.0, help='please bas krdo')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
    
def calc(args):
    if args.op =='add':
        return args.x+args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y

if __name__ == '__main__':
 main()