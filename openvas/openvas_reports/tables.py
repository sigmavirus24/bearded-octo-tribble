from django.core import urlresolvers
from horizon import tables


def text_link(datum):
    return urlresolvers.reverse(
        'horizon:openvas:openvas_reports:text_report',
        args=[datum.report_uuid]
    )


def pdf_link(datum):
    return urlresolvers.reverse(
        'horizon:openvas:openvas_reports:pdf_report',
        args=[datum.report_uuid]
    )


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
    text_report = tables.Column('text', verbose_name='Text Report',
                                link=text_link, sortable=False)
    pdf_report = tables.Column('pdf', verbose_name='Pdf Report',
                               link=pdf_link, sortable=False)

    class Meta:
        name = 'reports'
        multi_select = False
        row_class = tables.Row
        verbose_name = 'Reports'

    def get_object_id(self, datum):
        return datum.report_uuid
