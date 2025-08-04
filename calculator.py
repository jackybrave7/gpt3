import argparse


def main():
    parser = argparse.ArgumentParser(description="Simple CLI calculator")
    parser.add_argument('x', type=float, help='First number')
    parser.add_argument('op', choices=['+', '-', '*', '/'], help='Operation')
    parser.add_argument('y', type=float, help='Second number')
    args = parser.parse_args()

    if args.op == '+':
        result = args.x + args.y
    elif args.op == '-':
        result = args.x - args.y
    elif args.op == '*':
        result = args.x * args.y
    else:
        if args.y == 0:
            raise ZeroDivisionError('division by zero')
        result = args.x / args.y
    print(result)


if __name__ == '__main__':
    main()
