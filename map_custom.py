from folium import Map, LayerControl, TileLayer
from folium.plugins import MiniMap, Fullscreen, DualMap, Geocoder, LocateControl, Draw


class MapFoliumCustom:
    def __init__(self):
        self.max_zoom = 26
        self.initial_location = [47, 2.5]
        self.initial_zoom = 6
        self.map = self.create_map()

    def create_map(self):
        # Define the maximum zoom level
        # Create a map object centered at a specific latitude and longitude with a zoom level
        # Initial location on middle of France
        self.map = Map(location=self.initial_location, zoom_start=self.initial_zoom)
        # Add OpenStreetMap as a base map
        self.add_layer(self.get_openstreetmap_layer())
        # Add IGN orthophoto as a base map
        self.add_layer(self.get_ign_orthophoto_layer())
        # Add ESRI World Imagery as a base map
        self.add_layer(self.get_esri_layer())
        # Add Google Satellite as a base map
        self.add_layer(self.get_google_satellite_layer())
        # Add Google Hybrid as a base map
        self.add_layer(self.get_google_hybrid_layer())
        # Add Google Terrain as a base map
        self.add_layer(self.get_google_terrain_layer())
        # Add Google Roadmap as a base map
        self.add_layer(self.get_google_road_layer())
        # Add OpenTopoMap
        self.add_layer(self.get_opentopomap_layer())
        # Add OpenCycleMap
        self.add_layer(self.get_opencyclemap_layer())
        # Add CyclOSM
        self.add_layer(self.get_cyclosm_layer())
        # Add Windy
        self.add_layer(self.get_windy_tourist_layer())
        # ----------------------------------------------------
        # add IGN topo
        self.add_layer(self.get_ign_topo_layer())
        # add MNT IGN
        self.add_layer(self.get_ign_mnt_layer())
        # Add MNS IGN
        self.add_layer(self.get_ign_mns_layer())
        # ----------------------------------------------------
        # Add OpenRailwayMap
        self.add_layer(self.get_openrailwaymap_layer(show=True))
        # Add WaymarkedTrails
        self.add_layer(self.get_waymarkedtrails_layer())
        # Add layer control to the map
        self.add_layer(LayerControl())
        # Add minimap to the map
        self.add_layer(self.get_minimap(minimized=True))
        # Add geocoder to the map
        self.add_layer(self.get_geocoder())
        # Add fullscreen button to the map
        self.add_layer(self.get_full_screen())
        # Add locate control to the map
        self.add_layer(self.get_locate_control())
        # Add draw control to the map
        self.add_layer(self.get_draw_control())

        return self.map

    def create_dual_map(self):
        self.map = DualMap(
            location=self.initial_location,
            zoom_start=self.initial_zoom,
            layout="horizontal",
        )

        # Add OpenStreetMap as a base map
        self.add_layer(self.get_openstreetmap_layer())
        # Add IGN orthophoto as a base map
        self.add_layer(self.get_ign_orthophoto_layer())
        # Add ESRI World Imagery as a base map
        self.add_layer(self.get_esri_layer())
        # Add Google Satellite as a base map
        self.add_layer(self.get_google_satellite_layer())
        # Add Google Hybrid as a base map
        self.add_layer(self.get_google_hybrid_layer())
        # Add Google Terrain as a base map
        self.add_layer(self.get_google_terrain_layer())
        # Add Google Roadmap as a base map
        self.add_layer(self.get_google_road_layer())
        # Add OpenTopoMap
        self.add_layer(self.get_opentopomap_layer())
        # Add OpenCycleMap
        self.add_layer(self.get_opencyclemap_layer())
        # Add CyclOSM
        self.add_layer(self.get_cyclosm_layer())
        # Add Windy
        self.add_layer(self.get_windy_tourist_layer())

        # Now, add layers to the first map (m1)
        self.add_layer_m1(self.get_ign_mns_layer())
        self.add_layer_m1(self.get_ign_mnt_layer())

        # Now add layers to the second map (m2)
        self.add_layer_m2(self.get_ign_topo_layer(show=True))

        # Now add layers to both maps
        # Add OpenRailwayMap
        self.add_layer(self.get_openrailwaymap_layer())
        # Add WaymarkedTrails
        self.add_layer(self.get_waymarkedtrails_layer())

        # Add layer control to the map
        self.add_layer(LayerControl())
        # Add minimap to the map
        self.add_layer(self.get_minimap(minimized=True))
        # Add geocoder to the map
        self.add_layer(self.get_geocoder())
        # Add fullscreen button to the map
        self.add_layer(self.get_full_screen())
        # Add locate control to the map
        self.add_layer(self.get_locate_control())
        # Add draw control to the map
        self.add_layer(self.get_draw_control())

        return self.map

    def get_map(self):
        return self.map

    def add_layer(self, layer):
        layer.add_to(self.map)

    def add_layer_m1(self, layer):
        layer.add_to(self.map.m1)

    def add_layer_m2(self, layer):
        layer.add_to(self.map.m2)

    def get_minimap(self, minimized: bool = False):
        minimap = MiniMap(
            location=self.initial_location,
            tiles="OpenStreetMap",
            control_orientation="vertical",
            zoom_start=self.initial_zoom,
            position="bottomleft",
            toggle_display=True,
            auto_toggle_display=False,
            minimized=minimized,
        )

        return minimap

    def get_geocoder(self):
        return Geocoder(position="topleft", collapsed=True)

    def get_full_screen(self):
        return Fullscreen()

    def get_locate_control(self):
        return LocateControl(auto_start=True, position="bottomleft")

    def get_draw_control(self):
        return Draw(export=True, position="topleft", show_geometry_on_click=False)

    def get_openstreetmap_layer(self):
        return TileLayer("OpenStreetMap", max_zoom=self.max_zoom, show=False)

    def get_esri_layer(self):
        return TileLayer(
            "Esri.WorldImagery",
            max_zoom=self.max_zoom,
            visible=False,
            overlay=False,
            control=True,
            show=False,
            name="ESRI World Imagery",
        )

    def get_ign_orthophoto_layer(self):
        # Add WMTS Layer for IGN orthophoto
        wmts_url = (
            "https://data.geopf.fr/wmts?"
            "&REQUEST=GetTile&SERVICE=WMTS&VERSION=1.0.0"
            "&STYLE=normal"
            "&TILEMATRIXSET=PM"
            "&FORMAT=image/jpeg"
            "&LAYER=ORTHOIMAGERY.ORTHOPHOTOS"
            "&TILEMATRIX={z}"
            "&TILEROW={y}"
            "&TILECOL={x}"
        )

        layer_ortho = TileLayer(
            wmts_url,
            attr="IGN",
            min_zoom=0,
            max_native_zoom=18,
            max_zoom=self.max_zoom,
            tile_size=256,
            name="IGN Orthophoto",
            visible=False,
            overlay=False,
            control=True,
            show=False,
        )

        return layer_ortho

    def get_google_terrain_layer(self):
        # Add Google Terrain layer
        layer_google_terrain = TileLayer(
            "https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}",
            attr="Google",
            min_zoom=0,
            max_zoom=self.max_zoom,
            name="Google Terrain",
            visible=False,
            overlay=False,
            control=True,
            show=False,
        )
        return layer_google_terrain

    def get_google_hybrid_layer(self):
        # Add Google Hybrid layer
        layer_google_hybrid = TileLayer(
            "https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
            attr="Google",
            min_zoom=0,
            max_zoom=self.max_zoom,
            name="Google Hybrid",
            visible=False,
            overlay=False,
            control=True,
            show=True,  # Set this layer as the default visible layer
        )
        return layer_google_hybrid

    def get_google_road_layer(self):
        # Add Google Road layer
        layer_google_road = TileLayer(
            "https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
            attr="Google",
            min_zoom=0,
            max_zoom=self.max_zoom,
            name="Google Road",
            visible=False,
            overlay=False,
            control=True,
            show=False,
        )
        return layer_google_road

    def get_google_satellite_layer(self):

        # Add Google Satellite layer
        layer_google_satellite = TileLayer(
            "http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}",
            attr="Google",
            min_zoom=0,
            max_native_zoom=20,
            max_zoom=self.max_zoom,
            tile_size=256,
            name="Google Satellite",
            visible=False,
            overlay=False,
            control=True,
            show=False,
        )

        return layer_google_satellite

    def get_ign_topo_layer(self, show: bool = False, api_key: str = "ign_scan_ws"):

        url_topo = f"https://data.geopf.fr/private/wmts?apikey={api_key}&SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=GEOGRAPHICALGRIDSYSTEMS.MAPS&STYLE=normal&TILEMATRIXSET=PM&TILEMATRIX={{z}}&TILEROW={{y}}&TILECOL={{x}}&FORMAT=image%2Fjpeg"

        layer_topo25 = TileLayer(
            url_topo,
            attr="IGN",
            min_zoom=15,
            max_native_zoom=16,
            max_zoom=self.max_zoom,
            tile_size=256,
            name="IGN Topo",
            visible=False,
            overlay=True,
            control=True,
            show=show,
        )

        return layer_topo25

    def get_ign_mnt_layer(self):

        # Add LiDAR HD MNT layer using the constructed LiDAR URL

        lidar_url = (
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
        )

        layer_lidar_mnt = TileLayer(
            lidar_url,
            attr="IGN",
            min_zoom=0,
            max_native_zoom=18,
            max_zoom=self.max_zoom,
            tile_size=256,
            name="MNT LiDAR HD",
            visible=False,
            overlay=True,
            control=True,
            show=False,
        )

        return layer_lidar_mnt

    def get_opentopomap_layer(self):
        # This layer is not working well
        # Add OpenTopoMap layer
        layer_opentopomap = TileLayer(
            "https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png",
            attr="OpenTopoMap",
            min_zoom=0,
            max_zoom=self.max_zoom,
            name="OpenTopoMap",
            visible=False,
            overlay=False,
            control=True,
            show=False,
        )
        return layer_opentopomap

    def get_opencyclemap_layer(self):
        # Add OpenCycleMap layer
        layer_opencyclemap = TileLayer(
            "https://{s}.tile.thunderforest.com/cycle/{z}/{x}/{y}.png",
            attr="OpenCycleMap",
            min_zoom=0,
            max_zoom=self.max_zoom,
            name="OpenCycleMap",
            visible=False,
            overlay=False,
            control=True,
            show=False,
        )
        return layer_opencyclemap

    def get_cyclosm_layer(self):
        # Add CyclOSM layer
        layer_cyclosm = TileLayer(
            "https://{s}.tile-cyclosm.openstreetmap.fr/cyclosm/{z}/{x}/{y}.png",
            attr="CyclOSM",
            min_zoom=0,
            max_zoom=self.max_zoom,
            name="CyclOSM",
            visible=False,
            overlay=False,
            control=True,
            show=False,
        )
        return layer_cyclosm

    def get_ign_mns_layer(self):

        # Add MNS LiDAR HD layer using the constructed MNS URL
        mns_url = (
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
        )
        layer_mns = TileLayer(
            mns_url,
            attr="IGN",
            min_zoom=0,
            max_native_zoom=18,
            max_zoom=self.max_zoom,
            tile_size=256,
            name="MNS LiDAR HD",
            visible=False,
            overlay=True,
            control=True,
            show=True,
        )
        return layer_mns

    def get_openrailwaymap_layer(self, show: bool = False):
        # Add OpenRailwayMap layer
        layer_openrailwaymap = TileLayer(
            "https://tiles.openrailwaymap.org/standard/{z}/{x}/{y}.png",
            attr="OpenRailwayMap",
            min_zoom=0,
            max_native_zoom=18,
            max_zoom=self.max_zoom,
            tile_size=256,
            name="OpenRailwayMap",
            visible=True,
            overlay=True,
            control=True,
            show=show,  # Show by default
        )
        return layer_openrailwaymap

    def get_waymarkedtrails_layer(self):
        # Add Waymarked Trails layer
        layer_waymarkedtrails = TileLayer(
            "https://tile.waymarkedtrails.org/hiking/{z}/{x}/{y}.png",
            attr="Waymarked Trails",
            min_zoom=0,
            max_native_zoom=18,
            max_zoom=self.max_zoom,
            tile_size=256,
            name="Waymarked Trails",
            visible=True,
            overlay=True,
            control=True,
            show=False,
        )
        return layer_waymarkedtrails

    def get_windy_tourist_layer(self):
        # Add Windy layer
        layer_windy = TileLayer(
            "https://windytiles.mapy.cz/turist-m/{z}-{x}-{y}.png",
            attr="Windy",
            min_zoom=0,
            max_native_zoom=18,
            max_zoom=self.max_zoom,
            tile_size=256,
            name="WindyTouristMap",
            visible=True,
            overlay=False,
            control=True,
            show=False,
        )
        return layer_windy
