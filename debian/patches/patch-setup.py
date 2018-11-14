Index: Electrum_PAC-3.2.3/setup.py
===================================================================
--- Electrum_PAC-3.2.3.orig/setup.py
+++ Electrum_PAC-3.2.3/setup.py
@@ -77,6 +77,7 @@ setup(
         'electrum_pac',
         'electrum_pac.gui',
         'electrum_pac.gui.qt',
+        'electrum_pac.plugins',
     ] + [('electrum_pac.plugins.'+pkg) for pkg in find_packages('electrum_pac/plugins')],
     package_dir={
         'electrum_pac': 'electrum_pac'
