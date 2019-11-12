def fizzbuzz(num):
    say = ''
    if num % 3 == 0:
        say = 'Fizz'
    if num % 5 == 0:
        say += ('Buzz', ' Buzz')[num % 3 == 0]
    # if say is not an empty string return it otherwise return num
    return (num, say)[len(say) > 0]
