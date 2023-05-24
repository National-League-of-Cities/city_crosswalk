select 
      [org_cst_key]
      ,[org_name]
      ,[org_ogt_code]
      ,[org_state_incorporated]
      ,[n53_municipal_type]
      ,[org_metropolitan_area_ext]
      ,[org_fips_place_ext]
      ,[org_prefix_ext]
      ,[org_city_name_ext]
      ,[org_fips_county_subdivision_ext]
from co_organization
join co_organization_ext on org_cst_key = org_cst_key_ext
left join client_nlc_municipality_type on org_n53_key_ext = n53_key