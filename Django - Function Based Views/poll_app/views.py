from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib import messages

from .forms import RegisterModelForm, LoginModelForm, PersonalInfoForm, UserImageForm, EditInformationForm, ChartForm
from .models import Question, Survay, Personal, UserImage, ChartModel, MessageModel
from .my import DefineField, ReturnChartData

# Create your views here.

# ======================================== INDEX SECTION ==================================== #


def index_page(request):
    return HttpResponseRedirect(reverse("login-user"))

# ====================================== LOGGED IN SECTION ==================================== #


@login_required
def personal_page(request):
    warned_users = []
    warning_messages = MessageModel.objects.all()
    if warning_messages is not None:
        warned_users = [warned_user.user_name for warned_user in warning_messages]

    present_user = request.user
    if request.method == "POST":
        if "hidden_personal_info" in request.POST:
            form = PersonalInfoForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("personal-page"))

        if "hidden_image_file" in request.POST:
            current_user = UserImage.objects.filter(user=present_user).first()
            form = UserImageForm(
                request.POST, request.FILES, instance=current_user)
            if form.is_valid():
                form.save()
                messages.success(request, "Image has been changed!")
                return HttpResponseRedirect(reverse("personal-page"))

        if "hidden_poll" in request.POST:
            all_questions = Question.objects.all()
            for my_question in all_questions:
                if my_question.slug_title == request.POST.get(str(my_question.slug_title)):
                    survey_result = Survay(
                        question=my_question,
                        answer=request.POST.get(str(my_question.slug_name)),
                        user=present_user
                    )
                    survey_result.save()
                    if present_user.username in warned_users:
                        return HttpResponseRedirect(reverse("delete-warned-user", kwargs={"user_name": present_user.username}))
                    return HttpResponseRedirect(reverse("personal-page"))
            

        if "hidden_chart" in request.POST:
            chart_form = ChartForm(request.POST)
            if chart_form.is_valid():
                chart_record = ChartModel.objects.get(id=1)
                chart_record.current_type = chart_form.cleaned_data["charts"]
                chart_record.save()
                return HttpResponseRedirect(reverse("personal-page"))

    form_info = PersonalInfoForm()
    form_image = UserImageForm()
    chart_form = ChartForm()

    all_images = UserImage.objects.all()
    user_image = all_images.filter(user=present_user).first()
    personal_info = Personal.objects.filter(user=present_user).first()
    all_users = User.objects.filter(is_superuser=0).all()
    survey_data = Survay.objects.all()
    survay_participants = [my_user.user.username for my_user in survey_data]
    survey_submitted = [item.user.username for item in survey_data]
    chart_record = ChartModel.objects.get(id=1)
    poll_questions = Question.objects.all()

    chart_tool = ReturnChartData()
    answer_occurence = Survay.objects.values("answer").annotate(
        count=Count("answer")).order_by("answer")
    my_result = chart_tool.get_chart_data(
        poll_questions=poll_questions, occurences=answer_occurence)

    return render(request, "poll/personal.html", {
        "form_info": form_info,
        "form_image": form_image,
        "user": present_user,
        "about": personal_info,
        "user_image": user_image,
        "poll": poll_questions,
        "survey_submitted": list(set(survey_submitted)),
        "all_users": all_users,
        "all_images": all_images,
        "my_result": my_result,
        "chart_form": chart_form,
        "chart_type": chart_record.current_type,
        "survay_participants": list(set(survay_participants)),
        "warned_users": warned_users
    })


# ====================================== CRUD OPERATIONS ==================================== #
@login_required
def edit_information(request, about):
    present_user = request.user
    if request.method == "POST":
        form = EditInformationForm(request.POST)
        if form.is_valid():
            record = Personal.objects.filter(user=present_user).first()
            chosen_field = request.POST.get("edit_input")

            if chosen_field == "work":
                record.work = form.cleaned_data["item"]
            elif chosen_field == "university":
                record.university = form.cleaned_data["item"]
            elif chosen_field == "city":
                record.city = form.cleaned_data["item"]
            elif chosen_field == "country":
                record.country = form.cleaned_data["item"]
            elif chosen_field == "love":
                record.love = form.cleaned_data["item"]
            elif chosen_field == "phone":
                record.phone = form.cleaned_data["item"]
            record.save()

            return HttpResponseRedirect(reverse("personal-page"))

    form = EditInformationForm()
    tool = DefineField()
    field_name = tool.get_field_name(about_name=about)

    return render(request, "poll/edit.html", {
        "form": form,
        "about": about,
        "field_name": field_name
    })


@login_required
def delete_user(request, user_id):
    chosen_user = User.objects.get(id=user_id)
    chosen_user.delete()
    return HttpResponseRedirect(reverse("personal-page"))


# ==================================== MESSAGE SECTION ================================== #
@login_required
def message_page(request, user_id):
    chosen_user = User.objects.get(id=user_id)
    my_messages = MessageModel(
        user_name=chosen_user.username
    )
    my_messages.save()
    messages.warning(request, "Warning Has Been Sent to User!")
    return HttpResponseRedirect(reverse("personal-page"))


@login_required
def delete_warned_user(request, user_name):
    chosen_user = MessageModel.objects.get(user_name=user_name)
    chosen_user.delete()
    return HttpResponseRedirect(reverse("personal-page"))


# ==================================== AUTHENTICATION SECTION ================================== #
def register_user(request):
    if request.method == "POST":
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            form.save()
            current_user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"]
            )
            login(request, current_user)
            return HttpResponseRedirect(reverse("personal-page"))
    else:
        form = RegisterModelForm()
    return render(request, "poll/register.html", {
        "form": form
    })


def login_user(request):
    if request.method == "POST":
        form = LoginModelForm(request, data=request.POST)
        if form.is_valid():
            current_user = form.get_user()
            if current_user is not None:
                login(request, current_user)
                return HttpResponseRedirect(reverse("personal-page"))
        else:
            print("it wass me")
    else:
        form = LoginModelForm()
    return render(request, "poll/login.html", {
        "form": form
    })


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("login-user"))
