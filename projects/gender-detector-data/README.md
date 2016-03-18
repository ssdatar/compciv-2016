
# Gender Analysis of Art Grants by the San Francisco Art Commission

## Introduction

This is an automated analysis of the [grants made by the San Francisco Arts Commission to individual artists](http://www.sfartscommission.org/CAE/grants/grant-programs-and-applications/) since 2004. These grants are made by the Individual Artists Commission and can be up to $15,000. Preliminary analysis shows us that even though women have got more in total grants than men since 2004, the average grant amount for women is slightly lower -- though by $136.


### Methodology and caveats

The methodology of the gender detection is to use the dirt-cheap super naive and ethnocentric algorithm developed in the [babynames-gender-detector homework](http://www.compciv.org/assignments/exercise-sets/0020-gender-detector-set).

The caveats are basically: 

- Gender detection reference data set leaves out many names i.e. names that are uncommon and thus are classified under the 'NA' category
- Collaboration is allowed, though an individual artist is the grantee
- Grants can be requested for full funding of a project or for one phase of a "larger creative arc", as the website puts it. This may not reflect in the numbers

### Past research and articles

An [interview of Tom DeCaigny](http://ebar.com/news/article.php?sec=news&article=71373), the director of the Commission, on how he is fighting to fund individual artists in a city that is increasingly expensive to live in for artists.

I want to see how the grants are given out, just to glean if there is any particular preference to one gender or the other -- or even if one gender has more artists than the other.

## How to use it

Note: if you want to __clone__ this repo from Github, run this:

    git clone https://github.com/ssdatar/compciv-2016.git

This will clone the entire compciv-2016 repo, and you can find this project under __projects/gender-detector-data__

Run the following scripts provided in this repo in this order:


### fetch_gender_data.py

Downloads the raw [babyname data from the Social Security Administration](https://www.ssa.gov/oact/babynames/limits.html) and unpacks it into the __tempdata/babynames__ directory.


### wrangle_gender_data.py

Selects and compiles the baby name records for every five years between 1900 and 1991, and adds the records for 2014.

### fetch_artist_data.py

Downloads the CSV file from the [SF Open Data portal](https://data.sfgov.org/Culture-and-Recreation/San-Francisco-Arts-Commission-Grants-FY2004-2014/mxvq-mfs5)

This produces [tempdata/artists.csv](tempdata/artists.csv) as the CSV file.

### wrangle_data.py

I downloaded the entire dataset and filtered the data to get those for Individual Arts Commission.

This script produces: [tempdata/wrangled_data.csv](tempdata/wrangled_data.csv)

### classify.py

For each row in [tempdata/wrangled_data.csv](tempdata/wrangled_data.csv), I use the `detect_gender()` function in the __gender.py__ script to determine the likely gender of the name. 

The `extract_usable_name()` function uses this incredibly naive algorithm to extract the "usable" first name from a given first name string:

- `namestr` is something like `"Paul Flores"`
- split `namestr` by whitespace
- select the first element, i.e. `"Paul`

A new file -- [tempdata/classified_data.csv](tempdata/classified_data.csv) -- is produced. Basically, it's wrangled_data.csv with three new columns:

- gender
- ratio (the likelihood/bias of the baby boy vs girl numbers)
- usable_name - the partial string extracted from `first_name` to do the classification.


### analyze.py

Reads [tempdata/classified_data.csv](tempdata/classified_data.csv) and produces the output seen at the bottom of this README's analysis.



### Ancillary files

Here are some supporting files. You don't actually _run_ these, but they are called by the other files.


### gender.py

This contains the code to load the wrangled gender data and the `detect_gender()` function.





## Analysis

The gender distribution of the grants given to the individual artists were calculated.

The following facets were computed:
- Grants given to men and women since 2004, average grant amount over the years
- Grant distribution per year to each gender
- Types of grants taken up by each gender
- How many men vs women took up L/G/B/T projects


According to the automated analysis, 169 women have got $1.4 million in grants, as opposed to 129 men receiving $1.15 million.

This means that, on an average, the grant amount for women was $8,763. This was $8,899 for men.

The per year grant gender ratio showed no discernible trend. For four years, men got more money than women, and vice versa for the other seven.

More men have taken up projects focused on LGBT issues than women.



-----------------------------------

### Printout of analyze.py

The raw printout:

~~~
---------------------------------------------
Analyzing gender distribution of grants...
Since 2004, 129 men have got $1.15 million in grants
Since 2004, 160 women have got $1.4 million in grants
Average grant amount for men 8899 dollars
Average grant amount for women 8763 dollars
---------------------------------------------
Analyzing yearly distribution of grants...


In the year 2004
Men got 50000 dollars
Women got 59900 dollars
Grant gender ratio 0.83


In the year 2005
Men got 82000 dollars
Women got 60000 dollars
Grant gender ratio 1.37


In the year 2006
Men got 132000 dollars
Women got 131000 dollars
Grant gender ratio 1.01


In the year 2007
Men got 148700 dollars
Women got 233600 dollars
Grant gender ratio 0.64


In the year 2008
Men got 87500 dollars
Women got 85000 dollars
Grant gender ratio 1.03


In the year 2009
Men got 110680 dollars
Women got 121760 dollars
Grant gender ratio 0.91


In the year 2010
Men got 80000 dollars
Women got 90000 dollars
Grant gender ratio 0.89


In the year 2011
Men got 139600 dollars
Women got 190650 dollars
Grant gender ratio 0.73


In the year 2012
Men got 129500 dollars
Women got 98275 dollars
Grant gender ratio 1.32


In the year 2013
Men got 108000 dollars
Women got 174460 dollars
Grant gender ratio 0.62


In the year 2014
Men got 80000 dollars
Women got 157500 dollars
Grant gender ratio 0.51
---------------------------------------------
Analyzing gender distribution of types of grants...
Number of men who took up LGBT projects 1
Grant focus: Women L/G/B/T/Q
Men: 0
Women: 62000


Number of women who took up LGBT projects 0
Grant focus: Native American L/G/B/T/Q
Men: 8500
Women: 0


Number of men who took up LGBT projects 2
Grant focus: Women African American L/G/B/T/Q
Men: 0
Women: 8000


Grant focus: Latino American
Men: 121450
Women: 0


Grant focus: African American Women
Men: 0
Women: 93200


Grant focus: No specified focus
Men: 365680
Women: 16200


Grant focus: L/G/B/T/Q Transgender
Men: 60000
Women: 5060


Grant focus: African American
Men: 54700
Women: 10000


Grant focus: Women Asian American
Men: 0
Women: 9000


Grant focus: Women Native American Multiple People of Color
Men: 0
Women: 9000


Number of men who took up LGBT projects 3
Grant focus: Women Disabled L/G/B/T/Q
Men: 0
Women: 9700


Number of men who took up LGBT projects 4
Grant focus: L/G/B/T/Q Latino American Women
Men: 0
Women: 8700


Grant focus: Women
Men: 0
Women: 453710


Number of men who took up LGBT projects 5
Grant focus: Latino American L/G/B/T/Q Women
Men: 0
Women: 42000


Number of men who took up LGBT projects 6
Number of women who took up LGBT projects 1
Grant focus: Women L/G/B/T/Q Disabled
Men: 0
Women: 0


Number of women who took up LGBT projects 2
Grant focus: Asian American L/G/B/T/Q
Men: 24000
Women: 0


Number of men who took up LGBT projects 7
Grant focus: Asian American L/G/B/T/Q Women
Men: 0
Women: 43600


Number of women who took up LGBT projects 3
Grant focus: Latino American L/G/B/T/Q
Men: 19000
Women: 0


Number of women who took up LGBT projects 4
Grant focus: L/G/B/T/Q Native American
Men: 9000
Women: 0


Number of women who took up LGBT projects 5
Grant focus: L/G/B/T/Q Asian American
Men: 18000
Women: 0


Number of women who took up LGBT projects 6
Grant focus: L/G/B/T/Q African American
Men: 10000
Women: 0


Grant focus: L/G/B/T/Q
Men: 162650
Women: 18100


Number of men who took up LGBT projects 8
Grant focus: African American L/G/B/T/Q Women
Men: 0
Women: 9000


Number of men who took up LGBT projects 9
Grant focus: L/G/B/T/Q Women Asian American
Men: 0
Women: 10000


Grant focus: Asian American Women
Men: 0
Women: 283950


Number of men who took up LGBT projects 10
Grant focus: African American L/G/B/T/Q Asian American
Men: 0
Women: 9000


Grant focus: L/G/B/T/Q Women
Men: 26000
Women: 162400


Grant focus: Pacific Islander
Men: 10000
Women: 0


Number of men who took up LGBT projects 11
Grant focus: Asian American Latino American L/G/B/T/Q Women
Men: 0
Women: 10000


Number of women who took up LGBT projects 7
Grant focus: African American L/G/B/T/Q
Men: 30000
Women: 0


Grant focus: Latino American Women
Men: 0
Women: 76175


Grant focus: Women Native American
Men: 0
Women: 9700


Number of men who took up LGBT projects 12
Grant focus: Women L/G/B/T/Q Multiple People of Color Asian American
Men: 0
Women: 8000


Grant focus: Asian American
Men: 199000
Women: 17100


Grant focus: Asian American Latino American African American Pacific Islander
Men: 10000
Women: 0


Number of men who took up LGBT projects 13
Grant focus: L/G/B/T/Q Women Latino American
Men: 0
Women: 8550


Grant focus: Women African American
Men: 0
Women: 10000


Number of women who took up LGBT projects 8
Grant focus: L/G/B/T/Q Latino American
Men: 10000
Women: 0


Grant focus: African American Women Native American
Men: 10000
Women: 0


Number of men who took up LGBT projects 13
Number of women who took up LGBT projects 9

In [38]: 

~~~