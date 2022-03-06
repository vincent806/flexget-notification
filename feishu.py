from urllib import request
from loguru import logger
import ssl
import urllib.error
import json
import time
import hmac
import hashlib
import base64


from flexget import plugin
from flexget.config_schema import one_or_more
from flexget.event import event
from flexget.plugin import PluginWarning
from urllib import parse

plugin_name = 'feishu'
logger = logger.bind(name=plugin_name)


class FeishuNotifier:
    """
    Author: vincent806
    Date: 07Dec2021
    Description: support feishu notification for flexget
    Usage: put this file to plugin folder of flexget

    Example config:

    notify:
      entries:
        title: "{{ task }}"
        message: "{{ title }}"
        via:
          - feishu:
              webhook: your_webhook_url
              secret: your_webhook_secret
    """

    schema = {
        'type': 'object',
        'properties': {
            'webhook': {'type': 'string'},
            'secret': {'type': 'string'},
        },
        'required': ['webhook','secret'],
        'additionalProperties': False,
    }

    def notify(self, title, message, config):
        """
        Send a feishu notification
        """

        baseurl = config.get('webhook')
        secret = config.get('secret')

        # get timestamp
        ts = str(round(time.time()))
        # handle signature
        secret_enc = secret.encode("utf-8")
        string_to_sign = "{}\n{}".format(ts, secret)
        string_to_sign_enc = string_to_sign.encode("utf-8")
        hmac_code = hmac.new(string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = base64.b64encode(hmac_code).decode('utf-8')

        # format the message header
        baseurlheader = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
        }


        # format message
        json_text = {
            "timestamp": ts,
            "sign": sign,
            "msg_type": "text",
            "content": {
                "text": message
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
    plugin.register(FeishuNotifier, plugin_name, api_ver=2, interfaces=['notifiers'])
