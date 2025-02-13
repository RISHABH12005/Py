''' Write a python script to read a paragraph and print its words in sorted order 
Sample input: jaypee university of engineering and technology raghogarh guna madhya pradesh 
Sample Output: and engineering guna jaypee madhya of pradesh raghogarh technology university '''
def sort_paragraph(paragraph):
    words = paragraph.split()
    words.sort()
    return ' '.join(words)
paragraph = "JUET raghogarh guna MP"
print(sort_paragraph(paragraph))
