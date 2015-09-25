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


class ParticipantList(ListResource):

    def __init__(self, version, account_sid, conference_sid):
        """
        Initialize the ParticipantList
        
        :param Version version: Version that contains the resource
        :param account_sid: Contextual account_sid
        :param conference_sid: Contextual conference_sid
        
        :returns: ParticipantList
        :rtype: ParticipantList
        """
        super(ParticipantList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'conference_sid': conference_sid,
        }
        self._uri = "/Accounts/{account_sid}/Conferences/{conference_sid}/Participants.json".format(**self._kwargs)

    def read(self, muted=values.unset, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            "Muted": muted,
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            ParticipantInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, muted=values.unset, page_token=None, page_number=None,
             page_size=None, **kwargs):
        params = values.of({
            "Muted": muted,
            "PageToken": page_token,
            "Page": page_number,
            "PageSize": page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            ParticipantInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, call_sid):
        """
        Constructs a ParticipantContext
        
        :param call_sid: Contextual call_sid
        
        :returns: ParticipantContext
        :rtype: ParticipantContext
        """
        return ParticipantContext(self._version, call_sid=call_sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ParticipantList>'


class ParticipantContext(InstanceContext):

    def __init__(self, version, account_sid, conference_sid, call_sid):
        super(ParticipantContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'conference_sid': conference_sid,
            'call_sid': call_sid,
        }
        self._uri = "/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid}.json".format(**self._kwargs)

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            ParticipantInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, muted):
        data = values.of({
            "Muted": muted,
        })
        
        return self._version.update(
            ParticipantInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def delete(self):
        return self._version.delete("delete", self._uri)


class ParticipantInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, conference_sid,
                 call_sid=None):
        super(ParticipantInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'call_sid': payload['call_sid'],
            'conference_sid': payload['conference_sid'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'end_conference_on_exit': payload['end_conference_on_exit'],
            'muted': payload['muted'],
            'parent_sid': payload['parent_sid'],
            'sid': payload['sid'],
            'start_conference_on_enter': payload['start_conference_on_enter'],
            'uri': payload['uri'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'account_sid': account_sid,
            'conference_sid': conference_sid,
            'call_sid': call_sid or self._properties['call_sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = ParticipantContext(
                self._version,
                self._context_properties['account_sid'],
                self._context_properties['conference_sid'],
                self._context_properties['call_sid'],
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def call_sid(self):
        """ The call_sid """
        return self._properties['call_sid']

    @property
    def conference_sid(self):
        """ The conference_sid """
        return self._properties['conference_sid']

    @property
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """ The date_updated """
        return self._properties['date_updated']

    @property
    def end_conference_on_exit(self):
        """ The end_conference_on_exit """
        return self._properties['end_conference_on_exit']

    @property
    def muted(self):
        """ The muted """
        return self._properties['muted']

    @property
    def parent_sid(self):
        """ The parent_sid """
        return self._properties['parent_sid']

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def start_conference_on_enter(self):
        """ The start_conference_on_enter """
        return self._properties['start_conference_on_enter']

    @property
    def uri(self):
        """ The uri """
        return self._properties['uri']

    def fetch(self):
        self._context.fetch()

    def update(self, muted):
        self._context.update(
            muted,
        )

    def delete(self):
        self._context.delete()
