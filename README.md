# LiDAR Scan

## Objetives
- Explore usage of [RPLIDAR A1](https://www.slamtec.com/en/lidar/a1) with a Python [library](https://github.com/adafruit/Adafruit_CircuitPython_RPLIDAR).
- Visualize LiDAR scan data.
- Polar and Cartesian coordinates conversion.

## Requirements
Place the LiDAR at designated location, scan and analyze the data.
### (60%) 1. LiDAR Scan Visualization
1. Complete at least 1 successful scan in 360 degrees with 100+ non-zero distance samples. 
2. Plot the data points from last successful scan under the polar coordinate system.
3. Save the plot as a image file (PNG or JPG) in this repository.
4. Log distance samples at 0, 135, and 225 degrees and the (x, y) coordinates under the Cartesian frame as shown below.

- **Note:** The RPLIDAR A1 spins clockwise, but the polar plot use counter-clockwise as the default angle increasing direction. 
![](images/scan_example.png)

### (40%) 2. Convert Polar coordinates to Cartesian coordinates 
1. Describe the transformation rule (from polar to cartesian) using math language.
2. Attach a diagram to explain such a transformation. You can download one online, but your figure has to be correctly rendered by Github Markdown.
    
## Helpful Resources
- [Polar plot via Matplotlib](https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_demo.html)
