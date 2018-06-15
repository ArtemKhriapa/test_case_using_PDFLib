from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from apps.pdfcreator.models import Answer
from apps.pdfcreator.generatePDF import Exsample_PDF_Generate

cause_number ='123' # i d'nt know? what or who make it, random now
court_number = '321' # the same

def view(request):

    #cause_number,court_number,county, your_name, spuse_name, childs

    if 'user_id' in  request.GET:
        if request.GET.dict()['user_id'].isdigit():

            user = User.objects.get(id=request.GET.dict()['user_id'])
            for i in user.answers.all():
                print ('question:', i.question_name,' answer:', i.value)

                #Exsample_PDF_Generate(cause_number, court_number,county, your_name, spuse_name, childs)
            print('Create pdf in here')
            responce = 'Your looking for user with id: ' + request.GET.dict()['user_id']
            return HttpResponse(responce)
        else:
            return HttpResponse('Enter correct user ID. I do not know who to look for (enter after the address ?user_id=* where * is ID user in youd DB)')
    else:
        return HttpResponse('I do not know who to look for (enter after the address ?user_id=* where * is ID user in youd DB)')
