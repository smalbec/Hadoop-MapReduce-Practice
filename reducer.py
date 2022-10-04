#!/usr/bin/env python

import sys

current_fauthor = None
current_authors = []
fauthor = ''


for line in sys.stdin:
     
    #print 'new loop'

    # remove leading and trailing whitespaces
    line = line.strip()
    # parse the input we got from mapper.py
    if ',' not in line:
	print line
	continue
    else:
	fauthor, author = line.split(',\t')

	

    if current_fauthor == fauthor:
        current_authors.append(author.encode("utf-8"))
    else:
        if current_fauthor:
            print '<%s,%s>' % (current_fauthor.encode('ascii', 'ignore').decode('ascii'), current_authors)
	    current_authors = []
	    current_authors.append(author.encode("utf-8"))	
	else:
	    current_authors.append(author.encode("utf-8"))
        current_fauthor = fauthor
	

if current_fauthor == fauthor:
    print '<%s,%s>' % (current_fauthor.encode('ascii', 'ignore').decode('ascii'), current_authors)