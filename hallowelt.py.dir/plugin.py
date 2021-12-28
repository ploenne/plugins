#
# mein erstes PlugIn

class HalloWeltPlugin(PythonPlugin):
    def onEnable(self):
        self.getLogger().info("Hallo Welt Enable")