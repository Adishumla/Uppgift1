
def button1_pressed(self): 
    """
    Callback-rutin för tryckknapp 1, vilket medför att aktuellt tillstånd uppdateras till nästa.
    """
    import globals 
    globals.fsm.next()  
    return

def button2_pressed(self):
    """
    Callback-rutin för tryckknapp 2, vilket medför att aktuellt tillstånd uppdateras till föregående.
    """
    import globals
    globals.fsm.previous()
    return