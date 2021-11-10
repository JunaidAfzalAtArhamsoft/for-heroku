from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from .forms import PersonRegisterForm, TaskCreateForm
from django.contrib.auth.views import LoginView, TemplateView, LogoutView
from .models import Person, Task


class MainPageView(TemplateView):
    template_name = 'ManageTask/main_page.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return self.render_to_response(context)


class PersonFormView(CreateView):
    """
    Show registration form and on success goto login page
    """
    template_name = 'ManageTask/register.html'
    form_class = PersonRegisterForm
    success_url = reverse_lazy('ManageTask:login')


class PersonLoginView(LoginView):
    template_name = 'ManageTask/login.html'

    def get_redirect_url(self):
        return '/ManageTask/dashboard/'


class PersonLogoutView(LogoutView):
    next_page = '/ManageTask/'


class TaskCreateView(CreateView):
    """
    Show Task create form.
    And insert task in database.
    """

    template_name = "ManageTask/add_task.html"
    form_class = TaskCreateForm
    success_url = '/ManageTask/tasks/'

    def form_valid(self, form):
        """
        Message: If form is valid than it save the task in database
        Parameters:
            form: Form filed by user with task information
        Returns:
            HttpResponseRedirect: redirect to success url
        """

        task = form.instance
        user = self.request.user
        person = Person.objects.filter(username=user)
        person = person[0]
        task.owner = person
        task.save()
        self.object = task

        return HttpResponseRedirect(self.get_success_url())


class TaskView(ListView):
    """
    Show Tasks to loge in user
    """
    # template_name = 'ManageTask/task_list.html'
    model = Task

    def get_queryset(self):
        user = self.request.user
        print(user)
        user = Person.objects.filter(username=user)
        user = user[0]
        print(user)
        task = Task.objects.filter(owner=user)
        return task

    def get(self, request, *args, **kwargs):
        # if not validate_request(request):
        #     return HttpResponseForbidden()
        # else:
        self.object_list = self.get_queryset()

        comp_tasks = self.object_list.filter(is_complete=True)
        pending_tasks = self.object_list.filter(is_complete=False)

        context = {
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'pending_tasks': pending_tasks,
                'complete_tasks': comp_tasks,
            }
        return self.render_to_response(context)


class DashboardView(TemplateView):
    template_name = 'ManageTask/dashboard.html'


class UpdateTaskView(UpdateView):
    model = Task
    fields = ['task_title', 'task_description', 'task_category', 'is_complete']
    template_name = 'ManageTask/update_task.html'
    success_url = "/ManageTask/tasks/"


class SpecificTaskView(DetailView):
    model = Task
    template_name = 'ManageTask/specific_task.html'


class DeleteTaskView(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'ManageTask/delete_task.html'
    success_url = reverse_lazy('ManageTask:task_view')
