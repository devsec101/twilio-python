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
from twilio.rest.api.v2010.account.conference.participant import ParticipantList
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class ConferenceList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the ConferenceList
        
        :param Version version: Version that contains the resource
        :param account_sid: Contextual account_sid
        
        :returns: ConferenceList
        :rtype: ConferenceList
        """
        super(ConferenceList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
        }
        self._uri = "/Accounts/{account_sid}/Conferences.json".format(**self._kwargs)

    def read(self, date_created=values.unset, date_updated=values.unset,
             friendly_name=values.unset, status=values.unset, limit=None,
             page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            "DateCreated": serialize.iso8601_date(date_created),
            "DateUpdated": serialize.iso8601_date(date_updated),
            "FriendlyName": friendly_name,
            "Status": status,
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            ConferenceInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, date_created=values.unset, date_updated=values.unset,
             friendly_name=values.unset, status=values.unset, page_token=None,
             page_number=None, page_size=None, **kwargs):
        params = values.of({
            "DateCreated": serialize.iso8601_date(date_created),
            "DateUpdated": serialize.iso8601_date(date_updated),
            "FriendlyName": friendly_name,
            "Status": status,
            "PageToken": page_token,
            "Page": page_number,
            "PageSize": page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            ConferenceInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        """
        Constructs a ConferenceContext
        
        :param sid: Contextual sid
        
        :returns: ConferenceContext
        :rtype: ConferenceContext
        """
        return ConferenceContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ConferenceList>'


class ConferenceContext(InstanceContext):

    def __init__(self, version, account_sid, sid):
        super(ConferenceContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = "/Accounts/{account_sid}/Conferences/{sid}.json".format(**self._kwargs)
        
        # Dependents
        self._participants = None

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            ConferenceInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    @property
    def participants(self):
        if self._participants is None:
            self._participants = ParticipantList(
                self._version,
                account_sid=self._kwargs['account_sid'],
                conference_sid=self._kwargs['sid'],
            )
        return self._participants


class ConferenceInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, sid=None):
        super(ConferenceInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'api_version': payload['api_version'],
            'friendly_name': payload['friendly_name'],
            'sid': payload['sid'],
            'status': payload['status'],
            'uri': payload['uri'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'account_sid': account_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = ConferenceContext(
                self._version,
                self._context_properties['account_sid'],
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """ The date_updated """
        return self._properties['date_updated']

    @property
    def api_version(self):
        """ The api_version """
        return self._properties['api_version']

    @property
    def friendly_name(self):
        """ The friendly_name """
        return self._properties['friendly_name']

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def status(self):
        """ The status """
        return self._properties['status']

    @property
    def uri(self):
        """ The uri """
        return self._properties['uri']

    def fetch(self):
        self._context.fetch()

    @property
    def participants(self):
        return self._context.participants
