# -*- coding: utf-8 -*-


class MegaException(Exception):
    pass
    
class MegaIncorrectPasswordExcetion(MegaException):
    """
    𝙃𝙚𝙝𝙚🤪 𝙀𝙢𝙖𝙞𝙡 𝙤𝙧 𝙥𝙖𝙨𝙨𝙬𝙤𝙧𝙙 𝙞𝙨 𝙞𝙣𝙘𝙤𝙧𝙧𝙚𝙘𝙩.
    """

class MegaRequestException(MegaException):
    """
    There was an error in the request.
    """
    pass
