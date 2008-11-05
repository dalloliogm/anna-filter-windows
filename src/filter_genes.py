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
... 0		200		400		B3GALT1    San     4       1,00	# not included
... 200		400		600		B3GALT1    San     4       1,00	# not included
...	600		800		1000	B3GALT1    San     4       1,00	# should be Included!
...	1000	1200	1400	B3GALT1    San     4       1,00	# should be Included!
... 1400	1600	1800	B3GALT1    San     4       1,00	# should be Included!
... 1800	2000	2200	B3GALT1    San     4       1,00	# should be Included!
... 2200	2400	2600	B3GALT1    San     4       1,00	# not included
... ''')

>>> output_file = StringIO()

>>> output_file = filter_windows(sliding_windows_file, genes_file, output_file)
>>> print output_file.read()	#doctest: +NORMALIZE_WHITESPACE
#window_start, window_middle, window_end, gene_name
600		800		1000	B3GALT1
1000	1200	1400	B3GALT1
1400	1600	1800	B3GALT1
1800	2000	2200	B3GALT1
<BLANKLINE>

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
		line = line.strip()

		if line and not line.startswith('#'):		# if line is not empty and not a comment
			logging.debug(("line: %s" %line))
			fields = line.split()		# it is better to use the default splitting algorithm here.
										# read help(''.split)	

			gene_name = fields[0]
			logging.debug(("fields: %s" %fields))
			start = fields[2]
			end = fields[3].strip()		# remove \n\r, like chomp
			genes.append((gene_name, start, end))
			
#	logging.debug(("genes :", genes))		# print the contents of genes, if level=loggin.DEBUG

	# read sliding windows file, and select windows that fall in genes
	output = '#window_start, window_middle, window_end, gene_name\n'
	outputlineskeleton = "%s	%s	%s	%s\n"	# %(window_start, window_middle, window_end, gene_name)

	for line in sliding_windows_file:
		line = line.strip()		# remove trailing characters (like chomp)
		if line and not line.startswith('#'):
			window_fields = line.split()

#			logging.debug(window_fields)
			window_start = int(window_fields[0])
			window_end = int(window_fields[2])
			window_middle = int(window_fields[1])
			gene = window_fields[3]

			for gene in genes:
				gene_start = int(gene[1])
				gene_end = int(gene[2])
				gene_name = gene[0]
				# if window_start is comprised between gene_end and gene_start
				if gene_end >= window_start >= gene_start:
					logging.debug("This window starts inside gene %s (%s, %s)" %(gene[0], gene_start, gene_end))
					logging.debug(line)
					output +=  outputlineskeleton % (window_start, window_middle, window_end, gene_name)
				elif gene_end >= window_end >= gene_start:
					logging.debug("This window ends inside gene %s (%s, %s)" %(gene[0], gene_start, gene_end))
					logging.debug(line)
					output +=  outputlineskeleton % (window_start, window_middle, window_end, gene_name)
	
	logging.debug(output)
	output_file.write(output)
	output_file.seek(0)
	return output_file


def _test():
	"""Test the module"""
	import doctest
	doctest.testmod()

if __name__ == '__main__':
	logging.basicConfig(level = logging.DEBUG)
	main()
	_test()

