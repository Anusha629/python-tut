# fizzbizz
def fizzbizz(n):
    for i in range(1,n+1):
        if i % 15 == 0:
            print("fizzbizz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("bizz")
        else:
            print(i)

n=50
fizzbizz(n)


#  palindrome

def palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
input = "dad"
output = palindrome(input)
print(output)


# panagram 

def panagram(s):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()

    for letter in alphabets:
        if letter not in s:
            return False 
    return True

input = "he quick brown fox jumps over the lazy dog"
output = panagram(input)
print(output)


#occrance

def freq(s):
    freq_dict = {}
    for letter in s:
        if letter in freq_dict:
            freq_dict[letter] += 1
        else:
            freq_dict[letter] = 1
    return freq_dict

input = "helloO galaxy"  
output = freq(input)
print(output)
        


