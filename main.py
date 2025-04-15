from io import BytesIO
from map_custom import MapFoliumCustom
from layer_catalog import LayerCatalog
from shapely.geometry import Polygon
from streamlit_folium import st_folium
import contextily as ctx
import geopandas as gpd
import matplotlib.pyplot as plt
import streamlit as st


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    st.title("Download Tiles to PNG")
    st.write("Draw a rectangle on the map to download the tiles to PNG image")
    m = MapFoliumCustom(add_draw_control=True).get_map()

    # call to render Folium map in Streamlit
    st_data = st_folium(m, use_container_width=True)
    # st.write(st_data)

    last_active_drawing = st_data.get("last_active_drawing")

    if last_active_drawing is not None:
        last_active_drawing_geometry = last_active_drawing.get("geometry")
        type = last_active_drawing_geometry.get("type")
        coordinates = last_active_drawing_geometry.get("coordinates")

        current_zoom = st_data.get("zoom")
        current_center = st_data.get("center")

        # Create a Polygon wkt from the coordinates
        if type == "Polygon":
            wkt = "POLYGON(("
            for i in range(len(coordinates[0])):
                wkt += (
                    str(coordinates[0][i][0]) + " " + str(coordinates[0][i][1]) + ", "
                )
            wkt = wkt[:-2] + "))"
            # Create bbox from the coordinates using shapely

            polygon = Polygon(coordinates[0])
            bbox = polygon.bounds

            # Compute Area
            gdf = gpd.GeoDataFrame(index=[0], crs="EPSG:4326", geometry=[polygon])
            gdf = gdf.to_crs(epsg=2154)
            area = gdf.area[0]  # in square meters
            area_km2 = area / 1000000  # in square kilometers
            st.write(f"Area (km2): {area_km2:.2f}")

            min_lon, min_lat, max_lon, max_lat = bbox
            w, s, e, n = min_lon, min_lat, max_lon, max_lat

            # st.write("Current zoom level:", current_zoom)
            zoom_level = st.slider("Zoom level", 0, 27, current_zoom)
            st.write("Zoom level selected:", zoom_level)

            layer_catalog = LayerCatalog()
            layer_names = layer_catalog.get_layer_names()
            layer_name = st.selectbox("Select a layer", layer_names)

            source_url = layer_catalog.get_layer(layer_name)
            st.write("Source URL:", source_url)

            ll = True
            n_connections = 10

            button_download = st.button("Generate Download Link")
            if button_download:
                st.write("Downloading tiles ...")

                # Get the tiles using contextily
                img, extent = ctx.bounds2img(
                    w,
                    s,
                    e,
                    n,
                    zoom=zoom_level,
                    source=source_url,
                    ll=ll,
                    n_connections=n_connections,
                )

                # Create a BinaryIO object to write the image to

                img_io = BytesIO()
                plt.imsave(img_io, img)

                # Get the bytes from the BinaryIO object, and create a download button
                img_bytes = img_io.getvalue()
                st.download_button(
                    label="Download image as PNG",
                    data=img_bytes,
                    file_name="geo.png",
                    mime="image/png",
                )
