from datetime import datetime
import speedtest

s = speedtest.Speedtest()

# start_time = datetime.datetime.now().strftime("%H:%M:%S")
# start_time = datetime.datetime.now()
# print(start_time)
# print(s.download(), s.upload())
# stop_time = datetime.datetime.now()
# duration = stop_time - start_time
# print(duration)


def get_speed():
    """_summary_
    """
    startTime = datetime.now()
    time_now = datetime.now().strftime("%H:%M:%S")
    downspeed = round((round(s.download()) / 1048576), 2)
    upspeed = round((round(s.upload()) / 1048576), 2)
    duration = (datetime.now() - startTime).seconds
    print(f"time: {time_now}, Duration: {duration} seconds, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")


def get_time():
    # startTime = datetime.datetime.now().strftime("%H:%M:%S")
    startTime = datetime.now()
    duration = (datetime.now() - startTime)
    print(duration)


if __name__ == "__main__":
    get_speed()
