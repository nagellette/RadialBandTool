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
            u"Radial Band Tool", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        #self.iface.addPluginToMenu(u"&RadialBandsTool", self.action)
        self.iface.vectorMenu().addAction(self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&RadialBandsTool", self.action)
        self.iface.vectorMenu().removeAction(self.action)
        self.iface.removeToolBarIcon(self.action)


    def draw_circle_to_selected_coordinates(self):
        """
        Gets the coordinate of selected features and draws the circles for desired radius in qgis
        """

        #set active layer as layer
        layer = utils.iface.activeLayer()
        selected_features = layer.selectedFeatures()

        #for f in selected_features:
        #    print f.attributeMap()


        #creating layer structure using selected layer fields.
        fields = layer.pendingFields()
        fields_in = "Polygon?"
        field_counter = 1

        for field in fields:
            fields_in = fields_in + 'field=' + str(field.name()) + ':' + str(field.typeName()) + '&'
            field_counter += field_counter

        fields_in = fields_in + ('field=Band:Double')


        #creates new memory layer for radial bands with selected layer attributes
        vpoly = QgsVectorLayer(fields_in, "RadialBand", "memory")
        feature = QgsFeature()
        provider = vpoly.dataProvider()
        vpoly.startEditing()

        #filling radial band table with selected feature coordinates and desired radiuses
        for f in selected_features:
            geom = f.geometry()
            attr_in = f.attributes()
            x = float(geom.asPoint().x())
            y = float(geom.asPoint().y())
            item = 0
            for item in range(0, len(Ui_RadialBand.list_bands)):
                radius = Ui_RadialBand.list_bands[item]
                attr = attr_in
                #draw circle to the selected coordinates and radius one by one
                feature.setGeometry(QgsGeometry.fromPoint(QgsPoint(x, y)).buffer(radius, 100))
                attr.append(radius)
                feature.setAttributes(attr)
                provider.addFeatures([feature])
                print radius, attr
                del attr[-1]
                item += item


        #print attr
        #print Ui_RadialBand.list_bands
        # free lists for re-use
        attr = []
        Ui_RadialBand.list_bands = []

        vpoly.commitChanges()
        QgsMapLayerRegistry.instance().addMapLayer(vpoly)
        symbols = vpoly.rendererV2().symbols()
        symbol = symbols[0]
        symbol.setColor(QColor(0, 0, 0, 0))
        utils.iface.mapCanvas().refresh()
        utils.iface.legendInterface().refreshLayerSymbology(vpoly)


    # run method that performs all the real work
    def run(self):
        self.dlg = RadialBandDialog()
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            self.draw_circle_to_selected_coordinates()
            pass
