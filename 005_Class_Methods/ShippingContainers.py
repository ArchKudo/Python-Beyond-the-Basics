#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 08:11:18 2017

@author: ArchKudo
"""

import iso6346


class ShippingContainer:
    '''The ShippingContainer base class'''
    serial = 0  # A class variable

    HEIGHT_FT = 100
    WIDTH_FT = 100

    @staticmethod
    def _make_bic_code(owner, serial):
        # [owner] + [category] + [serial no.] + [check]
        return iso6346.create(owner_code=owner, serial=str(serial).zfill(6))

    @classmethod
    def _get_serial(cls):
        # Add class as argument
        result = cls.serial
        cls.serial += 1
        return result

    @classmethod
    def create_empty(cls, owner, *args, **kwargs):
        '''To accomodate extra args of child class'''
        return cls(owner, contents=None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner, contents, *args, **kwargs):
        '''To accomodate extra args of child class'''
        return cls(owner, contents, *args, **kwargs)

    def __init__(self, owner, contents, length_ft):
        self.contents = contents
        self.length_ft = length_ft
        # Static methods can change instance and not the class object and hence,
        # the self._make_bic_code instead of ShippingContainer._make_bic_code
        self.bic_code = self._make_bic_code(
            owner=owner, serial=ShippingContainer._get_serial())

    def _calc_volume(self):
        # The real volume function which needs to be overrided in child class
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft

    @property
    def volume_ft3(self):
        '''Calls _calc_volume to calculate volume'''
        return self._calc_volume()


class RefrigeratedShippingContainer(ShippingContainer):
    '''Shipping container class with temperature control'''

    MAX_TEMP = 4.0
    FRIDGE_VOLUME = 100

    @staticmethod
    def _f_to_c(fahrenheit):
        # Convert fahrenheit to celsius
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def _c_to_f(celsius):
        # Convert celsius to fahrenheit
        return (celsius) * 9 / 5 + 32

    @staticmethod
    def _make_bic_code(owner, serial):
        # Category R for refrigerated
        return iso6346.create(owner_code=owner, serial=str(serial).zfill(6), category='R')

    def __init__(self, owner, contents, length_ft, celsius):
        # To get init method of parent
        super().__init__(owner, contents, length_ft)
        # Equivalent to self._celsius = celsius with celsius.setter checks
        self._celsius = None
        self.celsius = celsius

    @property
    def celsius(self):
        '''Check Temperature '''
        return self._celsius

    def _set_celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_TEMP:
            raise ValueError('Temperature can\'t be greater than 4°C')
        self._celsius = value

    @celsius.setter
    def celsius(self, value):
        return self._set_celsius(value)

    @property
    def fahrenheit(self):
        '''Easy fahrenheit setting'''
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)

    def _calc_volume(self):
        return super()._calc_volume() - RefrigeratedShippingContainer.FRIDGE_VOLUME


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):
    '''RefrigeratedShippingContainer class with bounded temperature control'''
    MIN_CELSIUS = -20.0

    def _set_celsius(self, value):
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError('Temperature too cold < {}'.format(
                HeatedRefrigeratedShippingContainer.MIN_CELSIUS))
        return super()._set_celsius(value)
