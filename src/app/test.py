# using datetime module
import datetime

# ct stores current time
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print("current time:-", timestamp)
