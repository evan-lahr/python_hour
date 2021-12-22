# Minimal example of regridding using xESMF
# 
# Documentation here: https://xesmf.readthedocs.io/en/latest/why.html

import xarray as xr
import xesmf

# if not already in xarray format, set input/output grids
grid_out = xr.Dataset({'lat':(['lat'],output_grid['lats']),
                       'lon':(['lon'],output_grid['lons'])})
grid_in = xr.Dataset({'lat':(['y','x'],input_grid['lats']),
                      'lon':(['y','x'],input_grid['lons'])})

# create reusable "regridder"
# options for regridding algorithms: 'bilinear', 'conservative', 'nearest_s2d', 'nearest_d2s', 'patch'
regridder = xesmf.Regridder(grid_in,grid_out,'bilinear',filename='regridder.nc')

# regrid all time steps within a single file
data_regridded = regridder(data_file['variable_name'])
data_regridded.to_netcdf(...)

# iterate over separate files that need regridding
for data_file in range(len(data_in_a_list)):
  data_regridded = regridder(data_file['variable_name'])
  data_regridded.to_netcdf(...)
