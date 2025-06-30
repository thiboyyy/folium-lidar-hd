from folium import Map, LayerControl, TileLayer
from folium.plugins import MiniMap, Fullscreen, DualMap, Geocoder, LocateControl, Draw
from layer_catalog import LayerCatalog


class MapFoliumCustom:
    def __init__(self, add_draw_control=False):
        self.max_zoom = 26
        self.initial_location = [47, 2.5]
        self.initial_zoom = 6
        self.layer_catalog = LayerCatalog()
        self.map = self.create_map(add_draw_control)

    def create_map(self, add_draw_control=False):
        # Create a map object centered at a specific latitude and longitude with a zoom level
        # Define the maximum zoom level
        # Create a map object centered at a specific latitude and longitude with a zoom level
        # Initial location on middle of France
        self.map = Map(location=self.initial_location, zoom_start=self.initial_zoom)
        # Add OpenStreetMap as a base map
        self.add_layer(self.get_openstreetmap_layer())
        # Add IGN orthophoto as a base map
        self.add_layer(self.get_ign_orthophoto_layer())
        # Add IGN orthophoto as a base map
        self.add_layer(self.get_ign_orthohighres_layer())
        # Add IGN orthophoto as a base map
        self.add_layer(self.get_ign_orthohistoric_layer())
        # Add IGN orthophoto as a base map
        # self.add_layer(self.get_ign_pcrs_layer())
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
        # Add MapantFR
        self.add_layer(self.get_mapant_layer())
        # Add IGNE
        self.add_layer(self.get_igne())
        # Add IGNEL
        self.add_layer(self.get_ignel())
        # Add IGNEO
        self.add_layer(self.get_igneo())
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
        if add_draw_control:
            self.add_layer(self.get_draw_control())

        return self.map

    def create_dual_map(self, add_draw_control=False):
        self.map = DualMap(
            location=self.initial_location,
            zoom_start=self.initial_zoom,
            layout="horizontal",
        )

        # Add OpenStreetMap as a base map
        self.add_layer(self.get_openstreetmap_layer())
        # Add IGN orthophoto as a base map
        self.add_layer(self.get_ign_orthophoto_layer())
        # Add IGN orthophoto as a base map
        self.add_layer(self.get_ign_orthohighres_layer())
        # Add IGN orthophoto as a base map
        self.add_layer(self.get_ign_orthohistoric_layer())
        # Add IGN orthophoto as a base map
        # self.add_layer(self.get_ign_pcrs_layer())
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
        # Add MapantFR
        self.add_layer(self.get_mapant_layer())
        # Add IGNE
        self.add_layer(self.get_igne())
        # Add IGNEL
        self.add_layer(self.get_ignel())
        # Add IGNEO
        self.add_layer(self.get_igneo())

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
        if add_draw_control:
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
        wmts_url = self.layer_catalog.get_layer("IGN Orthophoto")

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
        layer_url = self.layer_catalog.get_layer("Google Terrain")
        layer_google_terrain = TileLayer(
            tiles=layer_url,
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
        layer_url = self.layer_catalog.get_layer("Google Hybrid")
        layer_google_hybrid = TileLayer(
            tiles=layer_url,
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
        layer_url = self.layer_catalog.get_layer("Google Roadmap")
        layer_google_road = TileLayer(
            tiles=layer_url,
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

        # Add Google Satellite
        layer_url = self.layer_catalog.get_layer("Google Satellite")
        layer_google_satellite = TileLayer(
            tiles=layer_url,
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

    def get_ign_pcrs_layer(self):
        layer_url = self.layer_catalog.get_layer("IGN_PCRS")
        layer_ortho = TileLayer(
            layer_url,
            attr="IGN",
            min_zoom=0,
            max_native_zoom=22,
            max_zoom=self.max_zoom,
            tile_size=256,
            name="IGN_PCRS",
            visible=False,
            overlay=False,
            control=True,
            show=False,
        )
        return layer_ortho

    def get_igne(self):
        layer_url = self.layer_catalog.get_layer("IGN_ES")
        layer_ortho = TileLayer(
            layer_url,
            attr="IGN_ES",
            min_zoom=0,
            max_native_zoom=22,
            max_zoom=self.max_zoom,
            tile_size=256,
            name="IGN_ES",
            visible=False,
            overlay=False,
            control=True,
            show=False,
        )
        return layer_ortho

    def get_ignel(self):
        layer_url = self.layer_catalog.get_layer("IGN_ES_LIDAR")
        layer_ortho = TileLayer(
            layer_url,
            attr="IGN_ES_LIDAR",
            min_zoom=0,
            max_native_zoom=22,
            max_zoom=self.max_zoom,
            tile_size=256,
            name="IGN_ES_LIDAR",
            visible=False,
            overlay=True,
            control=True,
            show=False,
        )
        return layer_ortho

    def get_igneo(self):
        layer_url = self.layer_catalog.get_layer("IGN_ES_Ortho")
        layer_ortho = TileLayer(
            layer_url,
            attr="IGN_ES_Ortho",
            min_zoom=0,
            max_native_zoom=22,
            max_zoom=self.max_zoom,
            tile_size=256,
            name="IGN_ES_Ortho",
            visible=False,
            overlay=False,
            control=True,
            show=False,
        )
        return layer_ortho

    def get_ign_orthohighres_layer(self):
        layer_url = self.layer_catalog.get_layer("IGN_OrthosHighRes")
        layer_ortho = TileLayer(
            layer_url,
            attr="IGN",
            min_zoom=0,
            max_native_zoom=21,
            max_zoom=self.max_zoom,
            tile_size=256,
            name="IGN_OrthosHighRes",
            visible=False,
            overlay=False,
            control=True,
            show=False,
        )
        return layer_ortho

    def get_ign_orthohistoric_layer(self):
        layer_url = self.layer_catalog.get_layer("IGN_OrthoHistorique")
        layer_ortho = TileLayer(
            layer_url,
            attr="IGN",
            min_zoom=0,
            max_native_zoom=18,
            max_zoom=self.max_zoom,
            tile_size=256,
            name="IGN_OrthoHistorique",
            visible=False,
            overlay=False,
            control=True,
            show=False,
        )
        return layer_ortho

    def get_ign_topo_layer(self, show: bool = False):
        # Add IGN Topo layer
        url_topo = self.layer_catalog.get_layer("IGN Topo")
        layer_topo25 = TileLayer(
            url_topo,
            attr="IGN",
            min_zoom=6,
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

        lidar_url = self.layer_catalog.get_layer("IGN MNT")

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
        layer_url = self.layer_catalog.get_layer("OpenTopoMap")
        layer_opentopomap = TileLayer(
            layer_url,
            attr="OpenTopoMap",
            min_zoom=0,
            max_zoom=self.max_zoom,
            max_native_zoom=16,
            name="OpenTopoMap",
            visible=False,
            overlay=False,
            control=True,
            show=False,
        )
        return layer_opentopomap

    def get_opencyclemap_layer(self):
        # Add OpenCycleMap layer
        layer_url = self.layer_catalog.get_layer("OpenCycleMap")
        layer_opencyclemap = TileLayer(
            layer_url,
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
        layer_url = self.layer_catalog.get_layer("CyclOSM")
        layer_cyclosm = TileLayer(
            layer_url,
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

        layer_url = self.layer_catalog.get_layer("IGN MNS")

        layer_mns = TileLayer(
            layer_url,
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
        layer_url = self.layer_catalog.get_layer("OpenRailwayMap")
        # Add OpenRailwayMap layer
        layer_openrailwaymap = TileLayer(
            layer_url,
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

    def get_mapant_layer(self):
        # Add Mapant layer
        layer_url = self.layer_catalog.get_layer("MapantFR")
        layer_mapant = TileLayer(
            tiles=layer_url,
            attr="Mapant",
            min_zoom=2,
            max_zoom=self.max_zoom,
            name="MapantFR",
            visible=True,
            overlay=True,
            control=True,
            show=False,
        )
        return layer_mapant

    def get_waymarkedtrails_layer(self):
        # Add Waymarked Trails layer
        layer_url = self.layer_catalog.get_layer("WayMarkedTrails")
        layer_waymarkedtrails = TileLayer(
            layer_url,
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
        layer_url = self.layer_catalog.get_layer("WindyTouristMap")
        layer_windy = TileLayer(
            layer_url,
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
