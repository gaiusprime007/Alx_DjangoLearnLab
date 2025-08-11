from django import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import user_passes_test

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return render(request, 'relationship_app/librarian_view.html')


class LibrarianView(TemplateView):
    template_name = 'relationship_app/librarian_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Welcome to the Librarian Dashboard"
        return context