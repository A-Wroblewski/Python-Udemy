class TV:
    def __init__(self, color, size, default_volume=50, default_channel=1, is_on=False):
        self._color = color
        self.size = size
        self._default_volume = default_volume
        self._default_channel = default_channel
        self._is_on = is_on


    @property
    def color(self):
        return self._color


    def turn_on(self):
        if self._is_on:
            print('The TV is already on...')

        else:
            self._is_on = True

            print('The TV is now on...')


    def turn_off(self):
        if self._is_on:
            self._is_on = False

            print('The TV is now off...')

        else:
            print('The TV is already off...')


my_tv = TV('Black', 44)

print(f'TV color -> {my_tv.color}')
print(f'TV size -> {my_tv.size}', '\n')

my_tv.turn_off()
my_tv.turn_on()
my_tv.turn_on()
my_tv.turn_off()
