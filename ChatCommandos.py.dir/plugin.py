#
# mein erstes PlugIn

class chatcommandoplugin(PythonPlugin):
    def onEnable(self):
        self.getLogger().info("--- Start ChatCommando PlugIn Enable")
        pass
    
    def onCommand(self, sender, command, label, args):
        
        self.getLogger().info("uebriges commando: " + str(command))
        
        if "halloserver" in str(command):
            
            self.getLogger().info("Hallo" + str(sender.name) + "!!" )
            self.getServer().broadcastMessage("Hallo " + str(sender.name) + " !!" )
            return True
        
        else:
            
            self.getLogger().info("Hier " + str(sender.name) + " ist dein Eierkuchen !!" )

            self.getServer().broadcastMessage("Hier " + str(sender.name) + " ist dein Eierkuchen !!" )
            return True

        return True
    