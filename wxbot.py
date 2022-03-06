from urllib import request
from loguru import logger
import ssl
import urllib.error
import json



from flexget import plugin
from flexget.config_schema import one_or_more
from flexget.event import event
from flexget.plugin import PluginWarning
from urllib import parse

plugin_name = 'wxbot'
logger = logger.bind(name=plugin_name)


class WxBotNotifier:
    """
    Author: vincent806
    Date: 07Dec2021
    Description: support wxbot notification for flexget
    Usage: put this file to plugin folder of flexget

    Example config:

    notify:
      entries:
        title: "{{ task }}"
        message: "{{ title }}"
        via:
          - wxbot:
              webhook: your_webhook_url
    """

    schema = {
        'type': 'object',
        'properties': {
            'webhook': {'type': 'string'},
        },
        'required': ['webhook'],
        'additionalProperties': False,
    }

    def notify(self, title, message, config):
        """
        Send a wxbot notification
        """

        baseurl = config.get('webhook')

        # format the message header
        baseurlheader = {
            "Content-Type": "application/json;charset=UTF-8"
        }

        if (len(title)==0):
            title = "Subject is not specified."

        # format message
        json_text = {
            "msgtype": "markdown",
            "markdown": {
                "content": "#### **" + title + "** \n\n" + message
            },
            "at": {
                "isAtAll": True
            }
        }

        # handle SSL certification error
        ssl._create_default_https_context = ssl._create_unverified_context


        send_data = json.dumps(json_text)
        send_data = send_data.encode("utf-8")
        handler = request.Request(url=baseurl, data=send_data, headers=baseurlheader)

        try:
            response = request.urlopen(handler)
        except urllib.error.HTTPError as e:
            print(e.__dict__)
        except urllib.error.URLError as e:
            print(e.__dict__)


@event('plugin.register')
def register_plugin():
    plugin.register(WxBotNotifier, plugin_name, api_ver=2, interfaces=['notifiers'])
