import os
import sys
import math
import time
import pygame
import colorsys
import numpy as np
import pygame as pg 
import pygame.locals
from typing import Any, List
from HilbertCurve import hilbert_curve

def map_value_to_color(value, min_value, max_value):
    # Normalize the value within the specified range
    normalized_value = (value - min_value) / (max_value - min_value)
    # Map the normalized value to HSV color space
    hue = normalized_value * 240  # Range of hue is 0-240
    saturation = 1.0  # Fully saturated color
    value = 1.0  # Maximum value
    # Convert HSV color to RGB color
    rgb = colorsys.hsv_to_rgb(hue / 360, saturation, value)
    # Scale RGB values to 0-255 range
    scaled_rgb = [int(x * 255) for x in rgb]
    return scaled_rgb

class Game:
    def __init__(self, width : int = 1920, height : int = 1080):
        self.running : bool = True
        self.flag : bool = True
        self.fps : float = 99999999999999999
        self.width : int = width
        self.height : int =  height

        self.last_time : float = time.perf_counter()

        pg.init()
        pg.font.init()
        self.font = pg.font.SysFont(None, 10)
        self.clock = pg.time.Clock()
        self.display = pg.display
        self.screen = self.display.set_mode((self.width, self.height))
        self.display.set_caption('_')
        self.dict_keys : List  = list(pg.locals.__dict__.keys())
        self.dict_values : List = list(pg.locals.__dict__.values())


    def handle_events(self):
        events = pg.event.get()
        for event in events:

            event_name = pg.event.event_name(event.type)

            # print(f"{event_name} : {event._dict_}")
            if event.type == pg.QUIT:
                self.quit()
                break
            elif 'Key' in event_name:
                key_pressed = self.dict_keys[self. dict_values.index(event.key)]
                if event_name == 'KeyDown':
                    if key_pressed == 'K_ESCAPE':
                        self.quit()
                        break
                    pass

                elif event_name == 'KeyUP': 
                    pass
                pass
            elif event_name == 'TextInput':
                #print(f"{event.text} Key Pressed")
                pass
            elif 'Mouse' in event_name:
                pass
            elif 'Window' in event_name:
                pass
            else:
                # print(f"Event Handler Not Implement : {event_name} : {event._dict_}")
                pass

    def update_fps(self):
        fps_text = f"{self.clock.get_fps():.2f}"
        # self.screen.blit(self.font.render(fps_text, True, pg.Color("cyan")), (self.width - self.font.size(fps_text)[0], 1))

        self.display.set_caption(f'FPS : {fps_text}')

        # print(f"FPS : fps_text", end='\r')

    def update(self, dt, rect):
        self.display.update(rect)
        self.update_fps()
        self.display.update()

    def run(self):
        self.order = 2
        while self.running:
            self.order += 1
            #if self.order >= 8:
                #self.screen.fill((0,0,0))

            lines = hilbert_curve(self.width, self.height, self.order)
            for i in range(1,len(lines)):
                start_pos = (int(lines[i].x), int(lines[i].y))
                end_pos = (int(lines[i - 1].x), int(lines[i - 1].y))
                if int(lines[i].y) < self.height + 61 and int(lines[i-1].y) < self.height + 61:
                    rect = pg.draw.line( self.screen,    map_value_to_color(i, 1, len(lines))     , start_pos=start_pos,     end_pos=end_pos)
                    #dt = self.clock.tick(self.fps)  # seconds
                    self.update(1, rect)
                    self.handle_events()


    def quit(self):
        self.running = False
        self.display.quit()
        pg.quit()

if __name__ == "__main__":
    game = Game()
    game.run()