### Census Geographies
The follow are the base geographical units from census. Each table has a unique ID for joining to the crosswalks

|Table Name|Unique ID (length)| Description| Change Date|
| :--- | :--- | :--- | ---: |
|CSA|FIPS (3)|Combined Statistical Area|2/1/2021|
|CBSA|FIPS (5)|Core-Based Statistical Area (Metro/Micro-politan Area)|2/1/2021|
|METDIV|FIPS (5)|Metropolitan Division|2/1/2021|
|COUNTY|GEOID (5)|Counties|1/6/2023|
|COUSUB|GEOID (10)|County Subdivision|2/1/2021|
|TRACT|GEOID (11)|Tracts| 1/6/2023|
|BLOCKGROUP|GEOID (12)|Block Group| 1/6/2023|
|BLOCK|GEOID (15)|Blocks| 1/6/2023|

**Non-Hierarchical Geographies**

|Table Name|Unique ID (length)| Description|Change Date|
| :--- | :--- | :--- | ---: |
|CD|GEOID (4)|118th Congressional Districts| 1/10/2023|
|PLACE|GEOID (7)| All Places| 2/1/2021|

### Census of Local Governments

The Census of Governments has 38,737 local governments listed as of 2022. The list was subdivided in to three parts based on the type of local government to isolate local governments that fall under the umbrella of NLC and match them to the Census geographies.

    1. COUNTIES - includes 2 city-counties, 4 (3 current and 1 former) NLC members that are officially counties, and organized boroughs of Alaska
    2. MUNICIPALITIES - includes incorporated places and 2 NLC members that are a unincorporated areas
    3. TOWNSHIPS - includes county-subdivision geographic units from New England and Boardman, OH (principal city in Youngstown Metro Area)
    4. Puerto Rico - The Municipios of Puerto Rico are not in the Census of Local Governments. The data for the 78 Municipios is foudn on the County-level tables of the census hierarchy.
    
These tables are combined to create the following table which can be merged to the crosswalks and the base geographies.

|Table Name|Unique ID (length)| Description|Change Date|
| :--- | :--- | :--- | ---: |
|CTV|GEOID (5/7/10)|All Cities, Towns and Villages| 11/27/2023|

Total: 20,943 Cities Towns and Villages


### Crosswalks

The following crosswalk tables can be used to join the primary CTV table to related geographies. Joining must be done using the  GEOID column with the corresponding table and primary key

|Table Name|Join On| Join Table|
| :--- | :--- | :--- |
|CTV_x_COUNTY|GEOID_ctv|CTV|
||GEOID_county|COUNTY|
||GEOID_csa|CSA|
||GEOID_cbsa|CBSA|
||GEOID_metdiv|METDIV|
|CTV_x_BLOCK|GEOID_ctv|CTV|
||GEOID_county|COUNTY|
||GEOID_cousub|COUSUB|
||GEOID_place|PLACE|
||GEOID_tract|TRACT|
||GEOID_blockgroup|BLOCKGROUP|
||GEOID_block|BLOCK|
|CTV_x_CD|GEOID_ctv|CTV|
||GEOID_cd|CD|



## Changelog and Errata

The following items are changes made to correct inconsistencies between the datasets as well as updating for more current information.

**State-level Changes/Issues**

* In 2019, Connecticut changed their counties. Actually, Connecticut abolished counties in the 60s but Census maintained the historical hierarchy for reporting and aggregations. THe 2019 "New Counties" were adopted to be more accurate aggregations based on how the population centers have shifted and grown. The new counties have new FIPS code, but are not on the Counties table here. Connecticut Townships use the county code in for digits 3 4 and 5, so the ones in CTV and COUSUB table reflect the OLD counties.


* City of Cahokia heights,IL was formed as a merger of Cahokia, Alorton and Centreville IL. The Fips_place was changed from 10373 to 10370 [the orginal for Cahokia], for matching)


* Louisville-Jefferson county KY, has 3 census geographies: 1) The Entire City-County, 2) Just the city of Louisville, 3) Just the areas of the county that do not belong to any municipality with exists within the city-county. The population that NLC reports is a combination of the latter 2, FIPS_place 48000 + 48006, but the City-County in its entireity is 48003

**Changed place code in Census of governments to match with Census Townships table**
166545, Bridgewater Township, place code 08085 to 08130
128148, Randolph Township, place code 55955 to 56000

**Changed place code in Census of governments to match with Census Place table**
101399, City of Central City CO, FIPS_place 12900 to 12910
124939, Village of Gulfport IL, FIPS_place 31991 to 31992
165866, Louisville-Jefferson county KY, change place 48003 to 48000
224809, City of Greenfield, place code 27100 to 27060
169115, Village of Bellerive, place code 04240 to 04248
171132, Village of Grandfather, place code 27320 to 27324
161834, Athens-Clarke County GA, FIP_place 03436 to 03440
175728, Nashville-Davidsonville TN, change place 52004 to 52006
108124, Butte-Silver Bow MT,change place 11390 to 11397

**Cities listed as active in Census of Governments but not in any other census geography table**
Lone Chimney, OK
Mule barn, OK
Double Horn, TX
Peaster Town, TX
Ellinger, TX
Corral City TX
Millican, TX
Village of Tuxedo, NY
