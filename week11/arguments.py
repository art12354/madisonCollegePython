import argparse
import sys

parser = argparse.ArgumentParser(description='This is Arthur\'s script')

parser.add_argument('-m', metavar='BASIC', dest='myVar', help='Enter some text')
parser.add_argument('-i', '--integer', dest='varInt', metavar='[an integer]', type=int, help='<required> Enter a simple integer')
parser.add_argument('-d', '--float', dest='varFloat', metavar='[a float]', type=float, help='Enter a simple float')
parser.add_argument('-s', '--string', dest='varString', metavar='[a string]', type=str, help='Enter a simple string')
parser.add_argument('-l', dest='varList', metavar='[strings]', nargs='+', help='Enter a list of strings (space delimited)')
parser.add_argument('-t', '--set-true', dest='bool_t', action='store_true', help='Toggle from default False to True')
parser.add_argument('-f', '--set-false', dest='bool_f', action='store_false', help='Toggle from default True to False')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

if(args.varInt):
    print(f'Integer: {args.varInt}')
if(args.varFloat):
    print(f'Float: {args.varFloat}')
if(args.varString):
    print(f'String: {args.varString}')
if(args.varList):
    print(f'List: {args.varList}')
