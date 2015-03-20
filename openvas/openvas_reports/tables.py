from horizon import tables

from openvas import omp


class ReportRow(tables.Row):
    def get_cells(self):
        (task, report) = self.datum
        return (task.uuid,) + report


class ReportsTable(tables.DataTable):
    task_uuid = tables.Column('task_uuid', verbose_name='Task UUID',
                              sortable=True)
    report_uuid = tables.Column('report_uuid', verbose_name='Report UUID',
                                sortable=True)
    report_status = tables.Column('report_status', verbose_name='Status',
                                  sortable=False)
    high = tables.Column('high', verbose_name='High Severity', sortable=False)
    med = tables.Column('med', verbose_name='Medium Severity', sortable=False)
    low = tables.Column('low', verbose_name='Low Severity', sortable=False)
    log = tables.Column('log', verbose_name='Log Severity', sortable=False)
    date = tables.Column('date', verbose_name='Date', sortable=True)
    name = tables.Column('template', sortable=False,)

    class Meta:
        name = 'template'
        multi_select = False
        row_class = ReportRow
        verbose_name = 'Reports'

    def get_data(self, *args, **kwargs):
        return list(omp.get_all_reports())

    def get_rows(self):
        data = self.get_data()
        return [self._meta.row_class(self, datum) for datum in data]
