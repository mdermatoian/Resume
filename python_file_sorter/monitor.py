import sys
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import logging
import shutil

if __name__ == '__main__':

    def move_file(file_path):
        if file_path.endswith('.jpg'):
            shutil.move(file_path, 'C:\Users\mattd\OneDrive\Pictures')

    logging.basicConfig(level=logging.INFO,
    format='%(asctime)s - %(process)d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

    #Directory or File I want to monitor
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    
    event_handler = LoggingEventHandler()
    observer = Observer()

    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()



            
        