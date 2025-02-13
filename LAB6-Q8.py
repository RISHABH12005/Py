''' Write a function translate() that will translate a text into "rovarspraket" (Swedish for "robber's language").
That is, double every consonant and place an occurrence of "o" in between.
For example, translate("this is fun") should return the string "tothohisos isos fofunon". '''
def translate(text):
    result = ""
    for char in text:
        if char.lower() not in 'aeiou ':
            result += char + 'o' + char
        else:
            result += char
    return result
