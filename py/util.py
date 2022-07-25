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

    # group by water year and sum to annual values for indicators that need total annual sum and then find annual average for temp
    sw = sw.groupby('wyear').agg({'stor':'sum', 'rch':'sum', 'run':'sum', 'aet':'sum', 'cwd':'sum', 'tmax':'mean', 'tmin':'mean', 'ppt':'sum', 'pet':'sum'}).reset_index()

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
    zones['percent_of_ecoregion'] = zones[intersect_name] / zones['ecoregion_acres'] * 100
    zones = zones.drop('geometry', axis = 1)
    return zones


def simplify_ecoregions(ecoregions: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """Simplify the ecoregion dataset 

    Args:
        ecoregions (gpd.GeoDataFrame): shapefile of the ecoregions

    Returns:
        gpd.GeoDataFram: The ecoregions geodataframe with a new simplified ecoregions column and the acres of the ecoregion
    """
    
    ecoregions['l4_simple'] = np.where(ecoregions['US_L4NAME'].isin({'Point Reyes/Farallon Islands', 'Marin Hills'}), 'Bodega Coastal Hills', ecoregions['US_L4NAME'])
    ecoregions['l4_simple'] = np.where(ecoregions['l4_simple'] == "Mayacmas Mountains", 'Mayacamas Mountains', ecoregions['l4_simple'])
    ecoregions_simp = ecoregions[['l4_simple', 'geometry']]
    ecoregions_simp = ecoregions_simp.dissolve(by = 'l4_simple', aggfunc='sum').reset_index()
    ecoregions_simp['ecoregion_acres'] = ecoregions_simp['geometry'].area / 43560
    return ecoregions_simp


def longname_landuse(landuse: gpd.GeoDataFrame) -> gpd.GeoDataFrame:

    # dissolve landuse by designation
    landuse_simp = landuse.dissolve(by="DESIGNATIO").reset_index()
    landuse_simp = landuse_simp[["DESIGNATIO", "geometry"]]
    
    # longname of the landuse
    name_map = {
    "DA": "Diverse Agriculture",
    "GC": "General Commercial",
    'GI': "General Industrial",
    'LC': "Limited Commercial",
    'LEA': "Land Extensive Agriculture",
    'LI': "Limited Industrial",
    'LIA': "Land Intensive Agriculture",
    'PQP': "Public / Quasi-public",
    'RR': "Rural Residential",
    'RRD': "Resources and Rural Development",
    'RVSC': "Recreation and Visitor Serving Commercial",
    'UR': "Urban Residential"
    }
    
    landuse_simp['landuse'] = landuse_simp["DESIGNATIO"].apply(lambda val: name_map[val])
    landuse_simp = landuse_simp[['landuse', 'geometry']]
    return landuse_simp