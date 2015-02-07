from django.conf.urls import patterns, url
from map.views.pensum_views import *

urlpatterns = patterns('',
   url(r'^pensum/$', pensum, name='pensum'),
   url(r'^pensum/(?P<pensum_id>[0-9]+)/$', pensum, name='pensum'),
   url(r'^pensum/create/$', pensum_edit, name='create_pensum'),
   url(r'^pensum/(?P<pensum_id>[0-9]+)/edit/$', pensum_edit, name='edit_pensum'),
   url(r'^pensum/(?P<pensum_id>[0-9]+)/delete/$', pensum_delete, name='delete_pensum'),
)

from map.views.course_views import *
urlpatterns += patterns('',
   url(r'^course/$', course, name='course'),
   url(r'^course/(?P<course_id>[0-9]+)/$', course, name='course'),
   url(r'^course/create/$', course_edit, name='create_course'),
   url(r'^course/(?P<course_id>[0-9]+)/edit/$', course_edit, name='edit_course'),
   url(r'^course/(?P<course_id>[0-9]+)/delete/$', course_delete, name='delete_course'),
)

from map.views.section_views import *
urlpatterns += patterns('',

   url(r'^section/$', section, name='section'),

   url(r'^section/(?P<section_id>[0-9]+)/$', section, name='section'),
   url(r'^section/create/$', section_edit, name='create_section'),
   url(r'^section/(?P<section_id>[0-9]+)/edit/$', section_edit, name='edit_section'),
   url(r'^section/(?P<section_id>[0-9]+)/delete/$', section_delete, name='delete_section'),
)

from map.views.student_views import *
urlpatterns += patterns('',
   url(r'^student/$', student, name='student'),
   url(r'^student/(?P<student_id>[0-9]+)/$', student, name='student'),
   url(r'^student/create/$', student_edit, name='create_student'),
   url(r'^student/(?P<student_id>[0-9]+)/edit/$', student_edit, name='edit_student'),
   url(r'^student/(?P<student_id>[0-9]+)/delete/$', student_delete, name='delete_student'),
)

from map.views.teacher_views import *
urlpatterns += patterns('',
   url(r'^teacher/$', teacher, name='teacher'),
   url(r'^teacher/(?P<teacher_id>[0-9]+)/$', teacher, name='teacher'),
   url(r'^teacher/create/$', teacher_edit, name='create_teacher'),
   url(r'^teacher/(?P<teacher_id>[0-9]+)/edit/$', teacher_edit, name='edit_teacher'),
   url(r'^teacher/(?P<teacher_id>[0-9]+)/delete/$', teacher_delete, name='delete_teacher'),
)

from map.views.subject_views import *
urlpatterns += patterns('',
   url(r'^subject/$', subject, name='subject'),
   url(r'^subject/(?P<subject_id>[0-9]+)/$', subject, name='subject'),
   url(r'^subject/create/$', subject_edit, name='create_subject'),
   url(r'^subject/(?P<subject_id>[0-9]+)/edit/$', subject_edit, name='edit_subject'),
   url(r'^subject/(?P<subject_id>[0-9]+)/delete/$', subject_delete, name='delete_subject'),
)


from map.views.course_views import *
urlpatterns += patterns('',

    url(
        regex=r'^course/$',
        view=CourseView.as_view(),
        name='map_course_list'
    ),

)

# API pensum
urlpatterns += patterns('map.api.pensum_api',
    url(r'^api/pensum/$', 'pensum'),
    url(r'^api/pensum/(?P<pensum_id>[0-9]+)/$', 'pensum'),
)
# API section
urlpatterns += patterns('map.api.section_api',
     url(r'^api/section/$', 'section'),
     url(r'^api/section/(?P<section_id>[0-9]+)/$', 'section'),
)
# API course
urlpatterns += patterns('map.api.course_api',
     url(r'^api/course/$', 'course'),
     url(r'^api/course/(?P<course_id>[0-9]+)/$', 'course'),
)
# API teacher
urlpatterns += patterns('map.api.teacher_api',
     url(r'^api/teacher/$', 'teacher'),
     url(r'^api/teacher/(?P<teacher_id>[0-9]+)/$', 'teacher'),
)
# API student
urlpatterns += patterns('map.api.student_api',
     url(r'^api/student/$', 'student'),
     url(r'^api/student/(?P<student_id>[0-9]+)/$', 'student'),
)
# API subject
urlpatterns += patterns('map.api.subject_api',
     url(r'^api/subject/$', 'subject'),
     url(r'^api/subject/(?P<subject_id>[0-9]+)/$', 'subject'),
)
