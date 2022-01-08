#
# mein erstes PlugIn

class pluseinsplugin(PythonPlugin):
    def onEnable(self):
        self.getLogger().info("--- Start Plus Eins PlugIn Enable")
        pass
    
    def onCommand(self, sender, command, label, args):
        
        # wie es im Buch gesagt wird 
        # eingabe  = args[0]
        # 
        # zahl = int(eingabe)
        # 
        # zahl = zahl + 1
        # 
        # info = "Ergebnis " + str(zahl)
        # 
        # self.getServer().broadcastMessage("Hallo " + str(sender.name) + " dein Ergbnis ist " + info)
        # 
        # return True
    
        if len(args) == 0:
            self.getServer().broadcastMessage( "Hallo " + sender.name + " du hast keinen Wert angegeben! Setze eine Zahl ein!" ) 
            return True
        
        if len(args) == 1: 
        
            wert = args[0]
        
            self.getLogger().info("uebergebener wert: " + wert)
            
            if wert.isdigit():
                
                    zahl = int(wert)
                
                    zahl2 = zahl + 1
                
                    self.getServer().broadcastMessage( "Hallo " + sender.name + " dein Ergebnis ist " + str(zahl2)
                                                      ) 
            else:
                    self.getServer().broadcastMessage("Du darfst nur Zahlen einstetzen, keine Woerter!")
                
            return True
        
        else:
            
            summe = 0
            
            for item in args:
                    summe = summe + int(item)
            
            self.getServer().broadcastMessage( "Hallo " + sender.name + " deine Rechenaufgabe ergibt " + str(summe) ) 

            return True  
            
            
                
            
                
                
                
        
        