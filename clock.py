#programmer:          Nathan Colburn
#program Name:        Digital Clock
#Date Written:        7/25/20
'''This program creates a working digital '''
#======================================================================

#variables
#they are set to specific times to show the program works correctly
seconds = 55;
minutes = 59;
hours = 12;

#======================================================================
#import
import time


#loop
while True:
    print(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2));
    #.zfill(2) forces python to show 2 digits no matter what
    seconds = seconds + 1;
    time.sleep(1);
    if seconds == 60:
        seconds = 0;
        minutes = minutes + 1;
    if minutes == 60:
        minutes = 0;
        hours = hours + 1;
    if hours == 13:
        hours = 1;