from django.http import HttpResponseRedirect
from django.views import View
from django.db.utils import OperationalError
from django.shortcuts import render
from django.db.models import F

from interview.models import Issue
from interview.form import IssueForm


class ListIssuesView(View):

    def get(self, request):
        # `Site`.`SiteName`, `Panel`.`Brand`, `Panel`.`Model`,`Issue`.`Comment`

        issues = Issue.objects.using('interview_db').annotate(
            site_name=F('site__site_name'),
            panel_brand=F('panel__brand'),
            panel_model=F('panel__model')
        ).order_by('id_issue').all()

        return render(request, 'issue-list.html', {'issues': issues})


class AddIssueView(View):
    def get(self, request):
        form = IssueForm()
        return render(request, 'issue-add.html', {'form': form})

    def post(self, request):
        form = IssueForm(request.POST)
        if form.is_valid():
            try:
                save_issue_from_formdata(form.cleaned_data)
            except (ValueError, OperationalError):
                return HttpResponseRedirect('/issues/add/?message=There was a problem saving your Issue.&class=error')
            return HttpResponseRedirect('/issues/?message=Your issue is added successfully&class=success')
        return HttpResponseRedirect(
            '/issues/add/?message=We could not process this data, try changing something&class=error')


def save_issue_from_formdata(data):
    new_issue = Issue(comment=data['comment'], panel=data['panel'], site=data['site'])
    new_issue.save()

