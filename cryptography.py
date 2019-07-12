
def shuffle(text, key):
    ## shuffle the text 
    key = int(key) % 2

    new_text = ""

    if key == 0:
        for x in 0, 1:
            for y in range(x, len(text), 2):
                new_text = new_text + text[y]
        return new_text

    elif key == 1:
        for x in 1, 0:
            for y in range(x, len(text), 2):
                new_text = new_text + text[y]
        return new_text

    else:
        return " invalid key "


def rearrange(text, key):
    ## rearrange shuffled text 
    key = int(key) % 2
    new_text = ""

    if len(text) % 2 == 0:
        half = int(len(text) / 2)
        if key == 0:
            part_1 = text[: half]
            part_2 = text[half:]
        elif key == 1:
            part_1 = text[half:]
            part_2 = text[: half]

    elif len(text) % 2 == 1:
        half = int(len(text) / 2)
        if key == 0:
            half = -half
            part_1 = text[: half]
            part_2 = text[half:]
        elif key == 1:
            part_1 = text[half:]
            part_2 = text[: half]

    for x in range(int(len(text) / 2)):
        new_text += part_1[x]
        new_text += part_2[x]

    if (int(len(text) / 2)) < (len(text) / 2):

        new_text += part_1[-1]

    return new_text


def ceaser_cipher(text, key, operation):
    ## using the ceaser cipher methon 
    
    operation = int(operation) % 2
    key = int(key)

    if operation == 0:
        pass
    elif operation == 1:
        key = -(key)

    new_text = ""
    alphabet = "euaglvQTOJDXNrishzbWYPHSCMqtodjxnEULGAVwypfkcmRIKFZB"
    numbers = "4561237890"

    for char in text:
        if char in alphabet:
            new_text += alphabet[((alphabet.find(char) +
                                      key) % len(alphabet))]

        elif char in numbers:

            new_text += numbers[((numbers.find(char) +
                                     key) % len(numbers))]

        else:
            new_text += char

    return new_text


def encrypt(text, key):
    for k in str(key):
        text = shuffle(text, int(k))
        text = ceaser_cipher(text, int(k), 0)
    return text


def decrypt(text, key):
    for k in reversed(str(key)):
        text = rearrange(text, int(k))
        text = ceaser_cipher(text, int(k), 1)
    return text

