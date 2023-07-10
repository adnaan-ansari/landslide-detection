
# Geotagged Image Pixel Coordinates to CSV Converter

This repository contains a script that converts a geotagged image into a CSV file containing pixel coordinates.

## Prerequisites

- QGIS software installed on your system. You can download it from the [official QGIS website](https://www.qgis.org/).

## Instructions

1. Open the file containing the geotagged image, which should be in black and white format representing landslides.
2. Convert the image into a vector format using the following steps in QGIS:
   - Click on `Raster` in the top menu.
   - Go to `Conversions`.
   - Select `Raster to Vector`.
3. Create bounding boxes around the vectorized image using the following steps:
   - Click on `Processing` in the top menu.
   - Go to `Toolbox`.
   - Select `Bounding Boxes`.
4. Open the attribute table of the generated "bounds layer".
5. Add the attributes in the following sequence: `fid`, `DN`, `width`, `height`, `center_x`, `center_y`.
   - Note: Generate the required attributes using the field calculator of the attribute table.
   - Note: There is an additional bounding box in the table representing the whole image, which should be discarded.
6. Use the provided code [Convert.py](https://github.com/adnaan-ansari/landslide-detection/blob/main/convert.py) to convert the table into pixel coordinates.
   - The code outputs a CSV file in pixel format, which should be further verified.

Since the images we are dealing with are large (approximately 15000x8000 pixels), it is recommended to convert them into smaller equal-sized images. This can be achieved using the following steps in QGIS:
1. Click on `Processing` in the top menu.
2. Go to `Toolbox`.
3. Select `Generate XYZ Tiles`.
4. Follow the instructions to generate smaller images in the desired size.
   - These smaller images can be used for YOLO training.

