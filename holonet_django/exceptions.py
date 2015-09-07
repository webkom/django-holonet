# -*- coding: utf8 -*-


class HolonetBaseError(Exception):
    """
    All django-holonet exceptions use this as a base class.
    """
    pass


class HolonetConfigurationError(HolonetBaseError):
    """
    This exception is raised when django-holonet has a error in its configuration.
    """
    pass


class HolonetAuthenticationFailiure(HolonetBaseError):
    """
    This class is raised when the module get permission denied from the Holonet API.
    """
    pass


class HolonetRequestFailiure(HolonetBaseError):
    """
    This is raised when the API returns a non 2xx code.
    """

    def __init__(self, response):
        self.response = response

    def __str__(self):
        return "Could not complete the request to the Holonet API. Status code: {} {}, " \
               "Method: {}, URL: {}".format(self.response.status_code, self.response.reason,
                                            self.response.request.method, self.response.request.url)
