# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GeorecordsBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, latitude: float=None, longitude: float=None):  # noqa: E501
        """GeorecordsBody - a model defined in Swagger

        :param latitude: The latitude of this GeorecordsBody.  # noqa: E501
        :type latitude: float
        :param longitude: The longitude of this GeorecordsBody.  # noqa: E501
        :type longitude: float
        """
        self.swagger_types = {
            'latitude': float,
            'longitude': float
        }

        self.attribute_map = {
            'latitude': 'latitude',
            'longitude': 'longitude'
        }
        self._latitude = latitude
        self._longitude = longitude

    @classmethod
    def from_dict(cls, dikt) -> 'GeorecordsBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The georecords_body of this GeorecordsBody.  # noqa: E501
        :rtype: GeorecordsBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def latitude(self) -> float:
        """Gets the latitude of this GeorecordsBody.

        Latitude of the current location.  # noqa: E501

        :return: The latitude of this GeorecordsBody.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float):
        """Sets the latitude of this GeorecordsBody.

        Latitude of the current location.  # noqa: E501

        :param latitude: The latitude of this GeorecordsBody.
        :type latitude: float
        """

        self._latitude = latitude

    @property
    def longitude(self) -> float:
        """Gets the longitude of this GeorecordsBody.

        Longitude of the current location.  # noqa: E501

        :return: The longitude of this GeorecordsBody.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float):
        """Sets the longitude of this GeorecordsBody.

        Longitude of the current location.  # noqa: E501

        :param longitude: The longitude of this GeorecordsBody.
        :type longitude: float
        """

        self._longitude = longitude
