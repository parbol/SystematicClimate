from pyesgf.search import SearchConnection
import xarray as xr
import os.path as op
from tqdm import tqdm
from datetime import datetime

conn = SearchConnection('http://esgf-data.dkrz.de/esg-search',
                        distrib=True)

ctx = conn.new_context(project='CMIP6',
                       variable='prc',
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
    outfile = op.join("./CMIP6", op.basename(fc.opendap_url))
    if op.isfile(outfile):
        continue
    try:
        with xr.open_dataset(fc.opendap_url) as ds:
            prc = ds["prc"]
            prc = prc.sel(lat=slice(43, 44), lon=slice(355, 357))
            prc.to_netcdf(outfile)
    except:
        print("Ha habido un problema con el fichero: ", op.basename(fc.opendap_url))
        print("Seguimos a por el próximo")
        with open("./ErroresDescarga.txt", "at") as fid:
            fid.write(op.basename(fc.opendap_url))
            fid.write("\n")