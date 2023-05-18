from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import UserBioForm, UploadFileForm


def process_get_view(request: HttpRequest) -> HttpResponse:
    a = request.GET.get('a', '')
    b = request.GET.get('b', '')
    result = a + b

    context = {
        'a': a,
        'b': b,
        'result': result,
    }
    return render(request, 'requestdataapp/request-data-params.html', context=context)


def user_form(request: HttpRequest) -> HttpResponse:
    context = {
        'form': UserBioForm(),
    }
    return render(request, 'requestdataapp/user-bio-form.html', context=context)


def handle_file_upload(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = form.cleaned_data['file']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            file_size = fs.size(filename)
            if file_size > 1048576:
                fs.delete(filename)
                print('file deleted', filename)
                context = {
                    'title': 'Filesize error message',
                    'error_msg': 'Error! Filesize couldn`t be more than 1 Mb.',
                    'href_msg': 'Return to upload file page',
                }

                return render(request, 'requestdataapp/error-message.html', context=context)
            else:
                print('file saved', filename)
    else:
        form = UploadFileForm()

    context = {
        'form': form,
    }

    return render(request, 'requestdataapp/file_upload.html', context=context)
