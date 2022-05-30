import os
from slack_sdk import WebClient

client = WebClient(token=os.environ.get("SLACK_TOKEN"))


def send_slack(channel, text):
    client.chat_postMessage(channel=channel, text=text)
