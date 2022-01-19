def button_pressed(self): 
    import globals 
    if globals.button1.is_pressed(): globals.fsm.next() 
    #elif globals.button1.is_pressed(): globals.fsm.previous()  
    return
