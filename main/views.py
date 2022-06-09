from django.shortcuts import render
from .models import Sherlar, DramatikTarjima, LirikTarjima, EpikTarjima, Etyudlar, Hikoyalar, Lavhalar, Maqolalar
from django.views import generic
from django.db.models import Q
from django.views.generic import TemplateView


# Create your views here.
# search
def s(request):
    search_p = request.GET.get('search')
    try:

        if search_p:
            natijasher = Sherlar.objects.filter(Q(nom__icontains=search_p) | Q(matn__icontains=search_p))
            natijahikoya = Hikoyalar.objects.filter(Q(nom__icontains=search_p) | Q(matn__icontains=search_p))
            natijalavha = Lavhalar.objects.filter(Q(nom__icontains=search_p) | Q(matn__icontains=search_p))
            natijadtar = DramatikTarjima.objects.filter(Q(nom__icontains=search_p) | Q(matn__icontains=search_p))
            natijaetar = EpikTarjima.objects.filter(Q(nom__icontains=search_p) | Q(matn__icontains=search_p))
            natijaltar = LirikTarjima.objects.filter(Q(nom__icontains=search_p) | Q(matn__icontains=search_p))
            natijaetyud = Etyudlar.objects.filter(Q(nom__icontains=search_p) | Q(matn__icontains=search_p))
            natijamaqola = Maqolalar.objects.filter(Q(nom__icontains=search_p) | Q(matn__icontains=search_p))
            ########################################################################
            nsher = Sherlar.objects.all()
            nhikoya = Hikoyalar.objects.all()
            nlavha = Lavhalar.objects.all()
            ndtar = DramatikTarjima.objects.all()
            netar = EpikTarjima.objects.all()
            ntar = LirikTarjima.objects.all()
            netyud = Etyudlar.objects.all()
            nmaqola = Maqolalar.objects.all()
            DDD = [nsher, nhikoya, nlavha, ndtar, netar, ntar, netyud, nmaqola]
            DCH = []
            for i in DDD:
                k = 0
                for j in i:
                    k += j.matn.count(search_p)
                DCH.append(k)

            ########################################################################
        context = {'nsher': natijasher,
                   'nhikoya': natijahikoya,
                   'nlavha': natijalavha,
                   'ndt': natijadtar,
                   'net': natijaetar,
                   'nlt': natijaltar,
                   'netyud': natijaetyud,
                   'nmaqola': natijamaqola,
                   'x0': DCH[0],
                   'x1': DCH[1],
                   'x2': DCH[2],
                   'x3': DCH[3],
                   'x4': DCH[4],
                   'x5': DCH[5],
                   'x6': DCH[6],
                   'x7': DCH[7],
                   'sx': sum(DCH)
                   }
    except:

        context = {'nsher': "",
                   'nhikoya': "",
                   'nlavha': "",
                   'ndt': "",
                   'net': "",
                   'nlt': "",
                   'netyud': "",
                   'nmaqola': ""
                   }

    return render(request, 'search.html', context)


def index(request):
    return render(request, 'index.html')


# maqolalar
class MaqolaList(generic.ListView):
    queryset = Maqolalar.objects.filter(status=1).order_by('vaqt')
    template_name = 'maqolalar/maqolalist.html'


class MaqolaDetail(generic.DetailView):
    model = Maqolalar
    template_name = 'maqolalar/maqola.html'


# sherlar
class SherList(generic.ListView):
    queryset = Sherlar.objects.filter(status=1).order_by('vaqt')
    template_name = 'sherlar/sher_list.html'


class SherDetail(generic.DetailView):
    model = Sherlar
    template_name = 'sherlar/sher_detail.html'


# nasriy asarlar
class HikoyaList(generic.ListView):
    queryset = Hikoyalar.objects.filter(status=1).order_by('vaqt')
    template_name = 'nasriylar/hikoyalist.html'


class HikoyaDetail(generic.DetailView):
    model = Hikoyalar
    template_name = 'nasriylar/hikoya.html'


class LavhaList(generic.ListView):
    queryset = Lavhalar.objects.filter(status=1).order_by('vaqt')
    template_name = 'nasriylar/lavhalist.html'


class LavhaDetail(generic.DetailView):
    model = Lavhalar
    template_name = 'nasriylar/lavha.html'


class EtyudList(generic.ListView):
    queryset = Etyudlar.objects.filter(status=1).order_by('vaqt')
    template_name = 'nasriylar/etyudlist.html'


class EtyudDetail(generic.DetailView):
    model = Etyudlar
    template_name = 'nasriylar/etyud.html'


# tarjimalar
class EpikList(generic.ListView):
    queryset = EpikTarjima.objects.filter(status=1).order_by('vaqt')
    template_name = 'tarjimalar/Etarjimalar.html'


class EpikDetail(generic.DetailView):
    model = EpikTarjima
    template_name = 'tarjimalar/Etarjima.html'


class LirikList(generic.ListView):
    queryset = LirikTarjima.objects.filter(status=1).order_by('vaqt')
    template_name = 'tarjimalar/Ltarjimalar.html'


class LirikDetail(generic.DetailView):
    model = LirikTarjima
    template_name = 'tarjimalar/Ltarjima.html'


class DramaList(generic.ListView):
    queryset = DramatikTarjima.objects.filter(status=1).order_by('vaqt')
    template_name = 'tarjimalar/Dtarjimalar.html'


class DramaDetail(generic.DetailView):
    model = DramatikTarjima
    template_name = 'tarjimalar/Dtarjima.html'


class KitobPageView(TemplateView):
    template_name = 'kitob.html'


class SuratPageView(TemplateView):
    template_name = 'surat.html'


class MukofotPageView(TemplateView):
    template_name = 'mukofot.html'



