from django.http  import HttpResponse
from django.middleware import csrf
from django.shortcuts import render

def hello(request):
	csrf_token = csrf.get_token(request)
	return HttpResponse("Hello<br>My Name is Manoj Kumar<br><form method='post' action='message'>{0}<input name='message' type=text value='hi'></input><input type='submit'></input></form>".format('<input type="hidden" name="csrfmiddlewaretoken" value="%s">' % csrf_token))

def message(request):
	# import ipdb; ipdb.set_trace()
	message = "empty"
	if request.method == 'POST' and "message" in request.POST:
		message = request.POST.get("message")
	return HttpResponse(message)

def hello_template(request):
	context = {"csrf_token": csrf.get_token(request)}
	return render(request, "hello_form.html", context=context)