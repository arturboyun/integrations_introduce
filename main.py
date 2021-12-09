from contrib import Alert
from integrations.notify import SlackIntegration, MSTeamsIntegration, TelegramIntegration
from integrations.siem import QRadar, Splunk


def run_siem_enrichment(alert):
    qradar = QRadar()
    splunk = Splunk()

    qradar.enrich_alert_fields(alert)
    splunk.enrich_alert_fields(alert)


def send_alert(alert):
    slack = SlackIntegration()
    ms_teams = MSTeamsIntegration()
    telegram = TelegramIntegration()

    # slack.send_message('test slack message')
    # ms_teams.send_message('test ms_teams message')

    slack.send_alert(alert)
    ms_teams.send_alert(alert)
    telegram.send_alert(alert)


def main():
    alert1 = Alert("Alert id=1")
    alert2 = Alert("Alert id=2")
    alert3 = Alert("Alert id=3")

    send_alert(alert1)
    send_alert(alert2)
    send_alert(alert3)

    print('-------------------------------')
    print('')
    print('')

    run_siem_enrichment(alert2)
    run_siem_enrichment(alert3)

    print('-------------------------------')
    send_alert(alert1)
    print('-------------------------------')
    send_alert(alert2)
    print('-------------------------------')
    send_alert(alert3)


if __name__ == '__main__':
    main()
