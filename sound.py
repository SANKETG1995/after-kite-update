import winsound
import time
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second


winsound.Beep(frequency, duration)

frequency = 1000  # Set Frequency To 1000 Hertz
duration = 2500  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
time.sleep(3)
winsound.Beep(frequency, duration)
time.sleep(3)
winsound.Beep(frequency, duration)