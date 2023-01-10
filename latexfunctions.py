from pdflatex import PDFLaTeX

import os

def latex_to_pdf(filename):
    pdfl = PDFLaTeX.from_texfile(os.getcwd()+'/dump/'+filename)
    pdfl.create_pdf(keep_pdf_file=True,keep_log_file=False)

#latex_to_pdf("Algebra Linear Inequality Easy 1.tex")