class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Initialize the Television with default power off, muted off, channel and volume at minimum."""
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__status = False
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """Toggle the power status of the television."""
        self.__status = not self.__status

    def mute(self):
        """Toggle mute status if the television is on."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """Increase the channel by 1 if the television is on. Wrap around to MIN_CHANNEL if at MAX_CHANNEL."""
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """Decrease the channel by 1 if the television is on. Wrap around to MAX_CHANNEL if at MIN_CHANNEL."""
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        """Increase the volume by 1 if the television is on and volume is below MAX_VOLUME. Unmute if muted."""
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """Decrease the volume by 1 if the television is on and volume is above MIN_VOLUME. Unmute if muted."""
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """Return a string representing the current power, channel, and volume (0 if muted) of the television."""
         if self.__muted:
             volume_display = Television.MIN_VOLUME
         else:
             volume_display = self.__volume
         return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {volume_display}'
