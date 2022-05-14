# 2017110292 김지완

class TV:
    # class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 20
    MIN_CHANNEL = 0
    MAX_CHANNEL = 200

    # set contribute of instance
    def __init__(self, volume = 5, channel = 0, is_on = False):
        self.__volume = volume
        self.__channel = channel
        self.__is_on = is_on

    def __str__(self):
        if self.__is_on:
            return f"볼륨 = {self.__volume}, 채널 = {self.__channel}"
        else:
            return "TV가 꺼짐 상태입니다."

    def toggle_power(self):
        if self.__is_on:
            self.__is_on = False
        else:
            self.__is_on = True

    # -----------------below are getters-----------------
    def get_channel(self):
        return self.__channel

    def get_volume(self):
        return self.__volume

    # -----------------below are setters-----------------
    def set_channel(self, channel):
        if channel >= TV.MIN_CHANNEL and channel <= TV.MAX_CHANNEL:
            self.__channel = channel
        else:
            print("채널 오류")

    def set_volume(self, volume):
        if volume >= TV.MIN_VOLUME and volume <= TV.MAX_VOLUME:
            self.__volume = volume
        else:
            print("볼륨 오류")
    
    def volume_up(self):
        if self.__volume < TV.MAX_VOLUME:
            self.__volume += 1

    def volume_down(self):
        if self.__volume > TV.MIN_VOLUME:
            self.__volume -= 1

    def channel_up(self):
        self.__channel += 1

        if self.__channel > TV.MAX_CHANNEL:
            self.__channel = TV.MIN_CHANNEL

    def channel_down(self):
        self.__channel -= 1

        if self.__channel < TV.MIN_CHANNEL:
            self.__channel = TV.MAX_CHANNEL

my_tv = TV()
print(my_tv)
my_tv.toggle_power()
print(my_tv)
my_tv.set_channel(45)
print(my_tv)
my_tv.volume_up()
my_tv.channel_up()
print(my_tv)
print()

# channel, volume up & down 검증을 위한 code
my_tv.set_channel(199)
my_tv.set_volume(19)
print(my_tv)
my_tv.channel_up()
my_tv.volume_up()
print(my_tv)
my_tv.channel_up()
my_tv.volume_up()
print(my_tv)
my_tv.channel_up()
my_tv.set_volume(2)
print(my_tv)
my_tv.channel_down()
my_tv.volume_down()
print(my_tv)
my_tv.channel_down()
my_tv.volume_down()
print(my_tv)
my_tv.channel_down()
my_tv.volume_down()
print(my_tv)