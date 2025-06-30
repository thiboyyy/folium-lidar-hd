class LayerCatalog:
    def __init__(self):
        self.layers = {
            "MapantFR": "https://tiles.mapant.fr/{z}/{x}/{y}.png",
            "OpenStreetMap": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
            "OpenRailwayMap": "https://{s}.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png",
            "OpenTopoMap": "https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png",
            "Google Satellite": "https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
            "Google Hybrid": "https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
            "Google Pentes": "https://mt1.google.com/vt/lyrs=t&x={x}&y={y}&z={z}",
            "Google Terrain": "https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}",
            "Google Roadmap": "https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
            "IGN Orthophoto": (
                "https://data.geopf.fr/wmts?"
                "&REQUEST=GetTile&SERVICE=WMTS&VERSION=1.0.0"
                "&STYLE=normal"
                "&TILEMATRIXSET=PM"
                "&FORMAT=image/jpeg"
                "&LAYER=ORTHOIMAGERY.ORTHOPHOTOS"
                "&TILEMATRIX={z}"
                "&TILEROW={y}"
                "&TILECOL={x}"
            ),
            "IGN MNT": (
                "https://data.geopf.fr/wmts?"
                "&REQUEST=GetTile"
                "&SERVICE=WMTS"
                "&VERSION=1.0.0"
                "&STYLE=normal"
                "&LAYER=IGNF_LIDAR-HD_MNT_ELEVATION.ELEVATIONGRIDCOVERAGE.SHADOW"
                "&FORMAT=image/png"
                "&TILEMATRIXSET=PM_0_18"
                "&TILEMATRIX={z}"
                "&TILEROW={y}"
                "&TILECOL={x}"
            ),
            "OpenCycleMap": "https://{s}.tile.thunderforest.com/cycle/{z}/{x}/{y}.png",
            "CyclOSM": "https://{s}.tile-cyclosm.openstreetmap.fr/cyclosm/{z}/{x}/{y}.png",
            "IGN MNS": (
                "https://data.geopf.fr/wmts?"
                "&REQUEST=GetTile"
                "&SERVICE=WMTS"
                "&VERSION=1.0.0"
                "&STYLE=normal"
                "&LAYER=IGNF_LIDAR-HD_MNS_ELEVATION.ELEVATIONGRIDCOVERAGE.SHADOW"
                "&FORMAT=image/png"
                "&TILEMATRIXSET=PM_0_18"
                "&TILEMATRIX={z}"
                "&TILEROW={y}"
                "&TILECOL={x}"
            ),
            "OpenRailwayMap": "https://{s}.tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png",
            "WayMarkedTrails": "https://tile.waymarkedtrails.org/hiking/{z}/{x}/{y}.png",
            "WindyTouristMap": "https://windytiles.mapy.cz/turist-m/{z}-{x}-{y}.png",
            "IGN Topo": "https://data.geopf.fr/private/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=GEOGRAPHICALGRIDSYSTEMS.MAPS.SCAN25TOUR&STYLE=normal&TILEMATRIXSET=PM_6_16&TILEMATRIX={z}&TILECOL={x}&TILEROW={y}&FORMAT=image/jpeg&apikey=ign_scan_ws",
            "IGN_PCRS": "https://data.geopf.fr/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=PCRS.LAMB93&STYLE=normal&FORMAT=image%2Fjpeg&TILEMATRIXSET=2154_5cm_6_22&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}",
            "IGN_OrthosHighRes": "https://data.geopf.fr/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=THR.ORTHOIMAGERY.ORTHOPHOTOS&STYLE=normal&FORMAT=image%2Fjpeg&TILEMATRIXSET=PM_6_21&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}",
            "IGN_OrthoHistorique": "https://data.geopf.fr/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=ORTHOIMAGERY.ORTHOPHOTOS.1950-1965&STYLE=BDORTHOHISTORIQUE&FORMAT=image%2Fpng&TILEMATRIXSET=PM_0_18&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}",
            "IGN_ES": "https://www.ign.es/wmts/mapa-raster?layer=MTN&style=default&tilematrixset=GoogleMapsCompatible&Service=WMTS&Request=GetTile&Version=1.0.0&Format=image/jpeg&TileMatrix={z}&TileCol={x}&TileRow={y}",
            "IGN_ES_LIDAR": "https://wmts-mapa-lidar.idee.es/lidar?Version=1.0.0&layer=EL.GridCoverageDSM&style=default&tilematrixset=GoogleMapsCompatible&Service=WMTS&Request=GetTile&Format=image/png&TileMatrix={z}&TileCol={x}&TileRow={y}",
            "IGN_ES_Ortho": "https://www.ign.es/wmts/pnoa-ma?layer=OI.OrthoimageCoverage&style=default&tilematrixset=GoogleMapsCompatible&Service=WMTS&Request=GetTile&Version=1.0.0&Format=image/jpeg&TileMatrix={z}&TileCol={x}&TileRow={y}",
        }

    def get_layers(self):
        return self.layers

    def get_layer_names(self):
        return sorted(list(self.layers.keys()))

    def get_layer(self, layer_name):
        layer = self.layers.get(layer_name)
        if layer is None:
            raise ValueError(f"Layer {layer_name} not found in catalog")
        return layer
