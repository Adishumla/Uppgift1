
def button1_pressed(self): 
    
    import globals 
    globals.fsm.next()  
    return

def button2_pressed(self):
    
    import globals
    globals.fsm.previous()
    return