#
# mein erstes PlugIn

class chatcommandoplugin(PythonPlugin):
    def onEnable(self):
        self.getLogger().info("--- Start ChatCommando PlugIn Enable")
        pass
    
    def onCommand(self, sender, command, label, args):
        
        logger = self.getLogger()
        
        info = "Hallo " + str(sender.name)
        
        logger.info(infoMessage)
        
        #self.getLogger().info("Hallo Spieler " + str(sender.name))
        self.getServer().broadcastMessage("Hallo " + str(sender.name))
        return True
    