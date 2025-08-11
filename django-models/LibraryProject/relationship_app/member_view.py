from django import render
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import TemplateView

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return render(request, 'relationship_app/member_view.html')

class Member(TemplateView):
    template_name = 'relationship_app/member_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Welcome to the Member Dashboard"
        return context