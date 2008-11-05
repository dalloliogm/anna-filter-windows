#!/usr/bin/env python
"""
Retrieve sliding windows (from OUT_DAF_lower_filtrat.txt) falling in a gene (from Genes.txt)


Usage:

>>> from StringIO import StringIO		# This module is to create fake files,
...										# to be used for testing purposes.
...										# don't worry about it.
>>> genes_file = StringIO('''
... #Gene   Position        initial.pos     Final.pos
... B3GALT1 chr1    1000	2000
... B3GALT2  chr1    4000	5000
... ''')

>>> sliding_windows_file = StringIO(''' 
... # start	middle end	gene_name pop ...
... 0		200		400		FUT8    San     4       1,00	# not included
... 200		400		600		FUT8    San     4       1,00	# ""
...	600		800		1000	FUT8    San     4       1,00	# should be Included!
...	1000	1200	1400	FUT8    San     4       1,00	# ""
... 1400	1600	1800	FUT8    San     4       1,00	# ""
... 1800	2000	2200	FUT8    San     4       1,00	# ""
... 2200	2400	2600	FUT8    San     4       1,00	# not included
... ''')

>>> output_file = StringIO()

>>> filter_windows(sliding_windows_file, genes_file, output_file)
>>> print output_file.read()	# this is the expected output # doctest: +NORMALIZE_WHITESPACE
600		800		1000	FUT8
1000	1200	1400	FUT8 
1400	1600	1800	FUT8
1800	2000	2200	FUT8


"""

import logging 	# module used only to debug

sliding_windows_file_path = '../data/OUT_DAF_lower_filtrat.txt'
genes_file_path = '../data/Genes.txt'
output_file_path = '../results/filtered_windows.txt'


def main():
	"""
	Open file handlers and launch filter_windows function.
	"""
	sliding_windows_file = file(sliding_windows_file_path, 'r')
	genes_file = file(genes_file_path, 'r')
	output_file = file(output_file_path, 'w')

	filter_windows(sliding_windows_file, genes_file, output_file)
	

def filter_windows(sliding_windows_file, genes_file, output_file):
	"""
	Given the two input files and the outputfile handlers, it filters the sliding windows
	that fall in a gene
	"""

	# Read sliding windows file and create a list in the form
	#  genes = [('gene1', 1000, 2000), ('gene2', 4000, 45000)]
	genes = []		# this could be a dictionary but I prefer not
	for line in genes_file:
		print "line: ", line
		if not line.startswith('#') or not line:
			fields = line.split('\t')	

			gene_name = fields[0]
			print fields
			start = fields[2]
			end = fields[3].strip()		# remove \n\r, like chomp
			genes.append((gene_name, start, end))
			
	logging.debug(genes)		# print the contents of genes, if level=loggin.DEBUG

	# read sliding windows file, and select windows that fall in genes
	for line in sliding_windows_file:
		window_fields = line.split()

		logging.debug(window_fields)
		start = window_fields[0]
		end = window_fields[2]
		gene = window_fields[3]

		for gene in genes:
			print start, end, gene[1], gene[2]


def _test():
	"""Test the module"""
	import doctest
	doctest.testmod()

if __name__ == '__main__':
	logging.basicConfig(level = logging.DEBUG)
#	main()
	_test()

