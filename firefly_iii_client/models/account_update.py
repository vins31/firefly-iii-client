# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API  # noqa: E501

    OpenAPI spec version: 0.9.0
    Contact: thegrumpydictator@gmail.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AccountUpdate(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'account_number': 'str',
        'account_role': 'str',
        'active': 'bool',
        'bic': 'str',
        'credit_card_type': 'str',
        'currency_code': 'str',
        'currency_id': 'int',
        'iban': 'str',
        'include_net_worth': 'bool',
        'interest': 'float',
        'interest_period': 'str',
        'liability_amount': 'float',
        'liability_start_date': 'date',
        'liability_type': 'str',
        'monthly_payment_date': 'date',
        'name': 'str',
        'notes': 'str',
        'opening_balance': 'float',
        'opening_balance_date': 'date',
        'type': 'str',
        'virtual_balance': 'float'
    }

    attribute_map = {
        'account_number': 'account_number',
        'account_role': 'account_role',
        'active': 'active',
        'bic': 'bic',
        'credit_card_type': 'credit_card_type',
        'currency_code': 'currency_code',
        'currency_id': 'currency_id',
        'iban': 'iban',
        'include_net_worth': 'include_net_worth',
        'interest': 'interest',
        'interest_period': 'interest_period',
        'liability_amount': 'liability_amount',
        'liability_start_date': 'liability_start_date',
        'liability_type': 'liability_type',
        'monthly_payment_date': 'monthly_payment_date',
        'name': 'name',
        'notes': 'notes',
        'opening_balance': 'opening_balance',
        'opening_balance_date': 'opening_balance_date',
        'type': 'type',
        'virtual_balance': 'virtual_balance'
    }

    def __init__(self, account_number=None, account_role=None, active=None, bic=None, credit_card_type=None, currency_code=None, currency_id=None, iban=None, include_net_worth=None, interest=None, interest_period=None, liability_amount=None, liability_start_date=None, liability_type=None, monthly_payment_date=None, name=None, notes=None, opening_balance=None, opening_balance_date=None, type=None, virtual_balance=None):  # noqa: E501
        """AccountUpdate - a model defined in OpenAPI"""  # noqa: E501

        self._account_number = None
        self._account_role = None
        self._active = None
        self._bic = None
        self._credit_card_type = None
        self._currency_code = None
        self._currency_id = None
        self._iban = None
        self._include_net_worth = None
        self._interest = None
        self._interest_period = None
        self._liability_amount = None
        self._liability_start_date = None
        self._liability_type = None
        self._monthly_payment_date = None
        self._name = None
        self._notes = None
        self._opening_balance = None
        self._opening_balance_date = None
        self._type = None
        self._virtual_balance = None
        self.discriminator = None

        if account_number is not None:
            self.account_number = account_number
        self.account_role = account_role
        if active is not None:
            self.active = active
        if bic is not None:
            self.bic = bic
        self.credit_card_type = credit_card_type
        if currency_code is not None:
            self.currency_code = currency_code
        if currency_id is not None:
            self.currency_id = currency_id
        if iban is not None:
            self.iban = iban
        if include_net_worth is not None:
            self.include_net_worth = include_net_worth
        self.interest = interest
        self.interest_period = interest_period
        self.liability_amount = liability_amount
        self.liability_start_date = liability_start_date
        self.liability_type = liability_type
        self.monthly_payment_date = monthly_payment_date
        self.name = name
        if notes is not None:
            self.notes = notes
        if opening_balance is not None:
            self.opening_balance = opening_balance
        if opening_balance_date is not None:
            self.opening_balance_date = opening_balance_date
        self.type = type
        if virtual_balance is not None:
            self.virtual_balance = virtual_balance

    @property
    def account_number(self):
        """Gets the account_number of this AccountUpdate.  # noqa: E501


        :return: The account_number of this AccountUpdate.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this AccountUpdate.


        :param account_number: The account_number of this AccountUpdate.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def account_role(self):
        """Gets the account_role of this AccountUpdate.  # noqa: E501

        Is only mandatory when the type is asset.  # noqa: E501

        :return: The account_role of this AccountUpdate.  # noqa: E501
        :rtype: str
        """
        return self._account_role

    @account_role.setter
    def account_role(self, account_role):
        """Sets the account_role of this AccountUpdate.

        Is only mandatory when the type is asset.  # noqa: E501

        :param account_role: The account_role of this AccountUpdate.  # noqa: E501
        :type: str
        """
        if account_role is None:
            raise ValueError("Invalid value for `account_role`, must not be `None`")  # noqa: E501
        allowed_values = ["defaultAsset", "sharedAsset", "savingAsset", "ccAsset", "cashWalletAsset"]  # noqa: E501
        if account_role not in allowed_values:
            raise ValueError(
                "Invalid value for `account_role` ({0}), must be one of {1}"  # noqa: E501
                .format(account_role, allowed_values)
            )

        self._account_role = account_role

    @property
    def active(self):
        """Gets the active of this AccountUpdate.  # noqa: E501

        If omitted, defaults to true.  # noqa: E501

        :return: The active of this AccountUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this AccountUpdate.

        If omitted, defaults to true.  # noqa: E501

        :param active: The active of this AccountUpdate.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def bic(self):
        """Gets the bic of this AccountUpdate.  # noqa: E501


        :return: The bic of this AccountUpdate.  # noqa: E501
        :rtype: str
        """
        return self._bic

    @bic.setter
    def bic(self, bic):
        """Sets the bic of this AccountUpdate.


        :param bic: The bic of this AccountUpdate.  # noqa: E501
        :type: str
        """

        self._bic = bic

    @property
    def credit_card_type(self):
        """Gets the credit_card_type of this AccountUpdate.  # noqa: E501

        Mandatory when the account_role is ccAsset. Can only be monthlyFull.  # noqa: E501

        :return: The credit_card_type of this AccountUpdate.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_type

    @credit_card_type.setter
    def credit_card_type(self, credit_card_type):
        """Sets the credit_card_type of this AccountUpdate.

        Mandatory when the account_role is ccAsset. Can only be monthlyFull.  # noqa: E501

        :param credit_card_type: The credit_card_type of this AccountUpdate.  # noqa: E501
        :type: str
        """
        allowed_values = ["monthlyFull"]  # noqa: E501
        if credit_card_type not in allowed_values:
            raise ValueError(
                "Invalid value for `credit_card_type` ({0}), must be one of {1}"  # noqa: E501
                .format(credit_card_type, allowed_values)
            )

        self._credit_card_type = credit_card_type

    @property
    def currency_code(self):
        """Gets the currency_code of this AccountUpdate.  # noqa: E501

        Use either currency_id or currency_code. Defaults to the user's default currency.  # noqa: E501

        :return: The currency_code of this AccountUpdate.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this AccountUpdate.

        Use either currency_id or currency_code. Defaults to the user's default currency.  # noqa: E501

        :param currency_code: The currency_code of this AccountUpdate.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def currency_id(self):
        """Gets the currency_id of this AccountUpdate.  # noqa: E501

        Use either currency_id or currency_code. Defaults to the user's default currency.  # noqa: E501

        :return: The currency_id of this AccountUpdate.  # noqa: E501
        :rtype: int
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this AccountUpdate.

        Use either currency_id or currency_code. Defaults to the user's default currency.  # noqa: E501

        :param currency_id: The currency_id of this AccountUpdate.  # noqa: E501
        :type: int
        """

        self._currency_id = currency_id

    @property
    def iban(self):
        """Gets the iban of this AccountUpdate.  # noqa: E501


        :return: The iban of this AccountUpdate.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this AccountUpdate.


        :param iban: The iban of this AccountUpdate.  # noqa: E501
        :type: str
        """

        self._iban = iban

    @property
    def include_net_worth(self):
        """Gets the include_net_worth of this AccountUpdate.  # noqa: E501

        If omitted, defaults to true.  # noqa: E501

        :return: The include_net_worth of this AccountUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._include_net_worth

    @include_net_worth.setter
    def include_net_worth(self, include_net_worth):
        """Sets the include_net_worth of this AccountUpdate.

        If omitted, defaults to true.  # noqa: E501

        :param include_net_worth: The include_net_worth of this AccountUpdate.  # noqa: E501
        :type: bool
        """

        self._include_net_worth = include_net_worth

    @property
    def interest(self):
        """Gets the interest of this AccountUpdate.  # noqa: E501

        Mandatory when type is liability. Interest percentage.  # noqa: E501

        :return: The interest of this AccountUpdate.  # noqa: E501
        :rtype: float
        """
        return self._interest

    @interest.setter
    def interest(self, interest):
        """Sets the interest of this AccountUpdate.

        Mandatory when type is liability. Interest percentage.  # noqa: E501

        :param interest: The interest of this AccountUpdate.  # noqa: E501
        :type: float
        """
        if interest is None:
            raise ValueError("Invalid value for `interest`, must not be `None`")  # noqa: E501

        self._interest = interest

    @property
    def interest_period(self):
        """Gets the interest_period of this AccountUpdate.  # noqa: E501

        Mandatory when type is liability. Period over which the interest is calculated.  # noqa: E501

        :return: The interest_period of this AccountUpdate.  # noqa: E501
        :rtype: str
        """
        return self._interest_period

    @interest_period.setter
    def interest_period(self, interest_period):
        """Sets the interest_period of this AccountUpdate.

        Mandatory when type is liability. Period over which the interest is calculated.  # noqa: E501

        :param interest_period: The interest_period of this AccountUpdate.  # noqa: E501
        :type: str
        """
        if interest_period is None:
            raise ValueError("Invalid value for `interest_period`, must not be `None`")  # noqa: E501

        self._interest_period = interest_period

    @property
    def liability_amount(self):
        """Gets the liability_amount of this AccountUpdate.  # noqa: E501

        Mandatory when type is liability. Amount of money in the liability. Must be positive.  # noqa: E501

        :return: The liability_amount of this AccountUpdate.  # noqa: E501
        :rtype: float
        """
        return self._liability_amount

    @liability_amount.setter
    def liability_amount(self, liability_amount):
        """Sets the liability_amount of this AccountUpdate.

        Mandatory when type is liability. Amount of money in the liability. Must be positive.  # noqa: E501

        :param liability_amount: The liability_amount of this AccountUpdate.  # noqa: E501
        :type: float
        """
        if liability_amount is None:
            raise ValueError("Invalid value for `liability_amount`, must not be `None`")  # noqa: E501

        self._liability_amount = liability_amount

    @property
    def liability_start_date(self):
        """Gets the liability_start_date of this AccountUpdate.  # noqa: E501

        Mandatory when type is liability. Start date for the liability.  # noqa: E501

        :return: The liability_start_date of this AccountUpdate.  # noqa: E501
        :rtype: date
        """
        return self._liability_start_date

    @liability_start_date.setter
    def liability_start_date(self, liability_start_date):
        """Sets the liability_start_date of this AccountUpdate.

        Mandatory when type is liability. Start date for the liability.  # noqa: E501

        :param liability_start_date: The liability_start_date of this AccountUpdate.  # noqa: E501
        :type: date
        """
        if liability_start_date is None:
            raise ValueError("Invalid value for `liability_start_date`, must not be `None`")  # noqa: E501

        self._liability_start_date = liability_start_date

    @property
    def liability_type(self):
        """Gets the liability_type of this AccountUpdate.  # noqa: E501

        Mandatory when type is liability. Specifies the exact type.  # noqa: E501

        :return: The liability_type of this AccountUpdate.  # noqa: E501
        :rtype: str
        """
        return self._liability_type

    @liability_type.setter
    def liability_type(self, liability_type):
        """Sets the liability_type of this AccountUpdate.

        Mandatory when type is liability. Specifies the exact type.  # noqa: E501

        :param liability_type: The liability_type of this AccountUpdate.  # noqa: E501
        :type: str
        """
        if liability_type is None:
            raise ValueError("Invalid value for `liability_type`, must not be `None`")  # noqa: E501
        allowed_values = ["loan", "debt", "mortgage"]  # noqa: E501
        if liability_type not in allowed_values:
            raise ValueError(
                "Invalid value for `liability_type` ({0}), must be one of {1}"  # noqa: E501
                .format(liability_type, allowed_values)
            )

        self._liability_type = liability_type

    @property
    def monthly_payment_date(self):
        """Gets the monthly_payment_date of this AccountUpdate.  # noqa: E501

        Mandatory when the account_role is ccAsset. Moment at which CC payment installments are asked for by the bank.  # noqa: E501

        :return: The monthly_payment_date of this AccountUpdate.  # noqa: E501
        :rtype: date
        """
        return self._monthly_payment_date

    @monthly_payment_date.setter
    def monthly_payment_date(self, monthly_payment_date):
        """Sets the monthly_payment_date of this AccountUpdate.

        Mandatory when the account_role is ccAsset. Moment at which CC payment installments are asked for by the bank.  # noqa: E501

        :param monthly_payment_date: The monthly_payment_date of this AccountUpdate.  # noqa: E501
        :type: date
        """

        self._monthly_payment_date = monthly_payment_date

    @property
    def name(self):
        """Gets the name of this AccountUpdate.  # noqa: E501


        :return: The name of this AccountUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountUpdate.


        :param name: The name of this AccountUpdate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def notes(self):
        """Gets the notes of this AccountUpdate.  # noqa: E501


        :return: The notes of this AccountUpdate.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this AccountUpdate.


        :param notes: The notes of this AccountUpdate.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def opening_balance(self):
        """Gets the opening_balance of this AccountUpdate.  # noqa: E501


        :return: The opening_balance of this AccountUpdate.  # noqa: E501
        :rtype: float
        """
        return self._opening_balance

    @opening_balance.setter
    def opening_balance(self, opening_balance):
        """Sets the opening_balance of this AccountUpdate.


        :param opening_balance: The opening_balance of this AccountUpdate.  # noqa: E501
        :type: float
        """

        self._opening_balance = opening_balance

    @property
    def opening_balance_date(self):
        """Gets the opening_balance_date of this AccountUpdate.  # noqa: E501


        :return: The opening_balance_date of this AccountUpdate.  # noqa: E501
        :rtype: date
        """
        return self._opening_balance_date

    @opening_balance_date.setter
    def opening_balance_date(self, opening_balance_date):
        """Sets the opening_balance_date of this AccountUpdate.


        :param opening_balance_date: The opening_balance_date of this AccountUpdate.  # noqa: E501
        :type: date
        """

        self._opening_balance_date = opening_balance_date

    @property
    def type(self):
        """Gets the type of this AccountUpdate.  # noqa: E501

        Can only be one one these four account types.  # noqa: E501

        :return: The type of this AccountUpdate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccountUpdate.

        Can only be one one these four account types.  # noqa: E501

        :param type: The type of this AccountUpdate.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["asset", "expense", "revenue", "liability", "liabilities"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def virtual_balance(self):
        """Gets the virtual_balance of this AccountUpdate.  # noqa: E501


        :return: The virtual_balance of this AccountUpdate.  # noqa: E501
        :rtype: float
        """
        return self._virtual_balance

    @virtual_balance.setter
    def virtual_balance(self, virtual_balance):
        """Sets the virtual_balance of this AccountUpdate.


        :param virtual_balance: The virtual_balance of this AccountUpdate.  # noqa: E501
        :type: float
        """

        self._virtual_balance = virtual_balance

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AccountUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
