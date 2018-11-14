from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core import core_select_lib

__all__ = ('NFCBase', 'NFCScanner')

class NFCBase(Widget):
    ''' This is the base Abstract definition class that the actual hardware dependent
    implementations would be based on. If you want to define a feature that is
    accessible and implemented by every platform implementation then define that
    method in this class.
    '''

    payload = ObjectProperty(None)
    '''This is the data gotten from the tag. 
    '''

    def nfc_init(self):
        ''' Initialize the adapter.
        '''
        pass

    def nfc_disable(self):
        ''' Disable scanning
        '''
        pass

    def nfc_enable(self):
        ''' Enable Scanning
        '''
        pass

    def nfc_enable_exchange(self, data):
        ''' Enable P2P Ndef exchange
        '''
        pass

    def nfc_disable_exchange(self):
        ''' Disable/Stop P2P Ndef exchange
        '''
        pass

# load NFCScanner implementation

NFCScanner = core_select_lib('nfc_manager', (
    # keep the dummy implementation as the last one to make it the fallback provider.NFCScanner = core_select_lib('nfc_scanner', (
    ('android', 'scanner_android', 'ScannerAndroid'),
<<<<<<< refs/remotes/upstream/master:electrum_dash/gui/kivy/nfc_scanner/__init__.py
    ('dummy', 'scanner_dummy', 'ScannerDummy')), True, 'electrum_dash.gui.kivy')
=======
    ('dummy', 'scanner_dummy', 'ScannerDummy')), True, 'electrum_PAC_gui.kivy')
>>>>>>> Rebranding for PAC:gui/kivy/nfc_scanner/__init__.py
