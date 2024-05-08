import os
import shutil
import time
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


source = "C:/Users/This PC/Downloads"
destination = "C:/Users/This PC/Desktop"
dir_tree = { "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'], "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'], "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'], "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg'] }

class filemovementhandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f'{event.src_path} has been created!')

    def on_deleted(self,event):
        print(f'{event.src_path} has been deleted!')
    
    def on_moved(self,event):
        print(f'{event.src_path} has been moved!')
    
    def on_deleted(self,event):
        print(f'{event.src_path} has been deleted!')

event_handler = filemovementhandler()
observer = Observer()
observer.schedule(event_handler,source,recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()
