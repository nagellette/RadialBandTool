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
from ui_radialband import Ui_RadialBand
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

        
    def draw_circle_to_selected_coordinates(self):
        """
        Gets the coordinate of selected features and draws the circles for desired radius in qgis
        """

        #set active layer as layer
        layer = utils.iface.activeLayer()
        selected_features = layer.selectedFeatures()
        
        #creates new memory layer for radial bands
        vpoly = QgsVectorLayer("Polygon", "RadialBand", "memory")
        feature = QgsFeature()
        provider = vpoly.dataProvider()
        vpoly.startEditing()
	
	#get band radiuses from the file
        list=[]
        f=open("radial_band.nodelete", "r")
        with open('radial_band.nodelete') as openfileobject:
            for line in openfileobject:
                value=float(line.strip())
                list.append(value)
        f.close()
        
        #filling radial band table with selected feature coordinates and desired radiuses
        for f in selected_features:
            geom = f.geometry()
            x=float(geom.asPoint().x())
            y=float(geom.asPoint().y())
            item=0
            for item in range(0, len(list)):
                radius=list[item]
		#draw circle to the selected coordinates and radius one by one
                feature.setGeometry( QgsGeometry.fromPoint(QgsPoint(x,y)).buffer(radius,100))
                provider.addFeatures( [feature] )
                item+=item


        vpoly.commitChanges()         

        QgsMapLayerRegistry.instance().addMapLayer(vpoly)
        
    

    # run method that performs all the real work
    def run(self):
        self.dlg=RadialBandDialog()
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            self.draw_circle_to_selected_coordinates()
            pass
