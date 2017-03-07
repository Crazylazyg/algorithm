def reverse (text):
    return text[::-1]

def is_palindrome (text):
    return text == reverse(text)

text = raw_input("Please enter something:")
text = text.lower()
text = text.replace(' ','')
text = text.replace(',','')
text = text.replace('.','')

if is_palindrome(text):
    print "Yes, it is a palindorme"
else:
    print "No, it is not a palindorme"