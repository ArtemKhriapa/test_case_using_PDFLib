import os
from datetime import datetime
from python33.pdflib_py import *

def PDF_Generate(cause_number, court_number,county, your_name, spuse_name, childs):
    dt= str(datetime.now())
    p = PDF_new()
    font = PDF_load_font(p, "Helvetica", "host", "")
    font_bold = PDF_load_font(p, "Helvetica-Bold", "host", "")

    if PDF_open_file(p,"pdf/"+your_name+"_"+dt+".pdf") == -1:
        print("Couldn't open PDF file 'pdf/"+your_name+"_"+dt+".pdf'\n")
    # else:
    PDF_set_info(p, "Author", "Khriapa Artem")
    PDF_set_info(p, "Title", "Test case")
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

    return your_name+"_"+dt+".pdf"

cause_number = '111'
court_number='999'
county='far-far-away'
your_name="ArnoldSwarzenegger"
spuse_name='Van Damm'
childs=['Bruce Li', 'Silvester Stallone']



# PDF_Generate(cause_number, court_number,county, your_name, spuse_name, childs)
