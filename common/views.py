from django.shortcuts import render


class TitleMixin:
    """ TitleMixin """

    title = None

    def get_context_data(self, **kwargs):
        """To get context data"""
        context = super(TitleMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context


def handling_404(request, exception):
    """404 page handling controller"""
    return render(request, '404.html', {})
