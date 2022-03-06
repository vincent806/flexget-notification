from urllib import request
from loguru import logger
import ssl
import urllib.error


from flexget import plugin
from flexget.config_schema import one_or_more
from flexget.event import event
from flexget.plugin import PluginWarning
from urllib import parse

plugin_name = 'pushplus'
logger = logger.bind(name=plugin_name)


class PushplusNotifier:
    """
    Author: vincent806
    Date: 07Dec2021
    Description: support pushplus notification for flexget - https://www.pushplus.plus
    Usage: put this file to plugin folder of flexget

    Example config:

    notify:
      entries:
        title: "{{ task }}"
        message: "{{ title }}"
        via:
          - pushplus:
              token: your_pushplus_token

    """

    schema = {
        'type': 'object',
        'properties': {
            'token': {'type': 'string'},
        },
        'required': ['token'],
        'additionalProperties': False,
    }

    def notify(self, title, message, config):
        """
        Send a pushplus notification
        """
        token = config.get('token')
        baseurl = "http://www.pushplus.plus/send?token=" + token

        
        pushplus_url = baseurl + "&title=" + parse.quote_plus(title) + "&content=" + parse.quote_plus(message)

        # handle SSL certification error
        ssl._create_default_https_context = ssl._create_unverified_context

        try:
            response = request.urlopen(pushplus_url)
        except urllib.error.HTTPError as e:
            print(e.__dict__)
        except urllib.error.URLError as e:
            print(e.__dict__)


@event('plugin.register')
def register_plugin():
    plugin.register(PushplusNotifier, plugin_name, api_ver=2, interfaces=['notifiers'])
