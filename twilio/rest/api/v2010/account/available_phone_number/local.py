# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class LocalList(ListResource):

    def __init__(self, version, account_sid, country_code):
        """
        Initialize the LocalList
        
        :param Version version: Version that contains the resource
        :param account_sid: Contextual account_sid
        :param country_code: Contextual country_code
        
        :returns: LocalList
        :rtype: LocalList
        """
        super(LocalList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'country_code': country_code,
        }
        self._uri = "/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}/Local.json".format(**self._kwargs)

    def read(self, number_type, beta=values.unset, limit=None, page_size=None,
             **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            "NumberType": number_type,
            "Beta": beta,
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            LocalInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, number_type, beta=values.unset, page_token=None,
             page_number=None, page_size=None, **kwargs):
        params = values.of({
            "NumberType": number_type,
            "Beta": beta,
            "PageToken": page_token,
            "Page": page_number,
            "PageSize": page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            LocalInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self):
        """
        Constructs a LocalContext
        
        :returns: LocalContext
        :rtype: LocalContext
        """
        return LocalContext(self._version, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.LocalList>'


class LocalContext(InstanceContext):

    def __init__(self, version):
        super(LocalContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {}
        self._uri = "None".format(**self._kwargs)


class LocalInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, country_code):
        super(LocalInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'friendly_name': payload['friendly_name'],
            'phone_number': payload['phone_number'],
            'lata': payload['lata'],
            'rate_center': payload['rate_center'],
            'latitude': payload['latitude'],
            'longitude': payload['longitude'],
            'region': payload['region'],
            'postal_code': payload['postal_code'],
            'iso_country': payload['iso_country'],
            'address_requirements': payload['address_requirements'],
            'beta': payload['beta'],
            'capabilities': payload['capabilities'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'account_sid': account_sid,
            'country_code': country_code,
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = LocalContext(
                self._version,
            )
        return self._lazy_context

    @property
    def friendly_name(self):
        """ The friendly_name """
        return self._properties['friendly_name']

    @property
    def phone_number(self):
        """ The phone_number """
        return self._properties['phone_number']

    @property
    def lata(self):
        """ The lata """
        return self._properties['lata']

    @property
    def rate_center(self):
        """ The rate_center """
        return self._properties['rate_center']

    @property
    def latitude(self):
        """ The latitude """
        return self._properties['latitude']

    @property
    def longitude(self):
        """ The longitude """
        return self._properties['longitude']

    @property
    def region(self):
        """ The region """
        return self._properties['region']

    @property
    def postal_code(self):
        """ The postal_code """
        return self._properties['postal_code']

    @property
    def iso_country(self):
        """ The iso_country """
        return self._properties['iso_country']

    @property
    def address_requirements(self):
        """ The address_requirements """
        return self._properties['address_requirements']

    @property
    def beta(self):
        """ The beta """
        return self._properties['beta']

    @property
    def capabilities(self):
        """ The capabilities """
        return self._properties['capabilities']
