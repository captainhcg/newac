from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('index.views',
    url(r'^$', 'index'),
    # url(r'create$', 'create_topic'),
    # url(r'^(?P<topic_id>\d+)/vote$', 'vote_topic'),
    # url(r'^(?P<topic_id>\d+)/edit$', 'edit_topic'),
    # url(r'^(?P<topic_id>\d+)/open$', 'open_topic'),
    # url(r'\d+/complete$', 'complete_topic'),
)
