import datetime
from tkinter import *
import time
import webbrowser

root = Tk()
root.title("Alarm Clock")

# Create a label to display instructions
label = Label(root, text="Set alarm time (24-hour format, HH:MM)")
label.pack()

# Create an entry field for the alarm time
entry = Entry(root)
entry.pack()

# Define a function to set the alarm time
def set_alarm():
    alarm_time = entry.get()
    try:
        # Convert the alarm time to datetime object
        alarm = datetime.datetime.strptime(alarm_time, "%H:%M")
        now = datetime.datetime.now()

        # Set the alarm for today
        alarm = alarm.replace(year=now.year, month=now.month, day=now.day)

        # Calculate the time difference until the alarm goes off
        time_diff = alarm - now

        # If the alarm time has already passed, set it for tomorrow
        if time_diff.total_seconds() < 0:
            alarm = alarm + datetime.timedelta(days=1)
            time_diff = alarm - now

        # Display the time until the alarm goes off
        print("Alarm set to go off in:", time_diff)

        # Sleep until the alarm goes off
        time.sleep(time_diff.total_seconds())

        # Time for the alarm to go off
        print("Wake Up!")

        # Open a web browser with a video or any desired action
        webbrowser.open("https://www.youtube.com/watch?v=Bov69XmoPoy")

    except ValueError:
        print("Invalid time format. Please enter the time in HH:MM format.")

# Create a button to set the alarm
button = Button(root, text="Set Alarm", command=set_alarm)
button.pack()

# Run the tkinter event loop
root.mainloop()
