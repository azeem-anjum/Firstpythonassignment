# Write a program to determine if a given character is a vowel or consonant.
chr = input("Enter a Alphabet: ")

if chr in ('a', 'e', 'i', 'o', 'u', "A", 'E', 'I', 'O', 'U'):
    print("This is a vowel: ")
else:
    print("This is a consonant: ")