<<<<<<< refs/remotes/upstream/master:electrum_dash/plugins/labels/kivy.py
from .labels import LabelsPlugin
from electrum_dash.plugin import hook
=======
from labels import LabelsPlugin
from electrum_PAC.plugins import hook
>>>>>>> Rebranding for PAC:plugins/labels/kivy.py

class Plugin(LabelsPlugin):

    @hook
    def load_wallet(self, wallet, window):
        self.window = window
        self.start_wallet(wallet)

    def on_pulled(self, wallet):
        self.logger.info('on pulled')
        self.window._trigger_update_history()

