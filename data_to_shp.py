# title: data_to_shp.py
# author: taewook kang
# date: 2022.11.25
import numpy as np
import geopandas as gpd
import osgeo.ogr as ogr
from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon
from shapely import affinity
from osgeo import gdal, osr

def read_file():
	input = []
	# todo 
	return input

def create_polygon(input):
    shapes = []
    for xy in input:
        # 연결링 구조 라인 객체 생성
        line_string = ogr.Geometry(ogr.wkbLinearRing)
        for p in xy:
            line_string.AddPoint(p[0], p[1])    
        shapes.append(line_string)

    return shapes

def save_shp(out_fname, shapes, projection_EPSG_ID = 25832):
    try:
        driver = ogr.GetDriverByName("ESRI Shapefile")    # ("GTiff")  # ("HFA") # Get a handler to a driver
        dataset_out = driver.CreateDataSource(out_fname)

        ref = osr.SpatialReference()
        ref.ImportFromEPSG(int(projection_EPSG_ID))

        # 레이어 생성
        layer = dataset_out.CreateLayer("data", ref, ogr.wkbPolygon)

        # shp 필드 정의 
        id_field = ogr.FieldDefn("id", ogr.OFTInteger)
        layer.CreateField(id_field)

        # 레이어에 피쳐 추가
        featureDefn = layer.GetLayerDefn()
        for index, s in enumerate(shapes):
            poly = ogr.Geometry(ogr.wkbPolygon) 
            poly.AddGeometry(s)

            feature = ogr.Feature(featureDefn)
            feature.SetGeometry(poly)
            feature.SetField("id", index)
            layer.CreateFeature(feature)

            feature = None
        dataset_out = None

    except BaseException as err:
        print(err)    

def main():
	input = read_file()
	shapes = create_polygon(input)
	save_shp('./output.shp', shapes)


