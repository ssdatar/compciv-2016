
# Gender Analysis of Art Grants by the San Francisco Art Commission

## Introduction

This is an automated analysis of the [grants made by the San Francisco Arts Commission to individual artists](http://www.sfartscommission.org/CAE/grants/grant-programs-and-applications/). These grants are made by the Individual Artists Commission and can be up to $15,000. Preliminary analysis shows us that even though women have got more in total grants than men since 2004, the average grant amount for women is slightly lower -- though by $136.


### Methodology and caveats

The methodology of the gender detection is to use the dirt-cheap super naive and ethnocentric algorithm developed in the [babynames-gender-detector homework](http://www.compciv.org/assignments/exercise-sets/0020-gender-detector-set).

The caveats are basically: 

- Gender detection reference data set leaves out many names i.e. names that are uncommon and thus are classified under the 'NA' category
- Collaboration is allowed, though an individual artist is the grantee
- Grants can be requested for full funding of a project or for one phase of a "larger creative arc", as the website puts it. This may not reflect in the numbers

### Past research and articles

An [interview of Tom DeCaigny](http://ebar.com/news/article.php?sec=news&article=71373) on how he is fighting to fund individual artists in a city that is increasingly expensive to live in for artists.

I want to see how the grants are given out, just to glean if there is any particular preference to one gender or the other -- or even if one gender has more artists than the other.

## How to use it

Note: if you want to __clone__ this repo from Github, run this:

    git clone https://github.com/compciv/gendered-pulitzer-board

It will create a new sub-folder named `gendered-pulitzer-board`. This repo includes the `tempdata` folder: you should delete it manually and run all the scripts to see the project build itself from scratch.

Simply run the following scripts provided in this repo in this order:


### fetch_gender_data.py

Downloads the raw [babyname data from the Social Security Administration](https://www.ssa.gov/oact/babynames/limits.html) and unpacks it into the __tempdata/babynames__ directory.


### wrangle_gender_data.py

Selects and compiles the baby name records for every five years between 1900 and 1991, and adds the records for 2014.

### fetch_pulitzer_board_pages.py

Scrapes the raw JSON corresponding to each board page on pulitzer.org.

For example, here's the 1980 board's webpage: http://www.pulitzer.org/board/1980

Here's the corresponding scraped JSON file: [tempdata/pages/1980.json](tempdata/pages/1980.json)

Note: I wouldn't read too much into this script; the AngularJS-heavy Pultizer.org has a fairly unorthodox front-end...no HTML parsing was even done.

### wrangle_pulitzer_board_data.py

Once the JSON files corresponding to each board page were downloaded, I extracted the specific fields I needed for the analysis, particularly the year of membership for each person, and their first and last name (mostly, their first name).

This script produces: [tempdata/wrangled_data.csv](tempdata/wrangled_data.csv)

### classify.py

For each row in [tempdata/wrangled_data.csv](tempdata/wrangled_data.csv), I use the `detect_gender()` function in the __gender.py__ script to determine the likely gender of the name. 

The `extract_usable_name()` function uses this incredibly naive algorithm to extract the "usable" first name from a given first name string:

- `namestr` is something like `"William B"`
- split `namestr` by whitespace
- select the first element, i.e. `"William`

This means that poor `"C.K."` of Charles McClatchy fame will not be joining our analysis...


A new file -- [tempdata/classified_data.csv](tempdata/classified_data.csv) -- is produced. Basically, it's wrangled_data.csv with three new columns:

- gender
- ratio (the likelihood/bias of the baby boy vs girl numbers)
- usable_name - the partial string extracted from `first_name` to do the classification.


### analyze.py

Reads [tempdata/classified_data.csv](tempdata/classified_data.csv) and produces the output seen at the bottom of this README's analysis.



### Ancillary files

Here are some supporting files. You don't actually _run_ these, but they are called by the other files.

### settings.py

This contains constants, like `DATA_DIR`, that are shared across several of the scripts.


### gender.py

This contains the code to load the wrangled gender data and the `detect_gender()` function.

### pulitzer-taxonomy.csv

Um...just something I had to create for myself to efficiently scrape Pulitzer.org's weird Angular-Drupal setup. 








## Analysis

The female/male ratio for the following facets were calculated

- Across the entire membership since 1968
- Across the membership for each decade
- Across the membership in each given year


In the time period of 1968 to the current year, an estimated __40+ women__ have served on the Pulitzer Prize board compared to __170+ men__.

The [2015 board membership](http://www.pulitzer.org/board/2015) was composed of 6 women and 12 men, according to a manual count; the automated analysis counted 6 and 11, respectively, apparently not being able to classify one of the male names. The makeup of the 2015 board is 33% women, which is the tied with 1997 as the highest rate of any year.

According to the automated analysis, the 1970s did not see a single woman on the Pulitzer Board. In the 1980s, about 10% of the board members were women.




-----------------------------------

### Printout of analyze.py

The raw printout:

~~~
Since 1968, the estimated gender breakdown for the Pulitzer Prize Board membership is:
  F: 44 20%
  M: 172 76%
  NA: 9 4%
-----------------------------------------
Now let's do a decade-by-decade breakdown
1960
  F: 0 0%
  M: 16 89%
  NA: 2 11%
1970
  F: 0 0%
  M: 32 97%
  NA: 1 3%
1980
  F: 6 9%
  M: 57 86%
  NA: 3 5%
1990
  F: 16 24%
  M: 47 71%
  NA: 3 5%
2000
  F: 17 28%
  M: 43 72%
  NA: 0 0%
2010
  F: 14 33%
  M: 28 65%
  NA: 1 2%
-----------------------------------------
Now let's do a year-by-year breakdown
1968
  F: 0 0%
  M: 11 85%
  NA: 2 15%
1969
  F: 0 0%
  M: 12 92%
  NA: 1 8%
1970
  F: 0 0%
  M: 13 93%
  NA: 1 7%
1971
  F: 0 0%
  M: 13 93%
  NA: 1 7%
1972
  F: 0 0%
  M: 13 93%
  NA: 1 7%
1973
  F: 0 0%
  M: 13 93%
  NA: 1 7%
1974
  F: 0 0%
  M: 13 93%
  NA: 1 7%
1975
  F: 0 0%
  M: 13 93%
  NA: 1 7%
1977
  F: 0 0%
  M: 15 100%
  NA: 0 0%
1978
  F: 0 0%
  M: 15 100%
  NA: 0 0%
1979
  F: 0 0%
  M: 15 100%
  NA: 0 0%
1980
  F: 1 6%
  M: 16 94%
  NA: 0 0%
1981
  F: 2 12%
  M: 15 88%
  NA: 0 0%
1982
  F: 2 12%
  M: 15 88%
  NA: 0 0%
1983
  F: 3 18%
  M: 14 82%
  NA: 0 0%
1984
  F: 2 11%
  M: 15 83%
  NA: 1 6%
1985
  F: 2 11%
  M: 15 83%
  NA: 1 6%
1986
  F: 2 11%
  M: 15 83%
  NA: 1 6%
1987
  F: 3 18%
  M: 13 76%
  NA: 1 6%
1988
  F: 2 12%
  M: 14 82%
  NA: 1 6%
1989
  F: 3 18%
  M: 13 76%
  NA: 1 6%
1990
  F: 4 22%
  M: 13 72%
  NA: 1 6%
1991
  F: 5 26%
  M: 13 68%
  NA: 1 5%
1992
  F: 5 26%
  M: 13 68%
  NA: 1 5%
1993
  F: 5 26%
  M: 13 68%
  NA: 1 5%
1994
  F: 5 28%
  M: 12 67%
  NA: 1 6%
1995
  F: 6 32%
  M: 12 63%
  NA: 1 5%
1996
  F: 6 32%
  M: 12 63%
  NA: 1 5%
1997
  F: 6 33%
  M: 11 61%
  NA: 1 6%
1998
  F: 5 25%
  M: 15 75%
  NA: 0 0%
1999
  F: 5 25%
  M: 15 75%
  NA: 0 0%
2000
  F: 4 20%
  M: 16 80%
  NA: 0 0%
2001
  F: 4 21%
  M: 15 79%
  NA: 0 0%
2002
  F: 3 17%
  M: 15 83%
  NA: 0 0%
2003
  F: 4 20%
  M: 16 80%
  NA: 0 0%
2004
  F: 5 24%
  M: 16 76%
  NA: 0 0%
2005
  F: 4 21%
  M: 15 79%
  NA: 0 0%
2006
  F: 4 21%
  M: 15 79%
  NA: 0 0%
2007
  F: 5 25%
  M: 15 75%
  NA: 0 0%
2008
  F: 5 26%
  M: 14 74%
  NA: 0 0%
2009
  F: 5 26%
  M: 14 74%
  NA: 0 0%
2010
  F: 5 28%
  M: 13 72%
  NA: 0 0%
2011
  F: 4 22%
  M: 13 72%
  NA: 1 6%
2012
  F: 5 25%
  M: 14 70%
  NA: 1 5%
2013
  F: 4 21%
  M: 14 74%
  NA: 1 5%
2014
  F: 6 32%
  M: 12 63%
  NA: 1 5%
2015
  F: 6 33%
  M: 11 61%
  NA: 1 6%
~~~