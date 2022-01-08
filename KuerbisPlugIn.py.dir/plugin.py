#
# mein erstes PlugIn

class kuerbisplugin(PythonPlugin):
    def onEnable(self):
        self.getLogger().info("--- Start Plus Eins PlugIn Enable")
        pass
    
    def onCommand(self, sender, command, label, args):
        originalPosition = sender.getLocation()
        # self.getServer().broadcastMessage( "Hallo " + sender.name + " deine Position ist: " + str(position))
        
        #position.setX(position.getX() + 3)
        
        for x in range(1,10):
            
            kuerbisPosition = sender.getLocation()
            #self.getLogger().info("vor: " + str(x) + ":  " + str(kuerbisPosition))
            kuerbisPosition.setX(kuerbisPosition.getX() + float(x) + 1 ) 
            kuerbisPosition.setY(kuerbisPosition.getY() + float(x) - 1)
           # self.getLogger().info("nach: " + str(x) + ":  " + str(kuerbisPosition))
            welt = sender.getWorld()
            block = welt.getBlockAt(kuerbisPosition)
            block.setType(bukkit.Material.PUMPKIN)
                    
        return True 
     
     