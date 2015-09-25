# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class CredentialListList(ListResource):

    def __init__(self, version, trunk_sid):
        """
        Initialize the CredentialListList
        
        :param Version version: Version that contains the resource
        :param trunk_sid: Contextual trunk_sid
        
        :returns: CredentialListList
        :rtype: CredentialListList
        """
        super(CredentialListList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'trunk_sid': trunk_sid,
        }
        self._uri = "/Trunks/{trunk_sid}/CredentialLists".format(**self._kwargs)

    def create(self, credential_list_sid):
        data = values.of({
            "CredentialListSid": credential_list_sid,
        })
        
        return self._version.create(
            CredentialListInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            CredentialListInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, page_token=None, page_number=None, page_size=None, **kwargs):
        params = values.of({
            "PageToken": page_token,
            "Page": page_number,
            "PageSize": page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            CredentialListInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        """
        Constructs a CredentialListContext
        
        :param sid: Contextual sid
        
        :returns: CredentialListContext
        :rtype: CredentialListContext
        """
        return CredentialListContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1.CredentialListList>'


class CredentialListContext(InstanceContext):

    def __init__(self, version, trunk_sid, sid):
        super(CredentialListContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'trunk_sid': trunk_sid,
            'sid': sid,
        }
        self._uri = "/Trunks/{trunk_sid}/CredentialLists/{sid}".format(**self._kwargs)

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            CredentialListInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def delete(self):
        return self._version.delete("delete", self._uri)


class CredentialListInstance(InstanceResource):

    def __init__(self, version, payload, trunk_sid, sid=None):
        super(CredentialListInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'sid': payload['sid'],
            'trunk_sid': payload['trunk_sid'],
            'friendly_name': payload['friendly_name'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'url': payload['url'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'trunk_sid': trunk_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = CredentialListContext(
                self._version,
                self._context_properties['trunk_sid'],
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def trunk_sid(self):
        """ The trunk_sid """
        return self._properties['trunk_sid']

    @property
    def friendly_name(self):
        """ The friendly_name """
        return self._properties['friendly_name']

    @property
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """ The date_updated """
        return self._properties['date_updated']

    @property
    def url(self):
        """ The url """
        return self._properties['url']

    def fetch(self):
        self._context.fetch()

    def delete(self):
        self._context.delete()
