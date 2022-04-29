from zefir_mall_app.models import infocenter, navbar
def header_and_footer(request):
    context = {}
    infocenter_queryset = infocenter.objects.all()
    navbar_queryset = navbar.objects.all()
    context['infocenter_queryset'] = infocenter_queryset
    context['navbar_queryset'] = navbar_queryset

    return context