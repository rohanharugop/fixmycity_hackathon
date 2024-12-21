import connexion
import six

from swagger_server.models.georecords_body import GeorecordsBody  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def geo_records_post(body):  # noqa: E501
    """Send current geo-coordinates and receive records.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: List[InlineResponse200]
    """
    if connexion.request.is_json:
        body = GeorecordsBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
