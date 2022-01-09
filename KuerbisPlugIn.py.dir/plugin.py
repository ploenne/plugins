#
# mein erstes PlugIn

class kuerbisplugin(PythonPlugin):
    def onEnable(self):
        self.getLogger().info(" Start Kuerbis ")
        pass
    
    def onCommand(self, sender, command, label, args):
        originalPosition = sender.getLocation()
        # self.getServer().broadcastMessage( "Hallo " + sender.name + " deine Position ist: " + str(position))
        
        #position.setX(position.getX() + 3)
        
        if len(args) > 0: 
        
            wert = args[0]
            
            if wert == "clear":
                
                groesse = 100
                
                haelfte = groesse / 2
                    
                for x in range(0,groesse):
                
                    for y in range(0,groesse):
                        
                        # self.getLogger().info("x: " + str(x) + "y:  " + str(y))
                        
                        for z in range(0,groesse):
                            
                            kuerbisPosition = sender.getLocation()
                            
                            kuerbisPosition.setX(kuerbisPosition.getX() + float(x - haelfte)) 
                            kuerbisPosition.setY(kuerbisPosition.getY() + float(y - haelfte))
                            kuerbisPosition.setZ(kuerbisPosition.getZ() + float(z - haelfte)) 
                           # self.getLogger().info("nach: " + str(x) + ":  " + str(kuerbisPosition))
                            welt = sender.getWorld()
                            block = welt.getBlockAt(kuerbisPosition)
                            
                            if block.getType() == bukkit.Material.PUMKIN:
                                block.setType(bukkit.Material.AIR)
                
                
                return True
        else:
                
            for z in range(1,4):
                
                for x in range(1,11):
                        
                    kuerbisPosition = sender.getLocation()
                    #self.getLogger().info("vor: " + str(x) + ":  " + str(kuerbisPosition))
                    kuerbisPosition.setX(kuerbisPosition.getX() + float(x) + 1 ) 
                    kuerbisPosition.setY(kuerbisPosition.getY() + float(x) - 1 )
                    kuerbisPosition.setZ(kuerbisPosition.getZ() + float(z) - 1 ) 
                   # self.getLogger().info("nach: " + str(x) + ":  " + str(kuerbisPosition))
                    welt = sender.getWorld()
                    block = welt.getBlockAt(kuerbisPosition)
                    block.setType(bukkit.Material.PUMKIN)
                    #block.setType(bukkit.Material.COBBLESTONE_STAIRS) ??
                    #block.setFacingDirection(BlockFace.EAST , True) ??
                    
        return True 
     
     