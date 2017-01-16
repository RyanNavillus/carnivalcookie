from flask import Flask, request, redirect
import twilio.twiml
import os
import time
from twilio.rest import TwilioRestClient
# put your own credentials here
ACCOUNT_SID = 'ACb77e65b904971ea0cf4b774dd64e62f5'
AUTH_TOKEN = '3b4cdb19f6d7a33199b21ca878536705'

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	"""Respond to incoming calls with a simple text message."""
	currentDate = (time.strftime("%m-%d-%Y"))
	DiningCourts = ["Earhart", "Ford", "Hillenbrand", "Wiley", "Windsor"]
	output = "\nDining Courts with Carnival Cookies today:\n"
	for DiningCourt in DiningCourts:
		command = "curl -s https://api.hfs.purdue.edu/menus/v1/locations/" + DiningCourt + "/" + currentDate + " | grep -m 1 -c 'Carnival'"
		if os.popen(command).read().rstrip() == "1":
			output = output + DiningCourt + "\n"

	if output == "Dining Courts with Carnival Cookies today:\n":
			s = u'\U0001F622'
			with open("yop", "wb") as f:
				f.write(s.encode("utf-8"))
			output = "No Dining Courts Have Carnival Cookies today " + s
			output = output.encode('utf-8')
	resp = twilio.twiml.Response()
	resp.message(output)
	return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
