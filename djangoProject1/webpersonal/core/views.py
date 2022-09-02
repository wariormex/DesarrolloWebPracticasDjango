from django.shortcuts import render, HttpResponse

def home(request):
    # return HttpResponse(
    #     """
    #        <h1>Mi pagina</h1>
    #        <p>Esto es un mensaje de prueba</p>
    #     """
        
    # )
    return render(request,'core/home.html')
