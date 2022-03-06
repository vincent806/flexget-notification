
from urllib import request
from loguru import logger
import ssl
import urllib.error


from flexget import plugin
from flexget.config_schema import one_or_more
from flexget.event import event
from flexget.plugin import PluginWarning
from urllib import parse

plugin_name = 'serverchan'
logger = logger.bind(name=plugin_name)


class serverchanNotifier:
    """
    Author: vincent806
    Date: 07Dec2021
    Description: support serverchan notification for flexget
    Usage: put this file to plugin folder of flexget

    Example config:

    notify:
      entries:
        title: "{{ task }}"
        message: "{{ title }}"
        via:
          - serverchan:
              sckey: your_serverchan_sckey

    """

    schema = {
        'type': 'object',
        'properties': {
            'sckey': {'type': 'string'},
        },
        'required': ['sckey'],
        'additionalProperties': False,
    }

    def notify(self, title, message, config):
        """
        Send a serverchan notification
        """
        sckey = config.get('sckey')
        if sckey.startswith("SCU"):
            baseurl = "https://sc.ftqq.com/" + sckey + ".send"
        else:
            baseurl = "https://sctapi.ftqq.com/" + sckey + ".send"

        title_tuned = title
        #serverchan - maximum message title length is 32 
        if(len(title)>32):
            title_tuned = title[0:32]
        #serverchan - title is mandatory field - if title is not provided, then post a default value 'Subject is not specified.'
        if(len(title)==0):
            title_tuned = "Subject is not specified."
        
        serverchan_url = baseurl + "?text=" + parse.quote_plus(title_tuned) + "&desp=" + parse.quote_plus(message)

        # handle SSL certification error
        ssl._create_default_https_context = ssl._create_unverified_context

        try:
            response = request.urlopen(serverchan_url)
        except urllib.error.HTTPError as e:
            print(e.__dict__)
        except urllib.error.URLError as e:
            print(e.__dict__)


@event('plugin.register')
def register_plugin():
    plugin.register(serverchanNotifier, plugin_name, api_ver=2, interfaces=['notifiers'])
