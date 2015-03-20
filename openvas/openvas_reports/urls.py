try:
    from django.conf.urls.defaults import patterns, url
except ImportError:  # Django 1.6
    from django.conf.urls import patterns, url

from openvas.openvas_reports.views import (
    IndexView, TextReportView, PdfReportView
)

urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view(), name='index'),
                       url(r'^reports/(?P<report_id>[^/]+)/text',
                           TextReportView.as_view(), name='text_report'),
                       url(r'^reports/(?P<report_id>[^/]+)/pdf',
                           PdfReportView.as_view(), name='pdf_report'),
                       )
