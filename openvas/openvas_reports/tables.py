import datetime
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


class UTC(datetime.tzinfo):
    """Yet another UTC reimplementation."""
    ZERO = datetime.timedelta(0)

    def __repr__(self):
        return 'UTC()'

    def dst(self, dt):
        return self.ZERO

    def tzname(self, dt):
        return 'UTC'

    def utcoffset(self, dt):
        return self.ZERO


TIMEFORMAT = '%Y-%m-%dT%H:%M:%SZ'


def parse_date(datum):
    date = datum.date
    dt = datetime.datetime.strptime(date, TIMEFORMAT)
    dt.replace(tzinfo=UTC())
    return dt


class ReportsTable(tables.DataTable):
    task_name = tables.Column('task_name', verbose_name='Task',
                              sortable=False)
    report_uuid = tables.Column('report_uuid', verbose_name='Report UUID',
                                sortable=False)
    report_status = tables.Column('report_status', verbose_name='Status',
                                  sortable=False)
    high = tables.Column('high', verbose_name='High Severity', sortable=True)
    med = tables.Column('med', verbose_name='Medium Severity', sortable=True)
    low = tables.Column('low', verbose_name='Low Severity', sortable=True)
    log = tables.Column('log', verbose_name='Log Severity', sortable=True)
    date = tables.Column(parse_date, verbose_name='Date', sortable=True)
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
