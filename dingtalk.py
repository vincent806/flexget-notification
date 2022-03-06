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

plugin_name = 'dingtalk'
logger = logger.bind(name=plugin_name)


class DingTalkNotifier:
    """
    Author: vincent806
    Date: 07Dec2021
    Description: support dingtalk notification for flexget
    Usage: put this file to plugin folder of flexget

    Example config:

    notify:
      entries:
        title: "{{ task }}"
        message: "{{ title }}"
        via:
          - dingtalk:
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
        Send a dingtalk notification
        """

        baseurl = config.get('webhook')
        secret = config.get('secret')

        # get timestamp
        ts = str(round(time.time() * 1000))
        # handle signature
        secret_enc = secret.encode("utf-8")
        string_to_sign = "{}\n{}".format(ts, secret)
        string_to_sign_enc = string_to_sign.encode("utf-8")
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = parse.quote_plus(base64.b64encode(hmac_code))

        # push signature as part of url, and format the message header
        baseurl = baseurl + "&timestamp={}&sign={}".format(ts, sign)
        baseurlheader = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
        }

        # format message
        if (len(title)==0):
            title = "Subject is not specified."
        json_text = {
            "msgtype": "markdown",
            "markdown": {
            "title": title,
            "text": message
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
    plugin.register(DingTalkNotifier, plugin_name, api_ver=2, interfaces=['notifiers'])
