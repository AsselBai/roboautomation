'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def IsPolindrome(word):
   return word == word[::-1] 

word =input("Please, type a word:  ");
word =word.lower()
word= word.strip()

result = IsPolindrome(word)

if result:
    print("This is a polindrome")
else:
    print("This isn't a polindrome")