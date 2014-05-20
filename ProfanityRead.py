import urllib 

def read_text():
    quotes = open("/Users/jantsankhorloo/Documents/ProgramA.txt")
    contents_of_file = quotes.read()
    print (contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print "Profanity Alert!"
    elif "false" in output:
        print "This document has no bad words!"
    else:
        print "Could not scan the document!"
    
read_text()


#Additional useful information:
#https://docs.python.org/2/library/functions.html
#http://www.wdyl.com/profanity?q=shot
#http://en.wikipedia.org/wiki/Query_string
#https://docs.python.org/2/library/urllib.html
