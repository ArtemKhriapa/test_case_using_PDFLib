from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from apps.pdfcreator.models import Answer
from apps.pdfcreator.generatePDF import PDF_Generate

def view(request):
    if 'user_id' in  request.GET:
        if request.GET.dict()['user_id'].isdigit():
            # your_name = Answer.objects.get(user=request.GET.dict()['user_id'], question_name ='your_name').value
            # spuse_name = Answer.objects.get(user=request.GET.dict()['user_id'], question_name ='spuse_name').value
            # county= Answer.objects.get(user=request.GET.dict()['user_id'], question_name ='county').value
            # court_number= Answer.objects.get(user=request.GET.dict()['user_id'], question_name='court_number').value
            # cause_number= Answer.objects.get(user=request.GET.dict()['user_id'], question_name='cause_number').value
            # childs = []
            # childs_list = Answer.objects.filter(user=request.GET.dict()['user_id'], question_name='child')
            # for child in childs_list:
            #     childs.append(child.value)
            """enother variant"""
            answers         = Answer.objects.filter(user=request.GET.dict()['user_id'])
            your_name       = answers.get(question_name='your_name').value
            spuse_name      = answers.get(question_name='spuse_name').value
            county          = answers.get(question_name='county').value
            court_number    = answers.get(question_name='court_number').value
            cause_number    = answers.get(question_name='cause_number').value
            childs          = [child.value for child in answers.filter(question_name='child')]
            filepath = "pdf/"+PDF_Generate(cause_number, court_number,county, your_name, spuse_name, childs)
            fsock = open(filepath,"rb")
            response = HttpResponse(fsock, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s.pdf' % your_name
            return response
        else:
            return HttpResponse('Enter correct user ID. I do not know who to look for (enter after the address ?user_id=* where * is ID user in youd DB)')
    else:
        return HttpResponse('I do not know who to look for (enter after the address ?user_id=* where * is ID user in youd DB)')
