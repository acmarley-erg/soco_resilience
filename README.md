# Sonoma County Climate Resilient Lands Strategy

This repository houses the data analysis conducted for the [Sonoma County Climate Resilient Lands Strategy](https://sonomacounty.ca.gov/administrative-support-and-fiscal-services/county-administrators-office/climate-action-and-resiliency/sonoma-county-climate-resilient-lands-strategy#:~:text=The%20Resilient%20Lands%20Strategy%20helps,management%20to%20maximize%20sequestration%2C%20and).

### Folders:
`output/`: Output maps, graphs, and interactive html maps of project analysis.

`R/`: RMarkdowns used to download demographic data, visualize available data, and process some hazard data.

`py/`: Jupyter notebooks used for most of the geospatial data analysis and processing conducted as well as static and interactive data visualizations used in the strategy. 

### Data

Some of the data used in this analysis is not available to the public or is too large to host on GitHub, so the `data/` folder referred to in the script is not in this repository. Below is a list of the data used in this analysis and the initial locations the data was saved to in the `data/` folder.

| Data Type  | Data Name | Data Source | Download Location |
| ------------- | ------------- | ------------- | ------------- |
| Sea level rise & storm surge | COSMOS  | [Our Coast Our Future (OCOF)](https://ourcoastourfuture.org/hazard-map/)| `data/raw/sonoma_flooding_slr075` & `data/raw/sonoma_flooding_slr200` |
| Flooding risk  | Sonoma County Flood Awareness Areas  | [Sonoma County Vital Lands](https://sonomaopenspace.maps.arcgis.com/apps/webappviewer/index.html?id=4e93808b8ea245bfa739caccdb0169fe) | `data/raw/Flood_Awareness_Areas` |
| Flooding risk | FEMA 100 yr flood layers | [FEMA](https://msc.fema.gov/portal/home) | `data/raw/FEMA_100yr_flood` |
| Landslide risk | Susceptibility to Deep-Seated Landslides | [CA Geological Survey](https://gis.conservation.ca.gov/portal/home/item.html?id=87289025c11d4ba7ae65f0f472bf7c2d) | `data/raw/ca_landslide_susceptibility_20181001` |
| Wildfire risk | Sonoma County Wildfire Risk Index | [Sonoma County](https://sonoma-county-cwpp-hub-site-sonomacounty.hub.arcgis.com/datasets/wildfire-risk-index/explore?location=38.480806%2C-122.941170%2C10.47) | `data/clean/soco_wildfire_risk_index` |
| Projected and historical drought | Climatic Water Deficit | [San Francisco Bay Area Climate-Smart Watershed Analyst](http://climate.calcommons.org/tbc3/sf-bay-watershed-analyst) | `data/raw/Sonoma County_BCM` |
| Projected and historical precipitation | Precipitation | [San Francisco Bay Area Climate-Smart Watershed Analyst](http://climate.calcommons.org/tbc3/sf-bay-watershed-analyst) | `data/raw/Sonoma County_BCM` |
| Projected and historical temperature | Max and min temperature | [San Francisco Bay Area Climate-Smart Watershed Analyst](http://climate.calcommons.org/tbc3/sf-bay-watershed-analyst) | `data/raw/Sonoma County_BCM` |
|Ecoregion|Level IV Ecoregions|[US Environmental Protection Agency (EPA)](https://www.epa.gov/eco-research/ecoregion-download-files-state-region-9#pane-04)| `data/raw/ca_ecoregions` |
| Vegetation type | Sonoma County Fine-scale Veg. and Habitat Map | [Sonoma Veg Map](https://sonomavegmap.org/data-downloads/) | `data/raw/Sonoma_County_Veg_Map_Shp` |
| Land use type | SoCo PRMD GIS General Plan Land Use | County of Sonoma | `data/raw/soco_landuse` |
| Demographics | Population | [American Community Survey 2020](https://www.census.gov/programs-surveys/acs) | downloaded via `R/demographics.Rmd` |
| Housing | Housing units | [American Community Survey 2020](https://www.census.gov/programs-surveys/acs) | downloaded via `R/demographics.Rmd` |
| Priority communities | Bay Area 2050 Equity Priority Communities | [Metropolitan Transportation Commission (MTC)](https://bayareametro.github.io/Spatial-Analysis-Mapping-Projects/Project-Documentation/Equity-Priority-Communities/) | `data/raw/priority_pops_ces3_2021` |
| Critical facilities | Critical facilities | Sonoma County Hazard Mitigation Plan | `data/raw/soco_critical_facilities` |


