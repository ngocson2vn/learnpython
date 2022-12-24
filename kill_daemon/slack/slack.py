import os
import time
import slackweb

STATUS_FATAL = "fatal"
STATUS_WARN = "warn"
STATUS_OK = "ok"

def post_to_slack(slackUrl, title, text, status):
	slack = slackweb.Slack(url=slackUrl)
	attachments = []

	if status == STATUS_WARN:
		color = "#FF8000"
	elif status == STATUS_FATAL:
		color = "#FF0000"
	elif status == STATUS_OK:
		color = "#36a64F"

	a = {
			"color": color,
			"title": title,
			"text": text,
			"ts": int(time.time())
		}
	attachments.append(a)
	slack.notify(username='AutoScaling', attachments=attachments)