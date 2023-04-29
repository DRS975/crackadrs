import argparse
import hashlib
import os
import pyfiglet

# Initialize argument parser
parser = argparse.ArgumentParser(description='Password cracker command line tool')

# Define arguments
parser.add_argument('-w', '--wordlist', metavar='WORDLIST_PATH', help='Path to wordlist file')
parser.add_argument('-t', '--hash-type', metavar='HASH_TYPE', help='Type of hash to crack (md5, sha1, sha256, sha512, whirlpool)')
parser.add_argument('-c', '--hash', metavar='HASH', help='Hash to crack')
parser.add_argument('-H', '--show-help', action='store_true', help='Show help message')

# Parse arguments
args = parser.parse_args()

# Create and print the banner
banner = pyfiglet.figlet_format("DRS975")
print(banner)

if args.show_help:
    parser.print_help()
elif not args.wordlist or not args.hash_type or not args.hash:
    print("Error: missing arguments")
    parser.print_usage()
else:
    # Read the wordlist file
    with open(args.wordlist, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            word = line.strip()
            # Generate the hash of the current word
            if args.hash_type == 'md5':
                hashed_word = hashlib.md5(word.encode()).hexdigest()
            elif args.hash_type == 'sha1':
                hashed_word = hashlib.sha1(word.encode()).hexdigest()
            elif args.hash_type == 'sha256':
                hashed_word = hashlib.sha256(word.encode()).hexdigest()
            elif args.hash_type == 'sha512':
                hashed_word = hashlib.sha512(word.encode()).hexdigest()
            elif args.hash_type == 'whirlpool':
                hashed_word = hashlib.new('whirlpool', word.encode()).hexdigest()
            else:
                print(f"Error: invalid hash type ({args.hash_type})")
                exit(1)

            # Check if the generated hash matches the target hash
            if hashed_word == args.hash:
                print(f"Password found: {word}")
                exit(0)
        print("Password not found in the wordlist.")
