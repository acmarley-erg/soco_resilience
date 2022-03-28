import pandas as pd
import numpy as np
import geopandas as gpd

# 
def calc_avs(fp: str) -> pd.DataFrame:

    """Create one large dataframe with the averages of each climate index for each watershed for each gcm

    Args:
        fp (str): The filepath to csv file to get averages for

    Returns:
        pd.DataFrame: A dataframe of averages
    """
    
    # read in the csv file
    sw = pd.read_csv(fp)

    # Create conditions for groupin water years
    conditions = [
    (sw["wyear"] < 1951),
    (sw["wyear"] >= 1951) & (sw["wyear"] <= 1980),
    (sw["wyear"] > 1980) & (sw["wyear"] < 2010),
    (sw["wyear"] >= 2010) & (sw["wyear"] <= 2039),
    (sw["wyear"] >= 2040) & (sw["wyear"] <= 2069),
    (sw["wyear"] >= 2070) & (sw["wyear"] <= 2099),
    (sw["wyear"] > 2099) 
    ]

    # create a list of the values we want to assign for each condition
    values = ["NA", "1951-1980", "NA", '2010-2039', '2040-2069', '2070-2099', "NA"]

    # create a new column and use np.select to assign values to it using our lists as arguments
    sw["wyear_group"] = np.select(conditions, values)

    # clean the dataframe to the columns we want
    sw_clean = sw[["wyear_group", "stor", "rch", "run", "aet", "cwd", "tmax", "tmin", "ppt", "pet"]]
    sw_clean = sw_clean[(sw_clean["wyear_group"] != "NA")]

    # Create the average dataframe of each climate index
    sw_av = sw_clean.groupby("wyear_group").agg("mean")
    return sw_av


def zone_intersect(ecoregions: gpd.GeoDataFrame, intersect_layer: gpd.GeoDataFrame, intersect_name: str) -> pd.DataFrame:
    """Calculate the area of each ecoregion in a hazard or land type

    Args:
        ecoregions (gpd.GeoDataFrame): shapefile of the ecoregions
        intersect_layer (gpd.GeoDataFrame): shapefile of the hazard or land type you want to calculate area for
        intersect_name (str): The name of the hazard

    Returns:
        pd.DataFrame: a dataframe with the ecoregion in one column and the area in acres of the hazard type in the region
    """
    zones = gpd.overlay(ecoregions, intersect_layer, how='intersection')
    zones[intersect_name] = zones['geometry'].area / 43560
    zones = zones.drop('geometry', axis = 1)
    return zones