#!/usr/bin/env python
"""
Retrieve sliding windows (from OUT_DAF_lower_filtrat.txt) falling in a gene (from Genes.txt)



>>> import StringIO		# don't worry about this. This is just to create an example
>>> sliding_windows_file = StringIO(''' 
... #Gene   Position        initial.pos     Final.pos
... B3GALT2 chr1    191414799       191422347
... B3GALT5 chr21   39850239        39956685
... B3GNT1  chr11   65869419        65871737
... B3GNT2  chr2    62276766        62305370
... B3GNT3  chr19   17766658        17785385
... B3GNT4  chr12   121254181       121258037
... B3GNT5  chr3    184453726       184473873
... '''

>>> genes_file = StringIO('''
... 64998701        65098701        65048701        FUT8    San     4       1,00
... 65118701        65218701        65168701        FUT8    San     5       1,00
... 64998701        65098701        65048701        FUT8    Japanese        6       1,00
... 64998701        65098701        65048701        FUT8    Han     5       1,00
... 64998701        65098701        65048701        FUT8    Pathan  9       1,00
... 64998701        65098701        65048701        FUT8    Pima    5       1,00
... 64998701        65098701        65048701        FUT8    Yakut   7       1,00
... 64998701        65098701        65048701        FUT8    Hazara  9       1,00
'''
"""
