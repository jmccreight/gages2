# Gages-II source/doc
#     https://water.usgs.gov/GIS/metadata/usgswrd/XML/gagesII_Sept2011.xml#stdorder
# https://github.com/xarray-contrib/cf-xarray/pull/260
# conda install -c conda-forge cf_xarray
import pathlib as pl

# import cf_xarray as cfxr
import geopandas as gpd

g2_shp = pl.Path("gagesII_9322_point_shapefile/gagesII_9322_sept30_2011.shp")
g2 = gpd.read_file(g2_shp)

# The projection information cant currently be kept, so drop geometry.
del g2["geometry"]
assert "geometry" not in g2.columns

ds = g2.to_xarray()
ds.to_netcdf("gagesII_9322_sept30_2011_no_geom.nc")
