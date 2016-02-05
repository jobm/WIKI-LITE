# from django.conf import settings
# from django.core.mail import send_mail
# from django.shortcuts import render
# from .models import SignUp
#
# # Create your views here.
#
#
# def auth(request):
#     title = 'Sign Up Now'
#     form = SignUpForm(request.POST or None)
#     context = {
#         "title": title,
#         "form": form
#     }
#     if form.is_valid():
#         # form.save()
#         # print request.POST['email'] #not recommended
#         instance = form.save(commit=False)
#
#         full_name = form.cleaned_data.get("full_name")
#         if not full_name:
#             full_name = "New full name"
#         instance.full_name = full_name
#         # if not instance.full_name:
#         # 	instance.full_name = "Justin"
#         instance.save()
#         context = {
#             "title": "Thank you"
#         }
#
#     if request.user.is_authenticated() and request.user.is_staff:
#         # print(SignUp.objects.all())
#         # i = 1
#         # for instance in SignUp.objects.all():
#         # 	print(i)
#         # 	print(instance.full_name)
#         # 	i += 1
#
#         queryset = SignUp.objects.all().order_by(
#             '-timestamp')  # .filter(full_name__iexact="Justin")
#         # print(SignUp.objects.all().order_by('-timestamp').filter(full_name__iexact="Justin").count())
#         context = {
#             "queryset": queryset
#         }
#
#     return render(request, "home.html", context)
