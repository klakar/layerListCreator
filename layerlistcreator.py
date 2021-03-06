# -*- coding: utf-8 -*-
"""
/***************************************************************************
 layerListCreator
                                 A QGIS plugin
 Skapa lagerlistor för insticksprogrammet "Ladda Lager".
                              -------------------
        begin                : 2014-04-29
        copyright            : (C) 2014 by Klas Karlsson / Geosupportsystem
        email                : klaskarlsson@hotmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.utils import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from layerlistcreatordialog import layerListCreatorDialog
import os.path
# Anpassningar för UTF-8
import codecs

global lagerLista
lagerLista = ""

class layerListCreator:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'layerlistcreator_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = layerListCreatorDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/layerlistcreator/icon.png"),
            u"Skapa Lagerlista", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Skapa Lagerlistor", self.action)

	
    def laddaLager(self):
	self.dlg.listWidget.clear()
	canvas = iface.mapCanvas()
	layers = canvas.layers()
	#QMessageBox.information(self.iface.mainWindow(),u"Tjoho",u"Visst är QGIS kul!")
	lagerLista = u"# Ladda Lager QGIS Plugin av Klas Karlsson\n"
	for layer in reversed(layers):
	    layerType = layer.type()
	    lagerkalla = layer.publicSource()
	    if layerType == QgsMapLayer.VectorLayer:
	        if "DBNAME=" in lagerkalla.upper():
			lagerLista = lagerLista + (u"POSTGIS,%s,%s\n" % (layer.name(), lagerkalla))
		elif "WFS" in lagerkalla.upper():
			lagerLista = lagerLista + (u"WFS,%s,%s\n" % (layer.name(), lagerkalla))
		else:
			lagerLista = lagerLista + (u"OGR,%s,%s\n" % (layer.name(), lagerkalla))
		self.dlg.listWidget.addItem(layer.name())
	    if layerType == QgsMapLayer.RasterLayer:
		if "WMS" in lagerkalla.upper():
			lagerLista = lagerLista + (u"wms,%s,%s\n" % (layer.name(), lagerkalla))
		else:
			lagerLista = lagerLista + (u"RASTER,%s,%s\n" % (layer.name(), lagerkalla))
		self.dlg.listWidget.addItem(layer.name())
	return lagerLista	
	#QMessageBox.information(self.iface.mainWindow(),u"Tjoho",lagerLista)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Skapa Lagerlistor", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # show the dialog
	lagerLista = self.laddaLager()
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            filnamn = QFileDialog.getSaveFileName(None, 'Save File', '.')
	    if filnamn != "":
		spara = codecs.open(filnamn, 'w', 'utf-8')
		spara.write(lagerLista)
		spara.close()
