import csv
from osgeo import gdal, osr


csv_file = 'bounding_boxes.csv'

bounding_boxes = []
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        lon = float(row['center_x'])
        lat = float(row['center_y'])
        bounding_boxes.append([lon, lat])


raster_path = 'Nepal_1994.tif'
raster_ds = gdal.Open(raster_path)


if raster_ds is not None:
    
    geotransform = raster_ds.GetGeoTransform()

    
    pixel_coordinates = []
    for bbox in bounding_boxes:
        lon, lat = bbox

       
        pixel_x = int((lon - geotransform[0]) / geotransform[1])
        pixel_y = int((lat - geotransform[3]) / geotransform[5])

        pixel_coordinates.append([pixel_x, pixel_y])

    
    output_csv_file = 'pixel_coordinates.csv'
    with open(output_csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['pixel_x', 'pixel_y'])  
        writer.writerows(pixel_coordinates)

    print("Conversion complete. The converted pixel coordinates have been saved to", output_csv_file)
else:
    print("Failed to open the raster dataset.")
