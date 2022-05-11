import time
import datetime
 
# Create class that acts as a countdown
def countdown_func(m):
    global rocket
    
    # Calculate the total number of seconds
    total_seconds =  m * 60
 
    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
 
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)
        
        # Prints the time left on the timer
        print(timer, end="\r")
        # Delays the program one second
        time.sleep(1)
 
        # Reduces total time by one second
        total_seconds -= 1
 
    #done_time = str("Bzzzt! The countdown is at zero seconds!")
    #return done_time
# Inputs for hours, minutes, seconds on timer


#countdown_func(int(m))