CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    N = 1

    def first_channel(self):
        self.N = 1
        print(self.N, CHANNELS[self.N - 1], sep=': ')

    def last_channel(self):
        self.N = len(CHANNELS)
        print(self.N, CHANNELS[self.N - 1], sep=': ')

    def turn_channel(self, channel):
        self.N = channel
        print(self.N, CHANNELS[self.N - 1], sep=': ')

    def next_channel(self):
        if not self.N == len(CHANNELS):
            self.N += 1
        else:
            self.N = 1
        print(self.N, CHANNELS[self.N - 1], sep=': ')

    def previous_channel(self):
        if not self.N == 1:
            self.N -= 1
        else:
            self.N = len(CHANNELS)
        print(self.N, CHANNELS[self.N - 1], sep=': ')

    def current_channel(self):
        print(self.N, CHANNELS[self.N - 1], sep=': ')

# Is there a way to not write the line with print these many times? For the aspect and maybe future efficiency of code.

    def is_exist(self, M):
        try:
            if M in CHANNELS or M <= len(CHANNELS):
                print('Yes')
            else:
                print('No')
        except TypeError:
            print('No')


TV = TVController()
print(TV.N)
print('\nFirst:')
TV.first_channel()
print('\nLast:')
TV.last_channel()
print('\nNext:')
TV.next_channel()
print('\nPrevious:')
TV.previous_channel()
print('\nCurrent:')
TV.current_channel()
print('\nis exist:')
TV.is_exist('BC')