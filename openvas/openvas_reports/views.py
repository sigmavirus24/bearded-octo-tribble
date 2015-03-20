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
import io

from django.core.servers.basehttp import FileWrapper
from django.views.generic.base import View, TemplateView
from django.http import StreamingHttpResponse
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
        txt_uuid = omp.get_report_format('txt')
        output = omp.omp(['-R', report_id, '-f', txt_uuid]).stdout.read()
        context['report_content'] = output
        context['report_id'] = report_id
        return context


class PdfReportView(View):
    def get(self, *args, **kwargs):
        report_id = kwargs['report_id']
        pdf_uuid = omp.get_report_format('pdf')
        proc = omp.omp(['-R', report_id, '-f', pdf_uuid])
        b = io.BytesIO(proc.stdout.read())
        b.seek(0, 0)
        resp = StreamingHttpResponse(FileWrapper(b),
                                     mimetype='application/pdf')
        resp['Content-Disposition'] = 'attachment; filename={0}.pdf'.format(
            report_id
        )
        resp['Content-Length'] = len(b.getvalue())
        return resp
