# Welcome to geonexus


[![image](https://img.shields.io/pypi/v/geonexus.svg)](https://pypi.python.org/pypi/geonexus)
[![image](https://static.pepy.tech/badge/geonexus)](https://pepy.tech/project/geonexus)
[![image](https://github.com/halieute/geonexus/workflows/docs/badge.svg)](https://halieute.github.io/geonexus/)
[![image](https://github.com/halieute/geonexus/workflows/Linux%20build/badge.svg)](https://github.com/halieute/geonexus/actions)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/halieute/geonexus/main.svg)](https://results.pre-commit.ci/latest/github/halieute/geonexus/main)
[![image](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![image](https://img.shields.io/conda/vn/conda-forge/geonexus.svg)](https://anaconda.org/conda-forge/geonexus)

**A Python package for geospatial analysis and interactive mapping in a Jupyter environment.**

-   GitHub repo: <https://github.com/halieute/geonexus>
-   Documentation: <https://halieute.github.io/geonexus/>
-   PyPI: <https://pypi.org/project/geonexus/>
-   Conda-forge: <https://anaconda.org/conda-forge/geonexus>
-   Free software: [MIT license](https://opensource.org/licenses/MIT)

## Introduction

**Geonexus** is a Python package for interactive mapping and geospatial analysis with minimal coding in a Jupyter environment. It is a project which was designed specifically to work with geospatial and climate data. Geonexus is designed to faciliatete geospatial data analysis for users.  It is a free and open-source Python package that enables users to analyze and visualize geospatial data with minimal coding in a Jupyter environment, such as Google Colab, Jupyter Notebook, JupyterLab, and [marimo](https://github.com/marimo-team/marimo). Leafmap is built upon several open-source packages, such as [folium](https://github.com/python-visualization/folium) and [ipyleaflet](https://github.com/jupyter-widgets/ipyleaflet) (for creating interactive maps), [WhiteboxTools](https://github.com/jblindsay/whitebox-tools) and [whiteboxgui](https://github.com/opengeos/whiteboxgui) (for analyzing geospatial data), and [ipywidgets](https://github.com/jupyter-widgets/ipywidgets) (for designing interactive graphical user interface [GUI]). Geonexus has a toolset with various interactive tools that allow users to load vector and raster data onto the map __without coding__. In addition, users can use the powerful analytical backend (i.e., WhiteboxTools) to perform geospatial analysis directly within the geonexus user interface without writing a single line of code. The WhiteboxTools library currently contains **500+** tools for advanced geospatial analysis, such as [GIS Analysis] (https://jblindsay.github.io/wbt_book/available_tools/gis_analysis.html), [Geomorphometric Analysis](https://jblindsay.github.io/wbt_book/available_tools/geomorphometric_analysis.html), [Hydrological Analysis](https://jblindsay.github.io/wbt_book/available_tools/hydrological_analysis.html), [LiDAR Data Analysis](https://jblindsay.github.io/wbt_book/available_tools/lidar_tools.html), [Mathematical and Statistical Analysis](https://jblindsay.github.io/wbt_book/available_tools/mathand_stats_tools.html), and [Stream Network Analysis](https://jblindsay.github.io/wbt_book/available_tools/stream_network_analysis.html).

## Acknowledgments



## Statement of Need

There is a plethora of Python packages for geospatial analysis, such as [geopandas](https://geopandas.org) for vector data analysis and [xarray](https://docs.xarray.dev) for raster data analysis. As listed at [pyviz.org](https://pyviz.org), there are also many options for plotting data on a map in Python, ranging from libraries focused specifically on maps like [ipyleaflet](https://ipyleaflet.readthedocs.io) and [folium](https://python-visualization.github.io/folium) to general-purpose plotting tools that also support geospatial data types, such as [hvPlot](https://hvplot.pyviz.org), [bokeh](http://bokeh.org), and [plotly](https://plotly.com/python). While these tools provide powerful capabilities, displaying geospatial data from different file formats on an interactive map and performing basic analyses can be challenging, especially for users with limited coding skills. Furthermore, many tools lack bi-directional communication between the frontend (browser) and the backend (Python), limiting their interactivity and usability for exploring map data.

Geonexus addresses these challenges by leveraging the bidirectional communication provided by ipyleaflet, enabling users to load and visualize geospatial datasets with just few lines of code. Geonexus also provides an interactive graphical user interface (GUI) for loading geospatial datasets. It is designed for anyone who wants to analyze and visualize geospatial data interactively in a Jupyter environment, making it particularly accessible for novice users with limited programming skills. Advanced programmers can also benefit from geonexus for geospatial data analysis and building interactive web applications.

## Usage

Launch the interactive notebook tutorial for the **geonexus** Python package with Google Colab, Binder, or Amazon Sagemaker Studio Lab now:


## Key Features

Geonexus offers a wide range of features and capabilities that empower geospatial data scientists, researchers, and developers to unlock the potential of their data. Some of the key features include:

-   **Creating an interactive map with just one line of code:** Geonexus makes it easy to create an interactive map by providing a simple API that allows you to load and visualize geospatial datasets with minimal coding.

-   **Switching between different mapping backends:** Geonexus can supports multiple mapping backends, including ipyleaflet, folium, kepler.gl, pydeck, and bokeh. You can switch between these backends to create maps with different visualization styles and capabilities.

-   **Changing basemaps interactively:** Geonexus allows you to change basemaps interactively, providing a variety of options such as OpenStreetMap, Stamen Terrain, CartoDB Positron, and many more.

-   **Adding XYZ, WMS, and vector tile services:** You can easily add XYZ, WMS, and vector tile services to your map, allowing you to overlay additional geospatial data from various sources.

-   **Displaying vector data:** Geonexus supports various vector data formats, including Shapefile, GeoJSON, GeoPackage, and any vector format supported by GeoPandas. You can load and display vector data on the map, enabling you to visualize and analyze spatial features.

-   **Displaying raster data:** Geonexus allows you to load and display raster data, such as GeoTIFFs, on the map. This feature is useful for visualizing satellite imagery, digital elevation models, and other gridded datasets.

-   **Creating custom legends and colorbars:** Geonexus provides tools for customizing legends and colorbars on the map, allowing you to represent data values with different colors and corresponding labels.

-   **Creating split-panel maps and linked maps:** With Geonexus, you can create split-panel maps to compare different datasets side by side. You can also create linked maps that synchronize interactions between multiple maps, providing a coordinated view of different spatial data.

-   **Downloading and visualizing OpenStreetMap data:** Geonexus allows you to download and visualize OpenStreetMap data, providing access to detailed street maps, buildings, and other points of interest.

-   **Creating and editing vector data interactively:** Geonexus includes tools for creating and editing vector data interactively on the map. You can draw points, lines, and polygons, and modify them as needed.

-   **Searching for geospatial data:** Geonexus will provide functionality for searching and accessing geospatial data from sources such as SpatialTemporal Asset Catalogs (STAC), Microsoft Planetary Computer, AWS Open Data Registry, and OpenAerialMap.

-   **Inspecting pixel values interactively:** Geonexus allows you to interactively inspect pixel values in raster datasets, helping you analyze and understand the data at a more granular level.

-   **Creating choropleth maps and heat maps:** Geonexus supports the creation of choropleth maps, where colors represent different data values for specific geographic areas. You can also create heat maps to visualize data density.

-   **Displaying data from a PostGIS database:** Geonexus provides tools for connecting to a PostGIS database and displaying spatial data stored in the database on the map.

-   **Creating time series animations:** Geonexus enables the creation of time series animations from both vector and raster data, allowing you to visualize temporal changes in your geospatial datasets.

-   **Analyzing geospatial data with whitebox:** Geonexus integrates with WhiteboxTools and whiteboxgui, providing a suite of geospatial analyses, such as hydrological analysis, terrain analysis, and LiDAR processing.

-   **Segmenting and classifying remote sensing imagery:** Geonexus integrates the segment-geospatial package, which provides tools for segmenting and classifying remote sensing imagery using deep learning algorithms.

-   **Building interactive web apps:** Geonexus supports the development of interactive web applications using frameworks like Voila, Streamlit, and Solara. This allows you to share your geospatial analyses and visualizations with others in a user-friendly web interface.

These features and capabilities make geonexus a powerful tool for geospatial data exploration, analysis, and visualization. Whether you are a beginner or an experienced geospatial data scientist, geonexus provides an accessible and efficient way to work with geospatial data in Python.
