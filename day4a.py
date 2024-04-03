#1.LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:  # Check if both numbers are even
        return min(a, b)
    else:
        return max(a, b)
print(lesser_of_two_evens(2, 4))  
print(lesser_of_two_evens(2, 5))

# 2.ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    words = text.split()
    return words[0][0].lower() == words[1][0].lower()
print(animal_crackers('Levelheaded Llama'))  
print(animal_crackers('Crazy Kangaroo'))

# 3.MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 *or* if one of the integers is 20. If not, return False
def makes_twenty(n1, n2):
    return n1 == 20 or n2 == 20 or n1 + n2 == 20
print(makes_twenty(20, 10))  
print(makes_twenty(12, 8))    
print(makes_twenty(2, 3))

# 4.OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    return name[:3].capitalize() + name[3:].capitalize()
print(old_macdonald('macdonald'))
     
#5. MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence
print(master_yoda('I am home'))
print(master_yoda('We are ready'))

#6. ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)
print(almost_there(90))   
print(almost_there(104))  
print(almost_there(150))  
print(almost_there(209)) 

#  LEVEL 2 PROBLEMS
#7. Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))     
print(has_33([1, 3, 1, 3]))   
print(has_33([3, 1, 3]))   

# 8.PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result
print(paper_doll('Hello')) 
print(paper_doll('Mississippi'))

# 9.Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a, b, c):
    total = sum((a, b, c))
    if total <= 21:
        return total
    elif 11 in (a, b, c):
        total -= 10
    return 'BUST' if total > 21 else total
print(blackjack(5, 6, 7))   
print(blackjack(9, 9, 9))  
print(blackjack(9, 9, 11))

# 10.SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_69(arr):
    total = 0
    skip = False
    
    for num in arr:
        if num == 6:
            skip = True
        elif num == 9 and skip:
            skip = False
        elif not skip:
            total += num    
    return total
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

#  CHALLENGING PROBLEMS
# 11.SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    has_zero = False
    has_double_zero = False
    for num in nums:
        if num == 0:
            if not has_zero:
                has_zero = True
            elif has_zero and not has_double_zero:
                has_double_zero = True
        elif num == 7:
            if has_zero and has_double_zero:
                return True

    return False
print(spy_game([1,2,4,0,0,7,5]))  
print(spy_game([1,0,2,4,0,5,7]))  
print(spy_game([1,7,2,0,4,5,0]))  

# 12.COUNT PRIMES: Write a function that returns the *number* of prime numbers that exist up to and including a given number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes, len(primes)

primes_list, primes_count = count_primes(100)
print("Prime numbers up to 100:", primes_list)
print("Total number of prime numbers up to 100:", primes_count)

# 13.PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
def print_big_E():
    pattern = ['*****', '*    ', '*****', '*    ', '*****']
    for line in pattern:
        print(line)
print_big_E()
# A
def print_big_A():
    pattern = ['  *  ', ' * * ', '*****', '*   *', '*   *']
    for line in pattern:
        print(line)
print_big_A()


