"""Main module."""

import ipyleaflet


class Map(ipyleaflet.Map):
    def __init__(self, center=[20, 0], zoom=2, height="600px", **kwargs):
        super().__init__(center=center, zoom=zoom, **kwargs)
        self.layout.height = height
        self.scroll_wheel_zoom = True

    def add_basemap(self, basemap="OpenStreetMap"):
        """Add a basemap to the map.

        Args:
            basemap (str, optional): Basemap name. Defaults to "OpenStreetMap".
        """

        url = eval(f"ipyleaflet.basemaps.{basemap}").build_url()
        layer = ipyleaflet.TileLayer(url=url, name=basemap)
        self.add_layer(layer)

    def add_google_map(self, map_type="ROADMAP"):
        """Add a Google Map to the map.

        Args:
            map_type (str, optional): Map type. Defaults to "ROADMAP".
        """

        map_types = {
            "ROADMAP": "m",
            "SATELLITE": "s",
            "HYBRID": "y",
            "TERRAIN": "p",
        }
        map_type = map_types[map_type.upper()]

        url = (
            f"https://mt1.google.com/vt/lyrs={map_type.lower()}&x={{x}}&y={{y}}&z={{z}}"
        )
        layer = ipyleaflet.TileLayer(url=url, name="Google Map")
        self.add(layer)

    def add_geojson(self, data, zoom_to_layer=True, hover_style=None, **kwargs):
        """
        Add a GeoJSON layer to the map.

        Args:
            data (str or dict): The GeoJSON data. Can be a file path (str) or a dictionary.
            zoom_to_layer (bool, optional): Whether to zoom to the layer's bounds. Defaults to True.
            hover_style (dict, optional): Style applied when hovering over the layer. Defaults to {"color": "yellow", "fillOpacity": 0.2}.
            **kwargs: Additional keyword arguments for the ipyleaflet.GeoJSON layer.

        Raises:
            ValueError: If the data type is invalid.
        """
        import geopandas as gpd

        if hover_style is None:
            hover_style = {"color": "yellow", "fillOpacity": 0.2}
        if isinstance(data, str):
            gdf = gpd.read_file(data)
            geojson = gdf.__geo_interface__
        elif isinstance(data, dict):
            geojson = data
        layer = ipyleaflet.GeoJSON(data=geojson, hover_style=hover_style, **kwargs)
        self.add_layer(layer)

        if zoom_to_layer:
            bounds = gdf.total_bounds
            self.fit_bounds([[bounds[1], bounds[0]], [bounds[3], bounds[2]]])

    def add_shp(self, data, **kwargs):
        """
        Add a shapefile to the map.

        Args:
            data (str): The file path to the shapefile.
            **kwargs: Additional keyword arguments for the GeoJSON layer.
        """
        import geopandas as gpd

        gdf = gpd.read_file(data)
        gdf = gdf.to_crs(epsg=4326)
        geojson = gdf.__geo_interface__
        self.add_geojson(geojson, **kwargs)

    def add_gdf(self, gdf, **kwargs):
        """
        Add a GeoDataFrame to the map.

        Args:
            gdf (geopandas.GeoDataFrame): The GeoDataFrame to add.
            **kwargs: Additional keyword arguments for the GeoJSON layer.
        """
        gdf = gdf.to_crs(epsg=4326)
        geojson = gdf.__geo_interface__
        self.add_geojson(geojson, **kwargs)

    def add_vector(self, data, **kwargs):
        """
        Add vector data to the map.

        Args:
            data (str, geopandas.GeoDataFrame, or dict): The vector data. Can be a file path (str), a GeoDataFrame, or a GeoJSON dictionary.
            **kwargs: Additional keyword arguments for the layer.

        Raises:
            ValueError: If the data type is invalid.
        """
        import geopandas as gpd

        if isinstance(data, str):
            gdf = gpd.read_file(data)
            self.add_shp(gdf, **kwargs)
        elif isinstance(data, gpd.GeoDataFrame):
            self.add_gdf(data, **kwargs)
        elif isinstance(data, dict):
            self.add_geojson(data, **kwargs)
        else:
            raise ValueError("Invalid data type")

    def add_layer_control(self):
        """
        Add a layer control widget to the map.

        The layer control allows users to toggle the visibility of layers.
        """
        control = ipyleaflet.LayersControl(position="topright")
        self.add_control(control)

    # def add_raster(self, filepath, **kwargs):

    #     from localtileserver import TileClient, get_leaflet_tile_layer
    #     from ipyleaflet import Map

    #     client = TileClient(filepath)
    #     tile_layer = get_leaflet_tile_layer(client, **kwargs)

    #     self.add(tile_layer)
    #     self.center = client.center()
    #     self.zoom = client.default_zoom

    def add_raster(self, raster_source, name=None, **kwargs):
        """
        Adds a raster tile layer to the map from a file path or URL.

        Args:
            raster_source (str): File path or URL to the raster.
            name (str, optional): Optional name for the raster layer.
            **kwargs: Additional arguments passed to the tile layer.
        """
        from localtileserver import TileClient, get_leaflet_tile_layer
        import os

        # Check if it's a URL or a file path
        if raster_source.startswith("http") or os.path.exists(raster_source):
            client = TileClient(raster_source)
            layer = get_leaflet_tile_layer(client, **kwargs)
        else:
            raise ValueError("Invalid raster source. Provide a valid URL or file path.")

        # Optionally name the layer
        if name:
            layer.name = name

        # Add to map
        self.add(layer)

        # Center the map once on the first layer
        if not getattr(self, "_has_centered", False):
            self.center = client.center()
            self.zoom = client.default_zoom
            self._has_centered = True
