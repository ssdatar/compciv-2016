# Eviction notices in San Francisco

### Where are people receiving them?


# About the dataset

The city of San Francisco has published a dataset of eviction notices delivered to tenants in the city. The dataset contains 34,914 records, with fields specifiying the address of the home, zip code, geolocation, and various columns that specify the reason why the tenant was evicted. The data is published since January 1, 1997.


## Basic facts about the dataset

- The source of the data: [SF Open Data portal](https://data.sfgov.org/)
- The data's landing page: [Eviction notices](https://data.sfgov.org/Housing-and-Buildings/Eviction-Notices/5cei-gny5)
- The data format: CSV (is also available as JSON, XLS, etc)
- Number of rows: 34,915

## Description of data fields

#### Eviction_ID

Unique ID of the case 


#### Address 

Contains a __text string__ that shows where the notice was issued. This is down to the block level.

#### City

City where it was issued, which is San Francisco in this case


#### Zip

Zip code of the address. Contains a __text string__

#### File Date  

Contains a __text string__ representing when the eviction notice was filed with the Rent Board of Arbitration

#### Non-Payment

Contains a __text string__ that is set true when the landlord has indicated non-payment as reason for serving eviction notice. False otherwise.

#### Breach

Contains a __text string__ that is set true when the landlord has indicated breach of lease as reason for serving eviction notice. False otherwise.

#### Nuisance

Contains a __text string__ that is set true when the landlord has indicated illegal use as grounds for eviction. False otherwise.

#### Illegal Use

Contains a __text string__ that is set true when the landlord has indicated non payment as reason for serving eviction notice. False otherwise.

#### Failure to Sign Renewal

Contains a __text string__ that is set true when the landlord has indicated failure to sign lease as reason for serving eviction notice. False otherwise.

#### Access Denial

Contains a __text string__ that is set true when the landlord has indicated unlawful denial of access as reason for serving eviction notice. False otherwise.

#### Unapproved Subtenant

Contains a __text string__ that is set true when the landlord has indicated the tenant had an unapproved subtenant as reason for serving eviction notice. False otherwise.

#### Owner move in

Contains a __text string__ that is set true when the landlord has indicated owner move in as reason for serving eviction notice. False otherwise.

#### Demolition

Contains a __text string__ that is set true when the landlord has indicated demolition of property as reason for serving eviction notice. False otherwise.

#### Capital Improvement

Contains a __text string__ that is set true when the landlord has indicated non payment as reason for serving eviction notice. False otherwise.

#### Substantial Rehab

Contains a __text string__ that is set true when the landlord has indicated substantial rehabilitation as reason for serving eviction notice. False otherwise.

#### Ellis Act

Contains a __text string__ that is set true when the landlord has indicated Ellis Act withdrawal (going out of business) as reason for serving eviction notice. False otherwise.

#### Condo Conversion

Contains a __text string__ that is set true when the landlord has indicated condo conversion as reason for serving eviction notice. False otherwise.

#### Roommate Same Unit

Contains a __text string__ that is set true when the landlord has indicated they are evicting a roommate in the same unit as reason for serving eviction notice. False otherwise.

#### Other Cause

Contains a __text string__ that is set true if some other cause not covered by the admin code was indicated by the landlord. These are not enforceable grounds, but are indicated here for record keeping. False otherwise.

#### Late Payments

Contains a __text string__ that is set true when the landlord has indicated habitual delayed payment of rent as grounds for eviction. False otherwise.

#### Lead Remediation

Contains a __text string__ that is set true when the landlord has indicated lead remediation as reason for serving eviction notice. False otherwise.

#### Development

Contains a __text string__ that is set true when the landlord has indicated a development agreement as a reason for serving eviction notice. False otherwise.

#### Good Samaritan Ends

Contains a __text string__ that is set true when the landlord has indicated period of good samaritan laws coming to an end as reason for serving eviction notice. False otherwise.

#### Constraints

True if the unit is under Notice of Constraints. This means the owner is withdrawing the house from the rental market. Should he/she want to put it back on the market again, he/she has to follow rules that place limits on amount of rent that can be charged and also has to offer it to the displaced tenant if within ten years of withdrawal

#### Constraints Date

Contains a __text string__ that specifies date till which unit is under constraint notice.

#### Supervisor_District

Contains a __number string__ that indicates the district number of San Francisco Board of Supervisors, under which the property falls

#### Neighborhood

Contains a __text string__ that shows which census neighbourhood the property falls under

#### Client_Location

Contains a __location tuple__ that gives the coordinates of the property under question

## Anticipated data wrangling

I will filter the dataset to the last five years' worth of data. I will also have to bring all the reasons for eviction under one column, and split the location tuple into latitude and longitude so that a mapping tool can recognize it.
