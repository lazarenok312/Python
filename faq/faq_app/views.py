from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponseForbidden

from .models import UserQuestion, Answer, UserLikes, UserDislikes
from .forms import AnswerForm, LikeForm, DislikeForm

# Create your views here.
class IndexView(generic.ListView):
	model = UserQuestion
	template_name = "faq/index.html"

	def get_queryset(self):
		return UserQuestion.objects.all().order_by('pub_date')

class DetailView(generic.DetailView):
	model = UserQuestion
	template_name = "faq/detail.html"

	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		form = AnswerForm
		context["form"] = form
		return context

class CreateAnswer(generic.edit.CreateView):
	model = Answer
	form_class = AnswerForm

	def get_success_url(self):
		return reverse('faq:detail', kwargs={'pk': self.object.question.pk})

	def form_valid(self, form):
		answer = form.save(commit=False)
		answer.user = self.request.user
		answer.question_id = self.request.POST.get('question')
		answer.save()
		return super().form_valid(form)

class RegisterView(generic.edit.FormView):
	form_class = UserCreationForm
	success_url = "/login/"
	template_name = "registration/register.html"

	def form_valid(self, form):
		form.save()
		return super(RegisterView, self).form_valid(form)

	def form_invalid(self, form):
		return super(RegisterView, self).form_invalid(form)

class CreateQuestionView(generic.edit.CreateView):
	model = UserQuestion
	template_name = "faq/create_question.html"
	fields = ['title', 'body']

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('faq:index')

class UpdateQuestionView(generic.edit.UpdateView):
	model = UserQuestion
	template_name = "faq/update_question.html"
	fields = ['title', 'body']

	def get_success_url(self):
		return reverse('faq:index')

class DeleteQuestionView(generic.edit.DeleteView):
	model = UserQuestion
	template_name = "faq/question_confirm_delete.html"

	def get_success_url(self):
		return reverse('faq:index')

# def question_detail(request, question_id):
# 	template_name = "faq/detail.html"
# 	question = get_object_or_404(UserQuestion, id=question_id)
# 	answers = question.answer_set.all()
# 	new_answer = None

# 	if request.method == 'POST':
# 		answer_form = AnswerForm(data=request.POST)
# 		if answer_form.is_valid():
# 			new_answer = answer_form.save(commit=False)
# 			new_answer.question = question
# 			new_answer.user = request.user
# 			new_answer.save()
# 	else:
# 		answer_form = AnswerForm()

# 	return render(request, template_name, {'question': question, 'answers': answers, 'new_answer': new_answer, 'answer_form': answer_form})

def liked(request, answer_id):
	answer = get_object_or_404(Answer, id=answer_id)
	if request.method == 'POST':
		form = LikeForm(request.POST)
		if form.is_valid():
			if request.user.is_authenticated:
				if not UserLikes.objects.filter(user=request.user, answer=answer) and not UserDislikes.objects.filter(user=request.user, answer=answer):
					like = UserLikes(user=request.user, answer=answer)
					answer.likes += 1
					like.save()
					answer.save()
				return redirect('faq:detail', answer.question.id)
			else:
				return redirect('login')
	else:
		form = LikeForm()

	return redirect('faq:detail', answer.question.pk)

def disliked(request, answer_id):
	answer = get_object_or_404(Answer, id=answer_id)
	if request.method == 'POST':
		form = DislikeForm(request.POST)
		if form.is_valid():
			if request.user.is_authenticated:
				if not UserLikes.objects.filter(user=request.user, answer=answer) and not UserDislikes.objects.filter(user=request.user, answer=answer):
					like = UserDislikes(user=request.user, answer=answer)
					answer.dislikes += 1
					like.save()
					answer.save()
				return redirect('faq:detail', answer.question.id)
			else:
				return redirect('login')
	else:
		form = DislikeForm()

	return redirect('faq:detail', answer.question.pk)