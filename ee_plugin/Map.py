# -*- coding: utf-8 -*-
"""
functions to use GEE within Qgis python script
"""

import ee_plugin.utils


def addLayer(image, vis_props=None, name=None, visible=None, opacity=None):
    """
        Mimic addLayer GEE function

        Uses:
            >>> from ee_plugin import Map
            >>> Map.addLayer(.....)
    """
    if vis_props:
        image = image.visualize(**vis_props)
    if not name:
        name = 'untitled'
    
    ee_plugin.utils.add_or_update_ee_image_layer(image, name)