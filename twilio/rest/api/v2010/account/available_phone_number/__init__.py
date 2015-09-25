# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest.api.v2010.account.available_phone_number.local import LocalList
from twilio.rest.api.v2010.account.available_phone_number.mobile import MobileList
from twilio.rest.api.v2010.account.available_phone_number.toll_free import TollFreeList
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class AvailablePhoneNumberCountryList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the AvailablePhoneNumberCountryList
        
        :param Version version: Version that contains the resource
        :param account_sid: Contextual account_sid
        
        :returns: AvailablePhoneNumberCountryList
        :rtype: AvailablePhoneNumberCountryList
        """
        super(AvailablePhoneNumberCountryList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
        }
        self._uri = "/Accounts/{account_sid}/AvailablePhoneNumbers.json".format(**self._kwargs)

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            AvailablePhoneNumberCountryInstance,
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
            AvailablePhoneNumberCountryInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, country_code):
        """
        Constructs a AvailablePhoneNumberCountryContext
        
        :param country_code: Contextual country_code
        
        :returns: AvailablePhoneNumberCountryContext
        :rtype: AvailablePhoneNumberCountryContext
        """
        return AvailablePhoneNumberCountryContext(self._version, country_code=country_code, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AvailablePhoneNumberCountryList>'


class AvailablePhoneNumberCountryContext(InstanceContext):

    def __init__(self, version, account_sid, country_code):
        super(AvailablePhoneNumberCountryContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'country_code': country_code,
        }
        self._uri = "/Accounts/{account_sid}/AvailablePhoneNumbers/{country_code}.json".format(**self._kwargs)
        
        # Dependents
        self._local = None
        self._toll_free = None
        self._mobile = None

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            AvailablePhoneNumberCountryInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    @property
    def local(self):
        if self._local is None:
            self._local = LocalList(
                self._version,
                country_code=self._kwargs['country_code'],
            )
        return self._local

    @property
    def toll_free(self):
        if self._toll_free is None:
            self._toll_free = TollFreeList(
                self._version,
                country_code=self._kwargs['country_code'],
            )
        return self._toll_free

    @property
    def mobile(self):
        if self._mobile is None:
            self._mobile = MobileList(
                self._version,
                country_code=self._kwargs['country_code'],
            )
        return self._mobile


class AvailablePhoneNumberCountryInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, country_code=None):
        super(AvailablePhoneNumberCountryInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'country_code': payload['country_code'],
            'country': payload['country'],
            'uri': payload['uri'],
            'beta': payload['beta'],
            'subresource_uris': payload['subresource_uris'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'account_sid': account_sid,
            'country_code': country_code or self._properties['country_code'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = AvailablePhoneNumberCountryContext(
                self._version,
                self._context_properties['account_sid'],
                self._context_properties['country_code'],
            )
        return self._lazy_context

    @property
    def country_code(self):
        """ The country_code """
        return self._properties['country_code']

    @property
    def country(self):
        """ The country """
        return self._properties['country']

    @property
    def uri(self):
        """ The uri """
        return self._properties['uri']

    @property
    def beta(self):
        """ The beta """
        return self._properties['beta']

    @property
    def subresource_uris(self):
        """ The subresource_uris """
        return self._properties['subresource_uris']

    def fetch(self):
        self._context.fetch()

    @property
    def local(self):
        return self._context.local

    @property
    def toll_free(self):
        return self._context.toll_free

    @property
    def mobile(self):
        return self._context.mobile
