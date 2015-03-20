# Copyright 2015, Rackspace US, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from django.core import urlresolvers
from django.views.generic.base import TemplateView
from django.http import HttpResponse, HttpResponseBadRequest
import horizon.tables

from openvas import omp
from openvas.openvas_reports import tables


class IndexView(horizon.tables.DataTableView):
    table_class = tables.ReportsTable
    template_name = 'openvas/openvas/index.html'

    def get_data(self):
        return list(omp.get_all_reports())


class TextReportView(TemplateView):
    template_name = 'openvas/openvas/text_report.html'

    def get_context_data(self, **kwargs):
        context = super(TextReportView, self).get_context_data(**kwargs)
        report_id = kwargs['report_id']
        txt_uuid = omp.get_report_formats()['txt']
        output = omp.omp(['-R', report_id, '-f', txt_uuid]).stdout.read()
        context['report_data'] = output
        return context
