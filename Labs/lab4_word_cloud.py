# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: Oct 2020
# purpose: Lab 4

class WordCloud:

    # initialises everything
    # everything gets kicked off here
    def __init__(self):
        self.my_dict = self.create_dict()
        # you might like to run the following line only
        # if there wasn't a problem creating the dictionary
        self.create_html(self.my_dict)

    # this function creates the actual html file
    # takes a dictionary as an argument
    # it helps to multiply the key/occurance of word number with 10
    # in order to get a decent size output in the html
    def create_html(self, the_dict):
        fo = open("output.html", "w")
        fo.write('<!DOCTYPE html>\
            <html>\
            <head lang="en">\
            <meta charset="UTF-8">\
            <title>Tag Cloud Generator</title>\
            </head>\
            <body>\
            <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')

        # your code goes here!
        fo.write('<span style="font-size: 20px"> Hello </span>')

        fo.write('</div>\
            </body>\
            </html>')

        fo.close()

    # opens the input file gettisburg.txt
    f = open("gettisburg.txt", "r")
    print(f.read())
    f.close()

    # remember to open in in the correct mode
    # reads the file line by line
    f = open("gettisburg.txt", "r")
    for line in f:
        word = line.split()
        print(word)
    f.close()
    # creates the dictionary containing the word itself
    my_dict = {
    }

    
    # and how often it occurs in a sentence
    # makes a call to add_to_dict where the dictionary
    # is actually populated
    # returns a dictionary
    def create_dict(self):
        my_dict = {}
        # your code goes here:

        with open("gettisburg.txt", "r") as file:
            for line in file:

                for word in line.split():
                    if word in my_dict:
                        my_dict[word] = my_dict[word]
                    else:
                        my_dict[word] = 1

                        self.add_to_dict(word, my_dict)

                        print(my_dict)



    # helper function that is called from
    # create_dict
    # receives a word and a dictionary
    # does the counting of the key we are at and adds 1
    # if this word already exists. Otherwise sets the
    # word occurance counter to 1
    # returns a dictionary
    def add_to_dict(self, word_in_line, the_dict):
        # your code goes here

        i = 0

        for word_in_dict in the_dict:

            if i != len(the_dict) - 1:

                if word_in_line == word_in_dict:
                    the_dict[word_in_dict] = the_dict[word_in_dict] +1

                    i = i + 1

                    return the_dict


wc = WordCloud()
