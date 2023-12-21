import pandas as pd

from zipline.data.bundles import register
from zipline.data.bundles.csvdir import csvdir_equities
register(
    'tesla_bundle',
    csvdir_equities(
        ['daily'],
        '/home/subrina/Trading with python/Zipline/custom_data'
    ),
    calendar_name='XNYS',
   
    
)