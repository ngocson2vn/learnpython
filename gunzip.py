#!/usr/bin/python

import base64
import gzip
import io
import json

outEvent = 'H4sIAAAAAAAAAL2V224bRwyGX6XY64zNOXAOujMcJ+iF0wByr6qg4MyQyaK2JGjXMQLD715Kjg0XcFMXTaqLFZZz4D8/v+HeDlc8TfSRL75seVgMr08uTn4/P1suT96eDa+Gzc2adxpOWDAUGyOkoOHLzce3u831Vkem9XRMW7Pe7OZPTNNs7PHTyTq2PT55/255/GZ8d2rGX5bm/W7Tr9s8btb3Oy3nHdOVbuUBe5XmTSqpm0DoDEFPhgSsz/pD23TJdF2nthu3+x3ejJcz76Zh8duwvZ4+qYx5lLHRfsyMm2n4cEhx9pnX837W7TD2fSZfoi25QPIFMWD2IZcU0NuSSvAY0/4fHdpSggsRvHPRWqfZ51ENm+lKz27RuQLZ6bB1rx6M1O1vV8NTIathoZGvw+evcXl9paHVECJ377CxrRyCbypHhCRy5to8uNXw6nHZz/2wBCJQFojGdyGDlcjkjmJ68yX7lChbOix7lHlY5sBmA8EA/gRxAX6B6chavxrudGrny/Ez777cy3x4+5qQG1ULuZqG5A3m4k111EzwNaTq2DP0Q8Ku6cb1w3lXA+3WC7qZFsrH4q98LJ7yseB1327G9fy3kBxrQUikW9NTYOPFoikO1QIVU2txNUq6l3DDl5cXevDzSSVYryGaZ77azof3vSubP/heXsgiUmuimiukmL1jYGTCprXINnP0zruaU4rArVbno3WtxhRaFS3UIaEaPF9Pp5vOuqcDuHuMHXIsfz091ZukLqvP/408/33JY8ned7BoofceAkVwDiJa6SI2wjPk7b0gpGrYpmwQsJmM1RmJKlc4ldjCP5MXVPpRCvkF5JVctUYJjLOFDSaXTaHkDbUgRTuCGuh/MHlNmVD7UaFz+qipmpIRTGsFoQNnyfQMeS5+izxpes0x1OwKeSD1vBWfWahjbh0tSudsfeq9Bp3a1YXmUtKrx+x8Cf8zeeH7kldd86LWBeLEYIsX7IGlWNFsDeQZ8iznHLlok/O8B6FGU2PQenSC2EPrjuqLyMtHCC8hzwVbi2QxRchpQgyGrCctewVnAWys4UeThy1LaMlIZjJ6bu3zJNW4wB6itiuw9jny0jd7niQk8FyJmwQQz12fiVIF20IvDSBQ1W+Qk5IgcEkWtRtCbbUHtP3fkvfh7k+uaX6IXggAAA=='

decoded = base64.b64decode(outEvent)
stream = io.BytesIO(decoded)
d = gzip.GzipFile(fileobj=stream).read()
record = json.loads(d.decode('utf-8'))
for event in record["logEvents"]:
	m = json.loads(event["message"])
	notification = m["notification"]
	delivery = m["delivery"]
	row = ",".join([
		notification["messageMD5Sum"],
		notification["messageId"],
		notification["timestamp"],
		delivery["deliveryId"],
		delivery["destination"],
		str(delivery["dwellTimeMs"]),
		str(delivery["attempts"]),
		delivery["token"],
		str(delivery["statusCode"]),
		m["status"]
	])
	print(row)