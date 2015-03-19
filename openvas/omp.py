import collections
import re
import subprocess
import xml.etree.ElementTree as ET


_Report = collections.namedtuple('Report',
                                 ['uuid', 'status', 'high', 'med', 'low',
                                  'log', 'date'])
_Task = collections.namedtuple('Task', ['uuid', 'status', 'type'])


class _Parser(object):
    _re = re.compile('\s+')

    @classmethod
    def parse(cls, line):
        split_list = cls._re.split(line, cls._num_splits)
        return cls(*split_list)


class Task(_Task, _Parser):
    _num_splits = 2


class Report(_Report, _Parser):
    _num_splits = 7


def omp(args):
    return subprocess.Popen(['omp'] + args, stdout=subprocess.PIPE)


def send_xml(xml):
    return omp(['-X', xml])


def create_target(name, hosts):
    xml = """<create_target>
    <name>{0}</name>
    <hosts>{1}</hosts>
    </create_target>"""
    p = send_xml(xml)
    x = ET.XML(p.stdout.read())
    return x.attrib


def get_targets():
    p = omp(['--get-targets'])
    output = p.stdout.read()
    return dict(l[0].split()[::-1] for l in output.splitlines())


def get_tasks():
    p = omp(['--get-tasks'])
    output = p.stdout.read()
    return (Task.parse(line) for line in output.splitlines())


def get_reports_for(task):
    # Accept a Task object or a plain uuid string
    task_uuid = getattr(task, 'uuid', None)
    task_uuid = task_uuid or task
    p = omp(['--get-tasks', task_uuid])
    output = p.stdout.read()
    # The first line of the output here is just the task description so we can
    # skip it.
    return (Report.parse(line.strip()) for line in output.splitlines()[1:])


def get_all_reports():
    for task in get_tasks():
        for report in get_reports_for(task):
            yield report, task
