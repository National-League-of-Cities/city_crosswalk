select 
org_cst_key,
org_name,
org_city_name_ext,
org_state_incorporated,
org_dues_population_ext,
org_census_geoid_ext,
cst_member_flag
from co_organization, co_organization_ext, co_customer
where org_cst_key = org_cst_key_ext and org_cst_key = cst_key and org_crosswalk_ext = 1 and org_delete_flag = 0
