# #do we want to use built in user password authetication. I guess yes\
# #permission caching

# #detail.html
# #<!--{% if error_message %}<p><strong>{{error_message}}</strong></p>{% endif%}

# <form action="{% url 'taskManager:comment' task.id %}" method= "post">
#  {% csrf_token %} 
# {% for comment in task.comment_set.all %}
# 	<input type ="text" name="comment" id="choice{{ forloop.counter }}" value="{{comment.id}}">
# 	<label for="choice{{forloop.counter}}"> {{comment.comment_text}}</label><br />
# {% endfor %}
# <input type="submit" value = "Comment" />
# </form>
# -->







				# counter = 0 

				# groups_changed = False


				# for user in user_list:

				# 	selected_choice = request.POST.get('user' + str(counter))

				# 	if selected_choice == 1 :
				# 		grp = Group.objects.get(name='admin_g')
				# 		user.groups.add(grp)#admin group
				# 		groups_changed = True
				# 	elif selected_choice == 2:
				# 		grp = Group.objects.get(name='project_managers')
				# 		user.groups.add(grp)#manager  group						
				# 		groups_changed = True
				# 	elif selected_choice :
				# 		grp = Group.objects.get(name='team_member')
				# 		user.groups.add(grp)
				# 		groups_changed = True

				# 	user.save()

				# 	counter = counter+1







				{% for user in users %}
        
        <h5>{{user.username}}</h5>        
        
        <input type="radio" name="radio" id="user{{forloop.counter}}" value="admin_g">Admin Access<br />
        <input type="radio" name="radio" id="user{{forloop.counter}}" value="project_managers">Project Manager Access<br /> 
        <input type="radio" name="radio" id="user{{forloop.counter}}" value="team_member">Project Member Access<br />

        {%  endfor %}   






        <link rel="stylesheet" href="/static/css/app.css" />
    <link rel="stylesheet" href="/static/css/bootstrap.css" />
    <link rel="stylesheet" href="/static/css/bootstrap.min.css" />
    <link rel="stylesheet" href="/static/css/font-awesome.css" />