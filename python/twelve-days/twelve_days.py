def recite(start_verse, end_verse):
    """
    Returns the lyrics to 'The Twelve Days of Christmas' 
    beginning from start_verse,and 
    ending at end_verse 
    """
    counting_string = " twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, a Partridge in a Pear Tree"
    # I have just copied the last line of the song. I have removed the `and`from the sentence, I will manipulate it later
    numbers_list = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    # I need this for the starting portion of every line
    counting_list = counting_string.split(",")
    # this turn all the one ..., two ..., etc into a list
    # next I reverse it to get it in the ascending order
    counting_list.reverse()
    # return_verse is the list of all
    return_verse = []
    # double looping to print all the verses
    # putting -1 in the for statement means I don't have to worry about Python indexing
    for i in range(start_verse-1, end_verse):
        verse_ith = f"On the {numbers_list[i]} day of Christmas my true love gave to me:"
        # We start very line of the lyrics this way
        # i here represents the line number in the lyrics
        
        if i == 0:
            # there is no `and` in the first line of the lyrics, so I am treating it as a separate case
            verse_ith = f"{verse_ith}{counting_list[0]}."
        else:
            j = i
            while j > 0:
                # starting from the ith count in the list, adding them to our string verse_ith
                verse_ith = f"{verse_ith}{counting_list[j]},"
                j -= 1
            # there is an `and` from second line onwards in the lyrics
            verse_ith = f"{verse_ith} and{counting_list[0]}."
        return_verse.append(verse_ith)
    return return_verse

print(recite(1,1))
print(recite(2, 2))
print(recite(3, 3))

