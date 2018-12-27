def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters //2)
    print (result)


yell(" You are doing great ")
yell("dont forget to ask for help")
yell("dont repeat yourself")
