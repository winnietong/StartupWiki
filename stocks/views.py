from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from forms import *
from django.core.mail import EmailMultiAlternatives
from stockproject import settings
from django.core.mail import send_mail
from rauth import OAuth2Service



# Create your views here.
def home(request):
    facebook = OAuth2Service(
        client_id='440483442642551',
        client_secret='cd54f1ace848fa2a7ac89a31ed9c1b61',
        name='facebook',
        authorize_url='https://graph.facebook.com/oauth/authorize',
        access_token_url='https://graph.facebook.com/oauth/access_token',
        base_url='https://graph.facebook.com/'
    )

    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            text_content = 'Thank you for signing up for our website, {}'.format(user.username)
            html_content = '<h2>Hey {}, thanks for signing up!</h2> <div>I hope you enjoy using our site</div>'.format(user.username)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("/")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })


def category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CategoryForm()

    return render(request, "category.html", {
        'form': form,
    })

def view_category(request, category_name):
    companies = Company.objects.filter(category__name=category_name)

    return render(request, "view_category.html", {'companies': companies,
                                                  'category_name': category_name})

def companies(request):
    companies = Company.objects.all()
    return render(request, "company/companies.html", {'companies': companies})


@login_required
def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/companies/")
    else:
        form = CompanyForm()

    return render(request, "company/add_company.html", {
        'form': form,
    })


def view_company(request, company_name):
    company = Company.objects.get(name=company_name)
    comments = Comment.objects.filter(post__name=company_name)

    # Follow Form
    # To check that request.POST['follow'] exists you can do:
    # if 'follow' in request.POST
    if request.POST.get('follow'):
        follower = User.objects.get(username = request.user)
        follower.company.add(company)

    # Comment Form
    if request.POST.get('comment-field'):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/companies/{}".format(company_name))
    else:
        form = CommentForm(
            initial={'user': request.user,
                     'post': company}
        )

    return render(request, "company/view_company.html", {'company': company,
                                                         'form': form,
                                                         'comments': comments})

@login_required
def edit_company(request, company_name):
    company = Company.objects.get(name=company_name)
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            if form.save():
                return redirect("/companies/{}".format(company_name))
    else:
        form = CompanyForm(instance=company)
    data = {"company": company, "form": form}
    return render(request, "company/edit_company.html", data)

@login_required
def add_funding(request, company_name):
    company = Company.objects.get(name=company_name)
    if request.method == 'POST':
        form = FundingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/companies/{}".format(company_name))
    else:
        form = FundingForm(
            initial={'company': company.id}
        )

    return render(request, "add_funding.html", {
        'form': form, 'company': company
    })


@login_required
def profile(request):
    companies = Company.objects.filter(followers__username=request.user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("/profile/")
    else:
        form = UserForm(instance=request.user)
    return render(request, "profile.html", {'companies': companies, 'form': form})


def profile_username(request, profile_username):
    companies = Company.objects.filter(followers__username=profile_username)
    profile_user = User.objects.get(username=profile_username)
    return render(request, "profile_username.html", {'companies': companies, 'profile_user': profile_user})


def contact(request):
    if request.method == 'POST':
        message = request.POST.get('message','')
        email = request.POST.get('email', '')
        name = request.POST.get('name', '')
        if message and email:
            send_mail(
                'Contact from your Contact Us Page',
                '{} from {} at {}'.format(message, name, email),
                'winnie.rocketu@gmail.com',
                ['tong.winnie@gmail.com'],)

    return render(request, "contact.html")

