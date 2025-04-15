class LayerCatalog:
    def __init__(self):
        self.layers = {
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
            "IGN Topo": "https://data.geopf.fr/private/wmts?apikey=ign_scan_ws&SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=GEOGRAPHICALGRIDSYSTEMS.MAPS&STYLE=normal&TILEMATRIXSET=PM&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}&FORMAT=image%2Fjpeg",
        }

    def get_layers(self):
        return self.layers

    def get_layer_names(self):
        return sorted(list(self.layers.keys()))

    def get_layer(self, layer_name):
        return self.layers.get(layer_name)
