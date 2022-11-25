# program
data_to_shp

# purpose
convert dataset including polygon's point list to ESRI shp file

# packages
pip install numpy, geopandas, osgeo

# run
git clone https://github.com/mac999/data_to_shp
prepare input dataset text file. 
  ex. [[(x, y), (x,y), ...], [(x, y), (x,y), ...], [...]]

programming read_file() function considering your dataset format. 
run python3 data_to_shp.py

# license
MIT
