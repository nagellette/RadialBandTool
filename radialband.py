# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RadialBand
                                 A QGIS plugin
 Draw desired radial bands for selected point features
                              -------------------
        begin                : 2014-03-30
        copyright            : (C) 2014 by NecipEnesGENGEC
        email                : necipenesgengec@gmail.com
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
from qgis.gui import *
from qgis import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from radialbanddialog import RadialBandDialog
import os.path


class RadialBand:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'radialband_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)


        self.dlg = RadialBandDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/radialband/icon.png"),
            u"Radilal Band Tool", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&RadialBandsTool", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&RadialBandsTool", self.action)
        self.iface.removeToolBarIcon(self.action)

    def inputConfig(self):
        QgisMainWindow = qgis.utils.iface.mainWindow()
        filename = QFileDialog.getSaveFileName(QgisMainWindow, "Save File", os.getenv('HOME'))
        fname = open(filename, w)
        data = fname.write()
        self.textEdit.setText(data)
        fname.close()

    def get_selected_coordinates(self):

        #need to grap coordinates from geometry to string
        layer = utils.iface.activeLayer()
        selected_features = layer.selectedFeatures()
        #geom=[]
        for f in selected_features:
            #geom.append(f.geometry())
            asd=f.geometry().asPoint
            print str(asd)
                

    def get_radius(self):
        none
        
    def draw_circle_to_selected_coordinates(self, band_values):
        none
    

    # run method that performs all the real work
    def run(self):
        self.dlg=RadialBandDialog()
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            self.get_selected_coordinates()
            RadialLayer=QgsVectorLayer(self.plugin_dir+"/shp/RadialBand.shp", "RadialBand", "ogr")
            if not RadialLayer.isValid():
                print ("Layer failed to load!")
                print (self.plugin_dir+"/RadialBandTool/shp/RadialBand.shp""Layer failed to load!")
            else:
                QgsMapLayerRegistry.instance().addMapLayer(RadialLayer)# show the dialog

            #self.inputConfig()
                        
            pass
