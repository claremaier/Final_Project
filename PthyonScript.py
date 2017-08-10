#Python Script to clean this up

#strip the punctuation and extra information from text document

#import re module
import re

#Open the text file with the ocr
ocr = open('83471_1897-01-07.txt')
#read the text file into a list
Text = ocr.readlines()

#Create an empty list to fill with lines of corrected text
CleanText = []

# checks each line in the imported text file for all the following patterns
for line in Text:
    #lines with multi-dashes contain data - searches for those lines
    # -- does not isolate intro text lines with one dash.
    dashes = re.search('(--+)', line)

    #isolates lines with dashes and cleans
    if dashes:
        #replaces dashes with my chosen delimiter
        nodash = re.sub('.(-+)', ',', line)
        #strikes multiple periods
        nodots = re.sub('.(\.\.+)', '', nodash)
        #strikes extra spaces
        nospaces = re.sub('(  +)', ',', nodots)
        #strikes *
        nostar = re.sub('.[*]', '', nospaces)
        #strikes new line and comma at the beginning of the line
        flushleft = re.sub('^\W', '', nostar)
        #getting rid of double commas (i.e. - Evarts)
        comma = re.sub(',{2,3}', ',', flushleft)
        #cleaning up some words that are stuck together (i.e. -  Dawes, Manderson)
        #skips double OO that was put in place of 00 in address
        caps = re.sub('[A-N|P-Z]{2,}', ',', comma)
        #Clean up NE and NW quadrant indicators by removing periods
        ne = re.sub('(\,*? N\. ?E.)', ' NE', caps)
        nw = re.sub('(\,*? N\. ?W[\.\,]*?_?)$', ' NW', ne) #MAKE VERBOSE
        #Replace periods with commas between last and first names (i.e. - Chace, Cockrell)
        match = re.search('^([A-Z][a-z]+\. )', nw) #MAKE VERBOSE
        if match:
            names = re.sub('\.', ',', nw)
        else:
            names = nw
           #Append each line to CleanText list while it loops through
        CleanText.append(names)

#Saving into a 'fake' csv file
fakecsv = open('fakecsv.csv', 'w')
#Write each line in CleanText to a file
for line in CleanText:
    fakecsv.write(line)


