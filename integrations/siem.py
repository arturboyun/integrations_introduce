import random

from contrib import Alert

operating_systems = ['macos', 'linux', 'windows']
ips = [
    '123.123.123.123',
    '111.168.21.1',
    '300.321.123.55'
]

class SiemBase(object):
    """Base class for SIEM integrations"""

    # def search_by_usernames(self, usernames: List[str]) -> List[dict]:
    #     raise NotImplementedError
    #
    # def search_last_record_by_source_ip(self, source_ip: str) -> List[dict]:
    #     raise NotImplementedError

    def enrich_alert_fields(self, alert) -> Alert:
        raise NotImplementedError


class QRadar(SiemBase):

    def enrich_alert_fields(self, alert) -> Alert:
        alert.fields['attacker_os'] = random.choice(operating_systems)
        return alert


class Splunk(SiemBase):

    def enrich_alert_fields(self, alert) -> Alert:
        alert.fields['attacker_ip'] = random.choice(ips)
        return alert
