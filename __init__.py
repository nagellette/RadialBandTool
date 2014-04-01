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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load RadialBand class from file RadialBand
    from radialband import RadialBand
    return RadialBand(iface)
