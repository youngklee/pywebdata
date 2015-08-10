class Output(object):
    def __init__(self, iotype, f_parse=lambda x:x):
        self.iotype = iotype
        self.value = None
        self.f_parse = f_parse

class Input(object):

    def __init__(self, iotype, required=True, min=None, max=None, default=None, inc=None):
        self.iotype = iotype
        self.is_required = required
        self._min = min
        self._max = max
        self._default = default
        self._inc = inc
        self.value = None

    def update(self, value):
        self.value = value

    def set_increment(self, inc):
        self._inc = inc