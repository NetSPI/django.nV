# from django.contrib.auth.models import Group, Permission, User
# from django.contrib.contenttypes.models import ContentType
# from taskManager.models import Task, Comments, Project

# administrator_group = Group(name='admin_group')
# proj_manager_group = Group(name='proj_manager_group')
# proj_member_group = Group(name = 'proj_member_group')

# administrator_group.save()
# proj_manager_group.save()
# proj_member_group.save()

# ct = ContentType.objects.get(model = 'Project')

# permission0 = Permission.objects.create(codename='can_add_project',
# 										 name='Can add project', content_type = ct)
# permission1 = Permission.objects.create(codename='can_change_project',
# 										 name='Can change project', content_type = ct)
# permission2 = Permission.objects.create(codename='can_delete_project',
# 										 name='Can delete project', content_type = ct)

# ct = ContentType.objects.get(model = 'Task')

# permission3 = Permission.objects.create(codename='can_add_task',
# 										 name='Can add task', content_type = ct)
# permission4 = Permission.objects.create(codename='can_change_task',
# 										 name='Can change task', content_type = ct)
# permission5 = Permission.objects.create(codename='can_delete_task',
# 										 name='Can delete task', content_type = ct)

# ct = ContentType.objects.get(model  = 'Comments')

# permission6 = Permission.objects.create(codename='can_add_comments',
# 										 name='Can add comments', content_type = ct)
# permission7 = Permission.objects.create(codename='can_change_comments',
# 										 name='Can change comments', content_type = ct)
# permission8 = Permission.objects.create(codename='can_delete_comments',
# 										 name='Can delete comments', content_type = ct)

# ct = ContentType.objects.get(model = 'Group')

# permission9 = Permission.objects.create(codename='can_add_group',
# 										name = 'Can add group',
# 										content_type ='ct')
# permission10 = Permission.objects.create(codename = 'can_change_group',
# 										name = 'Can change group',
# 										content_type = 'ct')
# permission11 = Permission.objects.create(codename = 'can_delete_group', 
# 										name  = 'Can delete group', content_type = 'ct')

# ct = ContentType.objects.get(model = 'User')

# permission12 = Permission.objects.create(codename = 'can_delete_user', 
# 										name = 'Can delete user', content_type = 'ct')

# permission0.save()#add project
# permission1.save()#change project
# permission2.save()#delete project
# permission3.save()#add task
# permission4.save()#change task
# permission5.save()#delete task
# permission6.save()#add comments
# permission7.save()#change comments
# permission8.save()#delete comments
# permission9.save()#add group
# permission10.save()#change group
# permission11.save()#delete group
# permission12.save()#delete user


# adminsitrator_group.permissions = [permission0,permission1,permission2,permission3,permission4,
# permission5, permission6 , permission7 ,permission8, permission9,
# permission10, permission11, permission12]


# proj_manager_group.permissions = [permission3,permission4,
# permission5, permission6 , permission7 ,permission8]


# proj_member_group.permissions = [permission6 , permission7 ,permission8]

