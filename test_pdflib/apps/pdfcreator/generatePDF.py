import os
from datetime import datetime
from python33.pdflib_py import *

def PDF_Generate(cause_number, court_number,county, your_name, spuse_name, childs):
    p = PDF_new()
    font = PDF_load_font(p, "Helvetica", "host", "")
    font_bold = PDF_load_font(p, "Helvetica-Bold", "host", "")

    PDF_set_info(p, "Author", "Khriapa Artem")
    PDF_set_info(p, "Title", "Test case")
    PDF_begin_document(p, '', '')
    PDF_begin_page(p, 595, 841)

    PDF_setfont(p, font, 12.0)

    PDF_set_text_pos(p, 50, 770)
    PDF_continue_text(p, 'NOTICE: THIS DOCUMENT CONTAINS SENSITIVE DATA.')
    PDF_continue_text(p, '')
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

    childs_string = ''
    for i in childs:
        ch = str(childs.index(i)+1)+'.'+i+"   "
        childs_string = childs_string + ch
    print(childs_string)

    tf = PDF_create_textflow(p, childs_string ,"fontname=Helvetica fontsize=14 encoding=unicode leading=120% alignment=justify")
    PDF_fit_textflow(p, tf, 50, 580, 545, 500, '')

    PDF_set_text_pos(p, 350, 700)
    PDF_setfont(p, font, 11.0)
    PDF_continue_text(p, ('in the court:   %s' % court_number))
    PDF_continue_text(p, '')
    PDF_continue_text(p, '')
    PDF_continue_text(p, ('%s,   County, Texas' % county))

    PDF_end_page(p)
    PDF_end_document(p,'');
    bufered_doc = PDF_get_buffer(p)
    PDF_delete(p)

    print('PDF created!')

    return bufered_doc
