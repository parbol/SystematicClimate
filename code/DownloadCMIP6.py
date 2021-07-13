from pyesgf.search import SearchConnection
import xarray as xr
import numpy as np
import os.path as op
from tqdm import tqdm
from datetime import datetime

Alemania = "https://esgf-data.dkrz.de/esg-search/"
Francia = "https://esgf-node.ipsl.upmc.fr/esg-search/"

conn = SearchConnection(Francia,
                        distrib=True)

# We need to download variables:
# prc: Convective precipitation
# pr: Non-convective precipitation
VAR_NAME = 'pr'
ctx = conn.new_context(project='CMIP6',
                       variable=VAR_NAME,
                       experiment_id="historical",
                       frequency="day")
datos = ctx.search()

for idx, i in tqdm(enumerate(datos), total=len(datos)):
    fc = i.file_context().search()
    if len(fc)==0:
        continue
    fc = fc[0]
    if fc.opendap_url is None:
        continue
    outfile = op.join("/srv/SystematicClimate/CMIP6", op.basename(fc.opendap_url))
    if op.isfile(outfile):
        continue
    try:
        with xr.open_dataset(fc.opendap_url) as ds:
            prc = ds[VAR_NAME]
            prc = prc.sel(lat = slice(34, 46),
                          lon = prc.lon[(prc.lon<5) | (prc.lon>350)])
            prc = prc.assign_coords(lon = (((prc.lon + 180) % 360) - 180))
            prc = prc.roll(lon = (-np.nonzero(prc.lon.values < 0)[0][0]), roll_coords=True)
            prc.to_netcdf(outfile)
    except Exception as e:
        print("Ha habido un problema con el fichero: ", op.basename(fc.opendap_url))
        print(e)
        print("Seguimos a por el próximo")
        with open("./ErroresDescarga.txt", "at") as fid:
            fid.write(op.basename(fc.opendap_url))
            fid.write("\n")
        