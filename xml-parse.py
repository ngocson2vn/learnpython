import xml.etree.ElementTree as ET

configs = {
  'tokenCredentialId': '6db9b4f2-4aef-42ca-8aa2-a44cd069444e',
  'room': '#data_analytics_alert',
  'startNotification': 'false',
  'notifySuccess': 'false',
  'notifyAborted': 'true',
  'notifyNotBuilt': 'true',
  'notifyUnstable': 'false',
  'notifyRegression': 'false',
  'notifyFailure': 'true',
  'notifyEveryFailure': 'true',
  'notifyBackToNormal': 'true',
  'notifyRepeatedFailure': 'false',
  'includeTestSummary': 'false',
  'includeFailedTests': 'false'
}

tree = ET.parse('data/config.xml')
root = tree.getroot()
p = root.find('publishers')
slack = p.find('jenkins.plugins.slack.SlackNotifier')

authTokenCredentialId = slack.find('authTokenCredentialId')
if authTokenCredentialId != None:
  slack.remove(authTokenCredentialId)

tokenCredentialId = slack.find('tokenCredentialId')
if not tokenCredentialId:
  slack.insert(0, ET.Element('tokenCredentialId'))

slack[:] = sorted(slack, key=lambda e: e.tag)

for e in list(slack):
  if e.tag in configs:
    e.text = configs[e.tag]

tree.write('data/config-fixed.xml', encoding='UTF-8', xml_declaration=True)


# Output:
"""
baseUrl: None
teamDomain: None
authToken: None
tokenCredentialId: 6db9b4f2-4aef-42ca-8aa2-a44cd069444e
botUser: false
room: #data_analytics_alert
sendAsText: false
iconEmoji: None
username: None
startNotification: false
notifySuccess: false
notifyAborted: true
notifyNotBuilt: true
notifyUnstable: false
notifyRegression: false
notifyFailure: false
notifyEveryFailure: true
notifyBackToNormal: true
notifyRepeatedFailure: false
includeTestSummary: false
includeFailedTests: false
commitInfoChoice: NONE
includeCustomMessage: false
customMessage: None
customMessageSuccess: None
customMessageAborted: None
customMessageNotBuilt: None
customMessageUnstable: None
customMessageFailure: None
"""