class ChristmasPresents:
    def __init__(self, mum=None, dad=None, sis=None, oana=None):
        if oana is None:
            oana = []
        if sis is None:
            sis = []
        if dad is None:
            dad = []
        if mum is None:
            mum = []
        self.mum = mum
        self.dad = dad
        self.sis = sis
        self.oana = oana

# -------------------------------------------------------------

    def m_show(self):
        return self.mum

    def m_set(self, value):
        self.mum.append(value)

    def m_del(self):
        self.mum = []

    mum_presents = property(m_show, m_set, m_del)

# -------------------------------------------------------------

    def f_show(self):
        return self.dad

    def f_set(self, value):
        self.dad.append(value)

    def f_del(self):
        self.dad = []

    dad_presents = property(f_show, f_set, f_del)

# -------------------------------------------------------------

    def s_show(self):
        return self.sis

    def s_set(self, value):
        self.sis.append(value)

    def s_del(self):
        self.sis = []

    sis_presents = property(s_show, s_set, s_del)

# -------------------------------------------------------------

    def o_show(self):
        return self.oana

    def o_set(self, value):
        self.oana.append(value)

    def o_del(self):
        self.oana = []

    oana_presents = property(o_show, o_set, o_del)

# -------------------------------------------------------------

    def __iter__(self):
        return ChristmasPresentsIter(self)


class ChristmasPresentsIter:
    def __init__(self, ChristmasPresents):
        self._mum = ChristmasPresents.mum
        self._dad = ChristmasPresents.dad
        self._sis = ChristmasPresents.sis
        self._oana = ChristmasPresents.oana
        self._presents_size = len(self._mum) + len(self._dad) + len(self._sis) + len(self._oana)
        self._current_index = 0
        self.__cactus = 2

    def __iter__(self):
        self._current_index = 0
        return self

    def __next__(self):
        if self._current_index < self._presents_size:
            if self._current_index < len(self._mum):
                member = self._mum[self._current_index]

            elif self._current_index < len(self._mum) + len(self._dad):
                member = self._dad[self._current_index - len(self._mum)]

            elif self._current_index < len(self._mum) + len(self._dad) + len(self._sis):
                member = self._sis[self._current_index - len(self._mum) - len(self._dad)]

            else:
                member = self._oana[self._current_index - len(self._mum) - len(self._dad) - len(self._sis)]

            self._current_index += 1
            return member

        raise StopIteration
