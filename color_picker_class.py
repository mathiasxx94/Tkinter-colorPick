import Tkinter as tk
import math
from PIL import Image, ImageTk

window = tk.Tk()

class colorPicker:
    def __init__(self):
        self.canvas = tk.Canvas(width=211,height=211)
        #self.canvas.pack(fill="none", expand=False, anchor="nw")
        
        self.button = tk.Button(width=3, height=1, relief="sunken", bg="white")
        #self.button.pack( anchor="ne")
        
        self.drag_data = {"x": 0, "y": 0, "item": None}
        self.angle = 0
        
        self.loadimg("colorpicker4.png")
        self.loadcursor("player_icon.png")
        
        self.canvas.tag_bind("token", "<ButtonPress-1>", self.on_token_press)
        self.canvas.tag_bind("token", "<ButtonRelease-1>", self.on_token_release)
        self.canvas.tag_bind("token", "<B1-Motion>", self.on_token_motion)
    
    def pack(self):
        self.canvas.pack(fill="none", expand=False, anchor="nw")
        self.button.pack( anchor="ne")
        
    
    def loadimg(self, imagename):
        #global tkphoto
        path = "C:\\Users\\mathi\\Desktop\\CSGO_tkinter_GUI\\"
        photo = Image.open(path + imagename)
        self.tkphoto = ImageTk.PhotoImage(photo)
        self.canvas.create_image((0,0), image=self.tkphoto, anchor="nw")
    
    def loadcursor(self, imagename):
        #global tkcursor
        path = "C:\\Users\\mathi\\Desktop\\CSGO_tkinter_GUI\\"
        cursorimg = Image.open(path + imagename)
        self.tkcursor = ImageTk.PhotoImage(cursorimg)
        self.cursor = self.canvas.create_image((106 + 84, 106), image=self.tkcursor, anchor="center", tags="token")
    
    def hue_to_rgb(self, hue):
        hue = abs(hue % 360)
        C = 1 * 1  # value * saturation
        X = C * (1 - abs((hue / 60.0) % 2 - 1))
    
        if 0 <= hue < 60:
            R, G, B = C, X, 0
        elif 60 <= hue < 120:
            R, G, B = X, C, 0
        elif 120 <= hue < 180:
            R, G, B = 0, C, X
        elif 180 <= hue < 240:
            R, G, B = 0, X, C
        elif 240 <= hue < 300:
            R, G, B = X, 0, C
        elif 300 <= hue < 360:
            R, G, B = C, 0, X
    
        R = R * 255
        G = G * 255
        B = B * 255
    
        return (R, G, B)
        
    def on_token_press(self, event):
        '''Begining drag of an object'''
        # record the item and its location
        self.drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def on_token_release(self, event):
        '''End drag of an object'''
        # reset the drag information
        self.drag_data["item"] = None
        self.drag_data["x"] = 0
        self.drag_data["y"] = 0

    def on_token_motion(self, event):
        '''Handle dragging of an object'''
        """
        # compute how much the mouse has moved
        delta_x = event.x - self.drag_data["x"]
        self.angle += delta_x
        # move the object the appropriate amount
        x = 106 + 84 * math.cos(math.radians(-self.angle))
        y = 106 - 84 * math.sin(math.radians(-self.angle))
        if self.drag_data["item"] == 2:
            self.canvas.coords(self.cursor, (x, y))
            mycolor = '#%02x%02x%02x' % (self.hue_to_rgb(self.angle))
            self.button.configure(bg=mycolor)
        # record the new position
        self.drag_data["x"] = event.x
        """
        
        if self.drag_data["item"] == 2:
            pos_x = event.x
            pos_y = event.y
    
            delta_x = 110 - pos_x
            delta_y = 110 - pos_y
    
            self.angle = math.atan2(delta_y, delta_x) * (180/math.pi)
        
            self.angle -=180
            if self.angle < 0:
                self.angle = 360 + self.angle
            
            x = 106 + 84 * math.cos(math.radians(-self.angle))
            y = 106 - 84 * math.sin(math.radians(-self.angle))
            self.canvas.coords(self.cursor, (x,y))
            mycolor = '#%02x%02x%02x' % (self.hue_to_rgb(self.angle))
            self.button.configure(bg=mycolor) 
        
        

a=colorPicker().pack()
b=colorPicker().pack()
def printer():
    print a.angle
tk.Button(command=printer).pack()
window.mainloop()


























