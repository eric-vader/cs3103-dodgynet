#!/usr/bin/env python3

logger_debug_format = '%(asctime)s %(levelname)-8s'\
' [%(process)-5d] %(filename)s +%(lineno)s: %(message)s'
logger_consumer_format = '%(message)s'

ascii_art_logo = """\

 /$$$$$$$                  /$$                     /$$   /$$             /$$    
| $$__  $$                | $$                    | $$$ | $$            | $$    
| $$  \ $$  /$$$$$$   /$$$$$$$  /$$$$$$  /$$   /$$| $$$$| $$  /$$$$$$  /$$$$$$  
| $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$| $$  | $$| $$ $$ $$ /$$__  $$|_  $$_/  
| $$  | $$| $$  \ $$| $$  | $$| $$  \ $$| $$  | $$| $$  $$$$| $$$$$$$$  | $$    
| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$\  $$$| $$_____/  | $$ /$$
| $$$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$  |  $$$$/
|_______/  \______/  \_______/ \____  $$ \____  $$|__/  \__/ \_______/   \___/  
                               /$$  \ $$ /$$  | $$                              
                              |  $$$$$$/|  $$$$$$/                              
                               \______/  \______/                               
"""

# vim: expandtab shiftwidth=4 softtabstop=4 textwidth=80:
