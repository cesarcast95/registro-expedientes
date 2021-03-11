from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Expediente
from .forms import ExpedienteForm, ExpedienteUpdateForm
from django.contrib.admin.views.decorators import staff_member_required
# Este metodo es para decorar nuestras clases
from django.utils.decorators import method_decorator
# Aqui para realizar la busqueda

from django.db.models import Q
from django.shortcuts import render_to_response


from .models import Expediente


from django.urls import reverse_lazy

# Create your views here.


class StaffRequiredMixin(object):

    # esto es un mixxin
    """
    Este mixin requerira que el usuario sea miembro del satff
    """
    # coneste decorator nos aseguramos q no puedan crear contenido sino son staf
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class RegistroListView(ListView):
    model = Expediente
    paginate_by = 25
    ordering = ['-updated']



class RegistroDetailView(DetailView):
    model = Expediente


@method_decorator(staff_member_required, name='dispatch')
class RegistroCreated(CreateView):
    model = Expediente
    form_class = ExpedienteForm
    success_url = reverse_lazy('registry:registry')


@method_decorator(staff_member_required, name='dispatch')
class RegistroUpdate(UpdateView):
    model = Expediente
    form_class = ExpedienteUpdateForm
    template_name_suffix = '_update_form'

    # redefinimos este metodo, para que despues de actualizar, nos
    # redirija al objecto que actualizamos y no a otro diferente
    def get_success_url(self):
        return reverse_lazy('registry:update', args=[self.object.id]) + '?ok'

    

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(codigo__icontains=query ) |
			Q(descripcion__icontains=query)
        )
        results = Expediente.objects.filter(qset)
    else:
        results = []
    return render(request, "registro/search.html", {
        "results": results,
        "query": query
    })
