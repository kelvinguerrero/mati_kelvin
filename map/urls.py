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
    # url(
    #     regex=r'^course/archive/$',
    #     view=CourseArchiveIndexView.as_view(),
    #     name='map_course_archive_index'
    # ),
    # url(
    #     regex=r'^course/create/$',
    #     view=CourseCreateView.as_view(),
    #     name='map_course_create'
    # ),
    # url(
    #     regex=r'^course/(?P<year>\d{4})/'
    #            '(?P<month>\d{1,2})/'
    #            '(?P<day>\d{1,2})/'
    #            '(?P<pk>\d+?)/$',
    #     view=CourseDateDetailView.as_view(),
    #     name='map_course_date_detail'
    # ),
    # url(
    #     regex=r'^course/archive/(?P<year>\d{4})/'
    #            '(?P<month>\d{1,2})/'
    #            '(?P<day>\d{1,2})/$',
    #     view=CourseDayArchiveView.as_view(),
    #     name='map_course_day_archive'
    # ),
    # url(
    #     regex=r'^course/(?P<pk>\d+?)/delete/$',
    #     view=CourseDeleteView.as_view(),
    #     name='map_course_delete'
    # ),
    # url(
    #     regex=r'^course/(?P<pk>\d+?)/$',
    #     view=CourseDetailView.as_view(),
    #     name='map_course_detail'
    # ),
    url(
        regex=r'^course/$',
        view=CourseView.as_view(),
        name='map_course_list'
    ),
    # url(
    #     regex=r'^course/archive/(?P<year>\d{4})/'
    #            '(?P<month>\d{1,2})/$',
    #     view=CourseMonthArchiveView.as_view(),
    #     name='map_course_month_archive'
    # ),
    # url(
    #     regex=r'^course/today/$',
    #     view=CourseTodayArchiveView.as_view(),
    #     name='map_course_today_archive'
    # ),
    # url(
    #     regex=r'^course/(?P<pk>\d+?)/update/$',
    #     view=CourseUpdateView.as_view(),
    #     name='map_course_update'
    # ),
    # url(
    #     regex=r'^course/archive/(?P<year>\d{4})/'
    #            '(?P<month>\d{1,2})/'
    #            'week/(?P<week>\d{1,2})/$',
    #     view=CourseWeekArchiveView.as_view(),
    #     name='map_course_week_archive'
    # ),
    # url(
    #     regex=r'^course/archive/(?P<year>\d{4})/$',
    #     view=CourseYearArchiveView.as_view(),
    #     name='map_course_year_archive'
    # ),
)

# API pensum
urlpatterns += patterns('map.api.pensum_api',
    url(r'^api/pensum/$', 'pensum'),
    url(r'^api/pensum/(?P<pensum_id>[0-9]+)/$', 'pensum'),
)

urlpatterns += patterns('map.api.section_api',
     url(r'^api/section/$', 'section'),
     url(r'^api/section/(?P<section_id>[0-9]+)/$', 'section'),
)

urlpatterns += patterns('map.api.course_api',
     url(r'^api/course/$', 'course'),
     url(r'^api/course/(?P<course_id>[0-9]+)/$', 'course'),
)

urlpatterns += patterns('map.api.teacher_api',
     url(r'^api/teacher/$', 'teacher'),
     url(r'^api/teacher/(?P<teacher_id>[0-9]+)/$', 'teacher'),
)
