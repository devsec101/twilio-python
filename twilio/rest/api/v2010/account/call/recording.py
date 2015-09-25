# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest import serialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class RecordingList(ListResource):

    def __init__(self, version, account_sid, call_sid):
        """
        Initialize the RecordingList
        
        :param Version version: Version that contains the resource
        :param account_sid: Contextual account_sid
        :param call_sid: Contextual call_sid
        
        :returns: RecordingList
        :rtype: RecordingList
        """
        super(RecordingList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'call_sid': call_sid,
        }
        self._uri = "/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json".format(**self._kwargs)

    def read(self, date_created=values.unset, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            "DateCreated": serialize.iso8601_date(date_created),
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            RecordingInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, date_created=values.unset, page_token=None, page_number=None,
             page_size=None, **kwargs):
        params = values.of({
            "DateCreated": serialize.iso8601_date(date_created),
            "PageToken": page_token,
            "Page": page_number,
            "PageSize": page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            RecordingInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        """
        Constructs a RecordingContext
        
        :param sid: Contextual sid
        
        :returns: RecordingContext
        :rtype: RecordingContext
        """
        return RecordingContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.RecordingList>'


class RecordingContext(InstanceContext):

    def __init__(self, version, account_sid, call_sid, sid):
        super(RecordingContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'call_sid': call_sid,
            'sid': sid,
        }
        self._uri = "/Accounts/{account_sid}/Calls/{call_sid}/Recordings/{sid}.json".format(**self._kwargs)

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            RecordingInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def delete(self):
        return self._version.delete("delete", self._uri)


class RecordingInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, call_sid, sid=None):
        super(RecordingInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'api_version': payload['api_version'],
            'call_sid': payload['call_sid'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'duration': payload['duration'],
            'sid': payload['sid'],
            'uri': payload['uri'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'account_sid': account_sid,
            'call_sid': call_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = RecordingContext(
                self._version,
                self._context_properties['account_sid'],
                self._context_properties['call_sid'],
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def api_version(self):
        """ The api_version """
        return self._properties['api_version']

    @property
    def call_sid(self):
        """ The call_sid """
        return self._properties['call_sid']

    @property
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """ The date_updated """
        return self._properties['date_updated']

    @property
    def duration(self):
        """ The duration """
        return self._properties['duration']

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def uri(self):
        """ The uri """
        return self._properties['uri']

    def fetch(self):
        self._context.fetch()

    def delete(self):
        self._context.delete()
