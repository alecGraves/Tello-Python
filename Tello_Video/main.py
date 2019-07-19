import tello
from tello_control_ui import TelloUI

def main():

    drone = tello.Tello('', 8889, interface_str="wlx503eaaac9b0f")  
    vplayer = TelloUI(drone,"./img/")
    
	# start the Tkinter mainloop
    vplayer.root.mainloop() 

if __name__ == "__main__":
    main()
