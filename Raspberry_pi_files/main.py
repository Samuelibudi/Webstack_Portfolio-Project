from goto import with_goto
from stddef import *
import var
import pio
import resource
from datetime import datetime
from Detect_face import capture_image_on_face_detection


# Peripheral Configuration Code (Do Not Edit)
#---CONFIG_BEGIN---
import cpu
import FileStore
import VFP
import camera
import Displays
import Generic

'''Module that sets up the raspberry pi and is main entry of program'''

def peripheral_setup () :
    '''Methods sets up peripherals to be used with raspberry pi'''
    pio.cpu=cpu.CPU ()
    pio.storage=FileStore.FileStore ()
    pio.server=VFP.VfpServer ()
    pio.CAM1=camera.RPiCamera ()
    pio.LCD1=Displays.I2CLDC ()
    pio.RGBLED1=Generic.RgbLedCa (pio.GPIO19, pio.GPIO20, pio.GPIO26)
    pio.BTN1=Generic.Button (pio.GPIO4)
    pio.storage.begin ()
    pio.server.begin (0)

# Install interrupt handlers

def peripheral_loop () :
    pio.server.poll ()

#---CONFIG_END---


def variables_setup () :
    # Flowchart Variables
    pass


# Flowchart Routines
@with_goto
def chart_SETUP () :
    pio.LCD1.clear () 
    pio.LCD1.print ("LOOK AT CAMERA")   
    pio.RGBLED1.set (False, True, False)
                                  
    return

@with_goto
def chart_LOOP () :
    while not (pio.BTN1()) :
        pass


    pio.LCD1.clear ()
    pio.LCD1.print ("CHECKING!")
    pio.RGBLED1.set (False, False, True)
    num = capture_image_on_face_detection()
                                             
    if (num == 'A'):
        pio.RGBLED1.set (False, True, False)
        pio.LCD1.clear()
        pio.LCD1.print("ACCESS GRANTED!")
    else:
        pio.RGBLED1.set (True, False, False)
        pio.LCD1.clear ()
        pio.LCD1.print ("ACCESS DENIED!")
    return

# Main function
def main () :
    '''Main method to start program on raspberry pi'''

    # Setup
    variables_setup ()
    peripheral_setup ()
    chart_SETUP ()
    
    # Infinite loop
    while True :
        peripheral_loop ()
        chart_LOOP ()
                                                                                
# Command line execution
if __name__ == '__main__' :
    main()
