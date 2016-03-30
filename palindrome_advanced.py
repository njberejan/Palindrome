import re

# def reversed_string(sentence):
# #recursive function to reverse string
#     if len(sentence) == 0:
#         return ''
#     else:
#         return reversed_string(sentence[1:]) + sentence[0]

def is_palindrome(sentence):
#uses iterative to solve, above function not called so commented out.
    sentence = re.sub(r'[^A-Za-z0-9]', '', sentence).lower()
    sentence_rev = sentence[::-1]
    if sentence == sentence_rev:
        return True
    else:
        return False

def main():
#main function which obtain input, removes chaff, and runs comparison function above
    sentence = input("Please enter a sentence to determine if it is palindromic: ")
    if is_palindrome(sentence):
        print("Is a palindrome")
    else:
        print("Is not a palindrome")

if __name__ == '__main__':
    main()
