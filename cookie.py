from twilio.rest import TwilioRestClient
# put your own credentials here
ACCOUNT_SID = 'ACb77e65b904971ea0cf4b774dd64e62f5'
AUTH_TOKEN = '3b4cdb19f6d7a33199b21ca878536705'
	
import os
import time
currentDate = (time.strftime("%m-%d-%Y"))
DiningCourts = ["Earhart", "Ford", "Hillenbrand", "Wiley", "Windsor"]
output = "Dining Courts with Red Velvet Cake today:\n"
for DiningCourt in DiningCourts:
	command = "curl -s https://api.hfs.purdue.edu/menus/v1/locations/" + DiningCourt + "/" + currentDate + " | grep -m 1 -c 'Velvet'"
	if os.popen(command).read().rstrip() == "1":
		output = output + DiningCourt + "\n"

if output == "Dining Courts with Red Velvet Cake today:\n":
		s = u'\U0001F622'
		with open("yop", "wb") as f:
		   f.write(s.encode("utf-8"))
		output = "No Dining Courts Have Red Velvet Cake today " + s
		output = output.encode('utf-8')
print output
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
client.messages.create(
        to = '9737387415',
        from_ = '8629022176',
        body = output,
)
