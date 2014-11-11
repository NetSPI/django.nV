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