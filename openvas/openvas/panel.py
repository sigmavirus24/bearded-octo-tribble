import horizon

from openvas import dashboard


class OpenVasPanel(horizon.Panel):
    name = 'Reports'
    slug = 'openvas-reports'


dashboard.OpenVasDashboard.register(OpenVasPanel)
