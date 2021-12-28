#
# mein erstes PlugIn

class pluseinsplugin(PythonPlugin):
    def onEnable(self):
        self.getLogger().info("--- Start Plus Eins PlugIn Enable")
        pass
    
    def onCommand(self, sender, command, label, args):
        
        eingabe  = args[0]
        
        zahl = int(eingabe)
        
        zahl = zahl + 1
        
        info = "Ergebnis " + str(zahl)
        
        self.getServer().broadcastMessage("Hallo " + str(sender.name) + " dein Ergbnis ist " + info)
        
        return True
    