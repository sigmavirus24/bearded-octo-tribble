# Copyright 2013, Rackspace US, Inc.
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

import json

from django.core import urlresolvers
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseBadRequest
from horizon.tables import DataTableView

from openvas.openvas_reports import tables
from openvas import omp


class IndexView(DataTableView):
    table_class = tables.ReportsTable
    template_name = 'rackspace/openvas/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        tables = []
        for (name, table) in list(context.items()):
            if name.endswith('_table'):
                del context[name]
                table.data.parameters = json.dumps(
                    table.data.get_parameter_types(self.request))
                table.data.launch_url = urlresolvers.reverse(
                    'horizon:rackspace:heat_store:launch',
                    args=[table.data.id])
                tables.append(table)

        context['tables'] = tables
        return self.render_to_response(context)

    def get_tables(self):
        return dict(('Reports', self.table_class(self.request, t))
                    for t in omp.get_all_reports())
