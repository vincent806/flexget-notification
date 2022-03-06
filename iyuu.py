
from urllib import request
from loguru import logger
import ssl
import urllib.error


from flexget import plugin
from flexget.config_schema import one_or_more
from flexget.event import event
from flexget.plugin import PluginWarning
from urllib import parse

plugin_name = 'iyuu'
logger = logger.bind(name=plugin_name)


class iyuuNotifier:
    """
    Author: vincent806
    Date: 05Dec2021
    Description: support iyuu notification for flexget
    Usage: put this file to plugin folder of flexget

    Example config:

    notify:
      entries:
        title: "{{ task }}"
        message: "{{ title }}"
        via:
          - iyuu:
              token: youriyuutoken

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
        Send a iyuu notification
        """

        baseurl = "https://iyuu.cn/" + config.get('token') + ".send"
        if(len(title)>0):
            iyuu_url = baseurl + "?text=" + parse.quote_plus(title) + "&desp=" + parse.quote_plus(message)
        else:
            iyuu_url = baseurl + "?text=" + parse.quote_plus(message)

        # handle SSL certification error
        ssl._create_default_https_context = ssl._create_unverified_context

        try:
            response = request.urlopen(iyuu_url)
        except urllib.error.HTTPError as e:
            print(e.__dict__)
        except urllib.error.URLError as e:
            print(e.__dict__)


@event('plugin.register')
def register_plugin():
    plugin.register(iyuuNotifier, plugin_name, api_ver=2, interfaces=['notifiers'])
