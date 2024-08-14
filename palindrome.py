def palindrome(number):
    numbers = int(number)
    reversed = int(number[::-1])
    if numbers == reversed:
        print(f"the {numbers} is a palindrome")


for n in range(0, 10002):
    palindrome(str(n))
