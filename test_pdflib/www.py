from sys import *
from python33.pdflib_py import *
# from PDFlib.PDFlib import PDFlib as p
# p =  PDF_open_pdi_document('example.pdf' )
#
# text = 'adsadafaf'
#
#
# try:
#     p.open_file(p, filename='example.pdf')
#
#     print('here')
# except Exception as e:
#     print(e)


# from PDFlib.pdflib_py import *

p = PDF_new()
# p = PDF_open_file(p, "pdf/hello_py222.pdf")
if PDF_open_file(p, "pdf/hello_py222.pdf") == -1:

    print ("Couldn't open PDF file 'hello_py.pdf'\n")

print (dir(p))
PDF_set_info(p, "Author", "ME")
# PDF_set_info(p, "Creator", "hello.py")
PDF_set_info(p, "Title", "Hello world (Python - edit)")
PDF_begin_page(p, 595, 842)
font = PDF_load_font(p, "Helvetica-Bold", "host", "")
PDF_setfont(p, font, 18.0)
PDF_set_text_pos(p, 50, 700)
PDF_show(p, "Hello world!")
PDF_continue_text(p, "(says all in Python)")
# PDF_set_text_pos(p, 50, 900)
PDF_setfont(p, font, 26.0)
PDF_continue_text(p, "---Hello world!---")
PDF_end_page(p)
PDF_close(p)
PDF_delete(p)
print('wtf')