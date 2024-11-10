# Practising using some RexEx
# Author: Aoife Flavin

# find some text in an access file

import re

regex = "\[.*\]"
filename = "smaller_access.log"

with open (filename) as input_file:
    for line in input_file:
        found_text_list = re.findall(regex, line)
        if (len(found_text_list)!=0):
            #print found_text_list
            found_text = found_text_list[0]
           # print(found_text)
           #if I don't want the [] in it
            print(found_text[1:-1])
