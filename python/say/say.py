# import espeakng


def say0_9(num):
    digit = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
             5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    return digit[num]


def say_multiples_10(num):
    tens = {10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty',
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
    return tens[num]


def say_teens(num):
    teens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
             15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    return teens[num]


def say0_99(num):
    if num < 10:
        return say0_9(num)
    elif num > 10 and num < 20:
        return say_teens(num)
    elif num in range(10, 99, 10):
        # multiples of ten
        return say_multiples_10(num)
    elif num in range(21, 100):
        # automatically not a multiple of 10
        return f"{say_multiples_10(int(num/10)*10)}-{say0_9(num%10)}"
    else:
        raise Exception(f"{num} out of range for say0_99")


def say0_999(num):
    if num in range(0, 100):
        return say0_99(num)
    elif num in range(100, 999, 100):
        return f"{say0_9(int(num/100))} hundred"
    else:
        return f"{say0_9(int(num/100))} hundred {say0_99(num % 100)}"


def chunk(num):
    words = ['thousand', 'million', 'billion', 'trillion']
    chunked = []
    counter = 0
    while int(num/1000) != 0:
        if num % 1000 != 0:
            chunked.append(num % 1000)
        num = int(num/1000)
        if num % 1000 != 0:
            chunked.append(words[counter])
        counter += 1

    chunked.append(num % 1000)
    # chunked.append(words[counter])
    chunked.reverse()
    return chunked


def say(num):
    if num in range(0, 1000):
        # 100 is not included!!!
        return say0_999(num)
    elif num in range(1000,  1000000000000):
        l = chunk(num)
        text = ''
        for element in l:
            text += " "
            # print(element)
            if type(element) == int:
                if element in range(1, 1000):
                    text += say0_999(element)
                else:
                    raise Exception("Error in chunking", l)
            elif type(element) == str:
                text += element
            # print(text)
        return text.strip()

    else:
        raise ValueError(f"{num} not in range")

        # mySpeaker = espeakng.Speaker()
        # mySpeaker.say('Hello, World!', wait4prev=True)


# Testing `chunk()`
# print(chunk(1002345))
# print(chunk(2000))
# print(chunk(1234567890))
# print(chunk(1000000000))
# print(chunk(2000345))
# # print(say(2000))
# mySpeaker = espeakng.Speaker()
# mySpeaker.say('Hello, World!')
