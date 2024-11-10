#Playing with regular expressions
#Author: Aoife Flavin

#Anonymise the sub domains of ip addresses by
#Xing out the last two triplets, store new lines in another file.

import re

#regex = "\d{1,3}\.\d{1,3} " # this will find other numbers apart from ips

#make a group at the beginning to keep
regex = "(\d{1,3}\.\d{1,3}\.)\d{1,3}\.\d{1,3}"

replacement_text = "\\1XXX.XXX "
filename = "smaller_access.log"
output_filename = "anonimised IPs.txt"

with open(filename) as input_file:
    with open(output_filename, 'w') as output_file:
        for line in input_file:
            #debugging
            #found_text = re.search(regex, line).group()
            #print(found_text)
            new_line = re.sub(regex, replacement_text, line)
            output_file.write(new_line)