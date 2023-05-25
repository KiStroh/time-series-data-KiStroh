import os
import pathlib
import subprocess
from io import BytesIO

# Third Party?
import folium
import matplotlib.dates as dates
import matplotlib.pyplot as plt
import pandas as pd
import requests

m = folium.Map(location=[44.08109849, -102.4012746])

m

# raise NotImplementedError("Map of Wasta, SD")