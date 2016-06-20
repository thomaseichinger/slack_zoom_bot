from slackclient import SlackClient
from time import sleep
from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

config_data = load(open("./config.yaml", 'r').read(), Loader=Loader)

sc = SlackClient(config_data['token'])

text = "Dear <!everyone>, this is a friendly reminder that the standup is about to happen again on " + config_data['zoom_url']
text2 = "So please get coffee, take a comfortable seat and enjoy!"

sc.api_call("chat.postMessage", channel=config_data['slack_channel'], text=text, username='Standup_Whoop', icon_emoji=':necktie:')

sleep(2)

sc.api_call("chat.postMessage", channel=config_data['slack_channel'], text=text2, username='Standup_Whoop', icon_emoji=':necktie:')

print "Sucessfully slackbotted."

quit()
