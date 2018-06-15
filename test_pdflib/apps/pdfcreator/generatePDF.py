# from sys import *
from python33.pdflib_py import *
# from PDFlib.PDFlib import PDFlib as P
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

# 1 pt = 1/72 inch = 25.4/72 mm = 0.3528 mm
# from PDFlib.pdflib_py import *

# cause_number = '123456'
# court_number = '654321'
# county = 'Some county'
# your_name= 'Bill Clinton'
# spuse_name='Monica Levinski'
# childs = ['Barack Obama', 'Donald Trump', 'Jorge Bush jr']

def Exsample_PDF_Generate(cause_number, court_number,county, your_name, spuse_name, childs):
    p = PDF_new()
    font = PDF_load_font(p, "Helvetica", "host", "")
    font_bold = PDF_load_font(p, "Helvetica-Bold", "host", "")


    if PDF_open_file(p, "pdf/hello_py222.pdf") == -1:
        print("Couldn't open PDF file 'hello_py.pdf'\n")

    PDF_set_info(p, "Author", "Khriapa Artem")
    PDF_set_info(p, "Title", "Test case")
    PDF_begin_page(p, 595, 841)

    PDF_setfont(p, font, 12.0)

    PDF_set_text_pos(p, 50, 770)
    PDF_continue_text(p, 'NOTICE: THIS DOCUMENT CONTAINS SENSITIVE DATA.')
    PDF_continue_text(p, ('                                       Cause number:  %s' % cause_number))
    PDF_continue_text(p, '')
    PDF_setfont(p, font_bold, 12.0)
    PDF_continue_text(p, 'IN THE MATTER IN MARRIAGE OF')
    PDF_continue_text(p, '')
    PDF_setfont(p, font_bold, 11.0)
    PDF_continue_text(p, ("Petitioner:       %s" % your_name))
    PDF_continue_text(p, '')
    PDF_setfont(p, font, 11.0)
    PDF_continue_text(p, '                         and')
    PDF_continue_text(p, '')
    PDF_setfont(p, font_bold, 11.0)
    PDF_continue_text(p, ('Respondent:   %s' % spuse_name))
    PDF_continue_text(p, '')
    PDF_continue_text(p, '')
    PDF_continue_text(p, '')
    PDF_continue_text(p, 'AND IN THE INTEREST OF :')
    PDF_continue_text(p, '')
    PDF_setfont(p, font, 11.0)

    for i in childs:
        PDF_continue_text(p, ('%s. %s' % (str(childs.index(i)+1), i)))

    PDF_set_text_pos(p, 350, 700)
    PDF_setfont(p, font, 11.0)
    PDF_continue_text(p, ('in the court:   %s' % court_number))
    PDF_continue_text(p, '')
    PDF_continue_text(p, '')
    PDF_continue_text(p, ('%s,   County, Texas' % county))

    PDF_end_page(p)
    PDF_close(p)
    PDF_delete(p)

    print('PDF created!')


# Exsample_PDF_Generate()


    # cause_number = '111',
    # court_number='999',
    # county='far-far-away',
    # your_name='Arnold Swarzenegger',
    # spuse_name='Van Damm',
    # childs=['Bruce Li', 'Silvester Stallone']
