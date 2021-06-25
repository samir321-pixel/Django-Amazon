from django.urls import reverse_lazy

from .models import User
from django.views.generic import ListView, CreateView
from django.views.decorators.csrf import csrf_protect


# Create your views here.

class IndexView(CreateView):
    model = User
    template_name = 'core/index.html'
    context_object_name = 'index'


# class SignalIDViewsets(PublicSignalIDViewSet):
#     serializer_class = PublicSignalSerializerDetail
#
#     def retrieve(self, request, id):
#         print("started working")
#         signal = Signal.objects.get(id=id) #self.kwargs["id"]
#         try:
#             jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#             jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
#             payload = jwt_payload_handler(request.user)
#             token = jwt_encode_handler(payload)
#             print(token)
#         except Exception as e:
#             print("Error occures", e)
#         data = PublicSignalSerializerDetail(signal, context=self.get_serializer_context()).data
#         return Response(data)

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import NameForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        url = "https://login.microsoftonline.com/d0db0b7e-ceac-44dc-8813-a89c1a10c5a6/oauth2/v2.0/token"
        data = {
            "code": "0.AYIAfgvb0KzO3ESIE6icGhDFplL8FtfPrR5Gn8RiWgL13xuCAAA.AQABAAIAAAD--DLA3VO7QrddgJg7Wevr8JFeEUMq1XJS3bB67YcJIT85HayzK0orMnErrFrFdq2EQhnYbmR_rG0umjImNAeqQVOPoekWRYz7q2xDLcpTjtYCkij_r13RoUAjYRLy3NueEHbjpAU9CLj5PO3fUN5QIE-r-BDgIhKd1oE2EGKSxjDEIiYbuoFP13mOgTH-4_qS1srIsoY1XLeFAVWFpd5DKOWxFcddM3R4L1K45ho5E-aldF8fCSxA9w_o9vJVn1f98rn5db0aLtsIjpPpDhpHD4gm4ZPS7bUq64mOH6HnUGwSeHLzRSGrem1QFOR9cKovUT4J3WUpuFT5mCBsn4A-0cfsxpjmgYf-fiwwlIWLdk4Rntazu49igqQyIGQvkUejwU3ozzdZIHDcnTXH9ejuZA_Di7LVFY_STiQ0uXz4eQ__ccX-zhZYB9yY_MEdHQdfd6AHkIXVmCOidiI3gWXyLTgZWP-kn8O5dvGVlMKduZ4mA9DBpDw0bdHkpjxNFi59TzQAn2FGFMP0kgEV297QuGNPxbTjd0koK92tf0iLkJ8j1VSo2Z7b6yv8QgcjLScTs1Iwikdkbo0XeP_4vBgYsOKhPc7sMosOEKsX6Rv6uMdrGrCvAoJFHOkbuIDxa76cppSX8AqqhVDS3APXuUahHDfiv39Lna_BMQ6ZyiJz99OiO8iJqCafkulAEclkDhMwGVVxuCopuFsPeVEnTzy6Z09_-V2_6qVI7yUi1gJfHurf8VeBnCHgWR8qIDwaMFsBPKT4JtzIPBcOLhAk3hPeIAA",
            "grant_type": "password",
            "username": username,
            "password": password,
            "client_id": "d716fc52-adcf-461e-9fc4-625a02f5df1b",
            "scope": "User.read",
            "client_secret": "-h5131XtDOoIlTtU28xIXz9s_~7Pda-M61"
        }
        import requests
        res = requests.post(url, data=data)
        print(res.json())
        print(res)
        data = res.json()
        token = data["access_token"]
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {}'.format(token)}
        url2 = "https://graph.microsoft.com/v1.0/me"
        res2 = requests.get(url2, headers=headers)
        print("this is second rresponse", res2.json())
        data2 = res2.json()
        azure_id = data2["id"]
        from django.core.exceptions import ObjectDoesNotExist
        try:
            query = User.objects.get(azure_id=azure_id)
        except ObjectDoesNotExist:
            user_query = User.objects.create_user(username=username,
                                                  email=username,
                                                  password=password,
                                                  azure_id=azure_id)
            print(user_query, "Created user")
        return redirect('/user')

    return render(request, 'core/index.html')
