#!/usr/bin/env python
import sys
import urllib
import feedparser

feedparser._FeedParserMixin.namespaces['http://a9.com/-/spec/opensearch/1.1/'] = 'opensearch'
feedparser._FeedParserMixin.namespaces['http://arxiv.org/schemas/atom'] = 'arxiv'

apicall = ''

for line in sys.stdin:
    apicall = line

response = urllib.urlopen(apicall).read()

feed = feedparser.parse(response)

# Run through each entry, and print out information
for entry in feed.entries:

    author_string = entry.author

    output = []

    for author in entry.authors:
        if len(entry.authors) == 1:
		print author_string.encode("utf-8")
	elif author.name != author_string and len(entry.authors) != 1:
		print '%s,\t%s' % (author_string.encode('ascii', 'ignore').decode('ascii'), (author.name).encode('ascii', 'ignore').decode('ascii'))