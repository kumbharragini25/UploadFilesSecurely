from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from users.models import Users
from owner.models import Owner
from manager.models import Managers
from django.conf import settings
from django.contrib.auth import authenticate, login
from authentication.forms import Authforms
from .utils import encrypt_file
import tempfile
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from UploadedEncryptedDocument.models import UploadedEncryptedDocument
from django.shortcuts import render, redirect
from upload.forms import DocumentUploadForm
from upload.models import UploadedDocument
from django.contrib.auth.backends import ModelBackend

from authentication.backendss import CustomAuthBackend

from django.contrib.auth.models import Group, User


def sin(request):
    return render(request,'authentication/signin.html')

def show_group(request,document_id):
    
    users= users = User.objects.all()
    return render(request, 'authentication/group.html',{'users': users,'document_id':document_id}) 




def create_group_for_document(request, document_id):
    document = get_object_or_404(UploadedDocument, pk=document_id)
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        user_ids = request.POST.getlist('users')
        access_level = request.POST.get('access_level')
        
       
        group = Group.objects.create(name=group_name)
        
        
        cnt=0
        for user_id in user_ids:
            user = User.objects.get(id=user_id)
            group.user_set.add(user)
            cnt=cnt+1
        print(cnt)
        
        document.shared_with_group = group
        document.access_level = access_level 
        document.save()
        
        return HttpResponse("Group created successfully",cnt)
    else:
        users = User.objects.all()
        return render(request, 'authentication/group.html', {'users': users})



def home(request):
    return HttpResponse("hello")



def permission(request):
    return render(request, 'authentication/permition.html') 




def upload_document(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            file = form.cleaned_data['file']
            owner = request.user 
            
            UploadedDocument.objects.create(name=name, file=file, owner=owner)
            messages.success(request,"Uploaded successfully")
             
    else:
        form = DocumentUploadForm()
    return render(request, 'authentication/upload_files.html', {'form': form})





def show(request,document_id):
   users= users = User.objects.all()
   return render(request, 'authentication/shareuser.html',{'users': users,'document_id':document_id}) 




def forms(request):

    fn=Authforms()
    return render(request,'authentication/signup.html',{'form':fn})




def signup(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        password2 = request.POST.get('Password2')
        role = request.POST.get('class1')
        my_user=User.objects.create_user(username=username,email=email,password=password)
        my_user.role=role
        my_user.first_name=username
        my_user.save()

        if(role=='1'):
            user1=Owner(Username=username,Email=email,Password=password,Confirm_password=password2,Role=role)
            user1.save()
        elif(role=='2'):
            user2=Managers(Username=username,Email=email,Password=password,Confirm_password=password2,Role=role)
            user2.save()
        elif(role=='3'):
            user3=Users(Username=username,Email=email,Password=password,Confirm_password=password2,Role=role)
            user3.save()    
            
        
        messages.success(request,"Your account is created successfully")   
  
        
        return redirect('signin')

    return HttpResponse("Signup successful. Redirect to a success page.")

   
    return HttpResponse()



@login_required
def view_uploaded_files(request):
    
    uploaded_documents = UploadedDocument.objects.filter(owner=request.user)
    messages.success(request,"Your Uploaded files......")
    return render(request, 'authentication/view_uploaded_files.html', {'uploaded_documents': uploaded_documents})




@login_required
def share_document_with_user(request, document_id):
    document = get_object_or_404(UploadedDocument, pk=document_id)
    user_id = request.POST.get('user')
    access_level = request.POST.get('access_level')
    user = get_object_or_404(User, pk=user_id)

   
    document.shared_with_user = user
    document.access_level = access_level 
    

    document.save()
    return HttpResponse("Saved")



@login_required
def view_all_files(request):
   
    uploaded_documents = UploadedDocument.objects.all()
    messages.success(request,"All organization files")
    return render(request, 'authentication/allfiles.html', {'uploaded_documents': uploaded_documents})




def signin(request):
    if request.method == 'POST':
        username = request.POST.get("Username")
        password = request.POST.get("Password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.error(request, "Sign in successufully") 
            return render(request, 'authentication/upload_files.html')  
        else:
           
            messages.error(request, "Bad credential")    
            return render(request, 'authentication/signin.html', {'error_message': 'Invalid credentials'})
           
    return render(request, 'authentication/signin.html')


    

@login_required
def view_uploaded_documents(request):
    documents = UploadedDocument.objects.filter(owner=request.user)
    return render(request, 'authentication/view_uploaded_documents.html', {'documents': documents})




@login_required
@login_required
def edit_document(request, document_id):
    document = get_object_or_404(UploadedDocument, pk=document_id)
    
   
    if request.user == document.owner or check_document_access(request, document,'edit'):
        return render(request, 'authentication/edit_document.html', {'document': document})
        document.save()
        return HttpResponse("Edit Document View")
    else:
         return HttpResponse("You are not authorized to delete this document") 
        

 




@login_required
def delete_document(request, document_id):
    document = get_object_or_404(UploadedDocument, pk=document_id)
    
   
    if request.user == document.owner or check_document_access(request, document,'delete'):
       
        file_path = document.file.path  
        document.file.delete(save=False)
    
    
        document.delete()
       
        return HttpResponse("Deleted successfully")    
    else:
        
       return HttpResponse("You are not authorized to delete this document")    

    






def check_document_access(request, document,required_access):
    if document.shared_with_user == request.user or (document.shared_with_group and request.user.groups.filter(pk=document.shared_with_group.pk).exists()):
        if document.access_level == 'delete' and required_access == 'delete':
            return True
        elif document.access_level == 'edit' and request.method in ['GET', 'POST'] and required_access == 'edit':
            return True
        elif document.access_level == 'download' and request.method == 'GET' and required_access == 'download':
            return True
    return False





@login_required
def download_document(request, document_id):
    
    document = get_object_or_404(UploadedDocument, pk=document_id)
    
    
    if request.user == document.owner or check_document_access(request, document,'download'):
        return render(request, 'authentication/download.html', {'document': document})
        
        messages.success(request, "Downloaded successfully")
    else:
        
        return HttpResponse("You are not authorized to download this document")    

     
    






@login_required
def authenticate_and_edit_document(request, document_id):
    if request.method == 'POST':
       
        username = request.POST.get("Username")
        password = request.POST.get("Password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
           
            return redirect('edit_document', document_id=document_id)
        else:
            
            return HttpResponse("Authentication failed")

   
    return render(request, 'authentication/signin.html')    