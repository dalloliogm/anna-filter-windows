#!/usr/bin/env python
"""
Retrieve sliding windows (from OUT_DAF_lower_filtrat.txt) falling in a gene (from Genes.txt)


Usage:

>>> from StringIO import StringIO		# This module is to create fake files,
...										# to be used for testing purposes.
...										# don't worry about it.
>>> genes_file = StringIO('''
... #Gene   Position        initial.pos     Final.pos
... B3GALT2 chr1    191414799       191422347
... B3GALT5 chr21   39850239        39956685
... B3GNT1  chr11   65869419        65871737
... B3GNT2  chr2    62276766        62305370
... B3GNT3  chr19   17766658        17785385
... B3GNT4  chr12   121254181       121258037
... B3GNT5  chr3    184453726       184473873
... ''')

>>> sliding_windows_file = StringIO(''' 
... # start	middle end	gene_name pop ...
... 64998701        65098701        65048701        FUT8    San     4       1,00
... 65118701        65218701        65168701        FUT8    San     5       1,00
... 64998701        65098701        65048701        FUT8    Japanese        6       1,00
... 64998701        65098701        65048701        FUT8    Han     5       1,00
... 64998701        65098701        65048701        FUT8    Pathan  9       1,00
... 64998701        65098701        65048701        FUT8    Pima    5       1,00
... 64998701        65098701        65048701        FUT8    Yakut   7       1,00
... 64998701        65098701        65048701        FUT8    Hazara  9       1,00
... ''')

>>> output_file = StringIO()

>>> filter_windows(sliding_windows_file, genes_file, output_file)
>>> print output_file.read()

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

	# Reads sliding windows file and create a list in the form
	# genes = [('gene1', 1000, 2000), ('gene2', 4000, 45000)]
	genes = []
	for line in genes_file:
		if not line.startswith('#'):
			fields = line.split('\t')
			gene_name = fields[0]
			start = fields[2]
			end = fields[3].strip()		# remove \n\r, like chomp
			genes.append((gene_name, start, end))
			
	logging.debug(genes)


def _test():
	"""Test the module"""
	import doctest
	doctest.testmod()

if __name__ == '__main__':
	logging.basicConfig(level = logging.DEBUG)
	main()
	_test()

