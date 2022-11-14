class UnfriendlyException(Exception):
    def __init__(self, message):
        self.message = message
        # super().__init__(self.message)


class WhatDoYouThinkUrDoing(AssertionError):
    def __init__(self, message):
        self.message = message


try:
    raise UnfriendlyException('This is not a friendly message!')
except UnfriendlyException:
    raise WhatDoYouThinkUrDoing('A mistake was made and it doesn\'t matter who\'s fault it is')
