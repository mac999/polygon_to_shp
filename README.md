# polygon to shape
polygon_to_shp skeleton code

# purpose
convert dataset including polygon's point list to ESRI shp file

# explain
Refer to https://daddynkidsmakers.blogspot.com/2022/11/shp.html

# packages
pip install numpy, geopandas, osgeo

# run
git clone https://github.com/mac999/data_to_shp </br>
prepare input dataset text file. Ex. [[(x, y), (x,y), ...], [(x, y), (x,y), ...], [...]]
</br>
programming read_file() function considering your dataset format. </br>
run python3 data_to_shp.py </br>

# license
MIT
