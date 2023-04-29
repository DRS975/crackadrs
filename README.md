# crackadrs

crackadrs is a terminal program that cracks a hashed password by checking through a list of passwors usually called wordlist<br>


crackadrs takes two arguments: the path to the wordlist file and the hash value to crack. It then reads the wordlist file and iterates over each word, hashing it using the same algorithm as the target hash. If a matching hash is found, it prints the password to the console. Otherwise, it prints a message indicating that the password was not found.<br>

To use the script, save it as a Python file (crackadrs.py) and run it from the terminal with the following command:<br>

python crackadrs.py -w path_to_wordlist.txt -H $6$SALT$HASH_VALUE<br>


Replace /path/to/wordlist.txt with the actual path to your wordlist file, and replace $6$SALT$HASH_VALUE with the actual hash value you want to crack. You can also use a different hash format by changing the prefix of the hash value <br>
.$1$ for MD5<br>
.$5$ for SHA-256<br>
.$2y$ for bcrypt<br>
