# Data Pandas Challenge

Working in teams of 3.

In this challenge we want you to find 2 - 3 datasets that will allow you to create a hypotheses against the datasets to be proven from undergoing some data analysis.

Ideally 1 or 2 of the datasets should have missing data, so that you can clean the data by either;

* Removing it
* Applying interpolation
* Or other solutions - please explain

The following datasets site has data sets that can be downloaded, of which some will have missing data.  https://archive.ics.uci.edu/datasets?skip=0&take=10&sort=desc&orderBy=NumHits&search=&Area=Business

The above link is for business data, but they have other data on their site.  The information about the dataset will tell you on the web page if it has missing data.

If possible you should attempt a merge of the data sets, for example having values relating to a city or state/county that could be added to one of the datasets.

There are plenty of other sites available for data, and in Python you also have access to the Yahoo Finance module called yFinance which provide data 15 minutes behind actual.

You should create a Jupyter Notebook that can guide us through your process of;

* Identifying the datasets
    * Textual mark up stating what datasets you used and their URLs or library inclusion
* Your hypothesis you wish to test
    * Is there a correlation between your datasets, and what did you originally set out to prove
* Cleansing of the data
    * This should include reasons for your choice of cleansing
        * Removal
        * Interpolation
    * Reasons why you chose the specific interpolation/calculation to fix missing values or outliers
* Manipulating the data into the required Dataframe
* Graphs, Charts and Tables that prove or disprove your hypothesis/correlation

Your notebook should flow and explain not just the code, but assumptions and other facts, as though you were writing a report, but with interaction from Python code, in the event a new dataset or data is available.

## Ideas

You might decide to look at current events in the new and determine what has happened to financial markets or data based on that new article - this may require obtaining data from yFinance.

Determine happiness based on GDP, or some other factors.

Price of petrol in particular countries according to their uptake of EVs.

## Extra Machine Learning (ML)

Take look at the ML features within Python.  This is specifically the sklearn module.  The official page for SciKit Learn - https://scikit-learn.org/stable/ ; on this page you'll find the getting started and example code.

For predictions you will want to review the **Getting Started** and then **Regressions**.

When working with ML modelling you will need to separate out your data into;

* Test
    * A subset of the whole data to test your prediction model against.
* Training
    * A different subset of data to the Test data to train the model on.  Normally this set may be larger than the test.
* Actual (production)
    * The entire data which predicitions will be taken from based on your prediction **model**.

## Some help and references

* [Useful links to help learn data and ML with Pandas](../Useful_links.md)
* [Useful dataset locations](../Useful_Dataset_Locations.md)