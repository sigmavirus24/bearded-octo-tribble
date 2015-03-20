import horizon

from openvas import dashboard


class OpenVasPanel(horizon.Panel):
    name = 'Reports'
    slug = 'openvas_reports'


dashboard.OpenVasDashboard.register(OpenVasPanel)
