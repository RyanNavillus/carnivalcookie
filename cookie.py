from twilio.rest import TwilioRestClient
# put your own credentials here
ACCOUNT_SID = 'ACb77e65b904971ea0cf4b774dd64e62f5'
AUTH_TOKEN = 'b3b93b889b515a90ea0826f1f08b1a4b'
	
import os
import time
currentDate = (time.strftime("%m-%d-%Y"))
DiningCourts = ["Earhart", "Ford", "Hillenbrand", "Wiley", "Windsor"]
output = "Dining Courts with Carnival Cookies today:\n"
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
print output
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
client.messages.create(
        to = '9737387415',
        from_ = '8629022176',
        body = output,
)
