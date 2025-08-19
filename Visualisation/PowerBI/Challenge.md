## Power BI mini‑project: Clean, analyse, and tell a data story

This is a focused, hands‑on project where you will import a dataset, or datasets; clean and filter it with Power Query, build a simple data model, create core measures, then design a dashboard to tell a clear, evidence‑based story which you will present to the class.

---

## Deliverables and assessment

* **Deliverable 1:** A Power BI (.pbix) file with a dashboard. 
* **Deliverable 2:** A short appendix page (or notes pane) showing the key transformation steps taken in Power Query.
* **Deliverable 3:** A short 5 – 10 minute presentation to tell the story using your Power BI dashboard.
* **Brief criteria:**
    * **Data import accuracy:** Correctly loaded data and applied appropriate data types. 
    * **Cleansing and modeling:** Clear, reproducible transformations and a logical model with relationships. 
    * **Measures quality:** Applied additional columns, and/or have applied defined DAX measures. 
    * **Visual effectiveness:** Visuals match questions; clear labels, titles, and accessible formatting.
    * **Narrative coherence:** Story answers specific questions or provides evidence as to whether a hypothesis is true or false, supported by the dashboard and filters. 

---

## Dataset and setup

* **Dataset choice:** Use single or multiple data sources from the Internet, or from the Python Data Wrangling Labs to create your story data.
    * Some possible sources can be found at;
        * [Useful Data Sets](../../Data/Useful_Dataset_Locations.md) 
        * [Published data - Office for National Statistics](https://www.ons.gov.uk/economy/datalist?filter=datasets) 
            * [Open Geography Portal](https://geoportal.statistics.gov.uk/) 
        * [Find open data - data.gov.uk](https://www.data.gov.uk/)
        * [Registry of Open Data on AWS ](https://registry.opendata.aws/)
    * Data can be in any format as long as you can import it into Power BI (PBI)
        * Excel spreadsheet, PBI semantic models, Dataverse, Web page, JSON, XML, Parquet, MS Access, MySQL, 
        * For a full list check the Get data icon in PBI and select More... 
* Backup option: CSV files provided in the Python Data Wrangling labs zip file

## Step‑by‑step guidance

### Import and model

1. **Open Power BI Desktop:** Start a new report; save it as “PBI Story Telling.pbix.” 
2. **Get Data:** Home > Get Data > More... > select your dataset file. 
3. **Preview check:** Verify headers, sample rows, and delimiters; click Transform Data to open Power Query. 
4. **Set data types:** In Power Query, set Date columns to Date, numeric columns to Decimal Whole/Fixed Decimal as appropriate. 
    1. If using multiple data sets, merge datasets, and create any necessary extra columns
5. **Promote headers:** Use Home > Use First Row as Headers if needed. 
6. **Name the query:** Rename to “Sales” (or similar) in the Queries pane. 
7. **Create Date table (optional but recommended):** Close & Apply, then Modeling > New table, and add:

    ```
    Date = CALENDARAUTO()
    ```

    or use the following for a specific date range

    ```
    Date = CALENDAR(DATE(2000, 1, 1), DATE(2023, 11, 20))
    ```

8. **Mark as date table:** Modeling > Mark as date table > select Date[Date]. 
9. **Create relationships:** Model view > relate Sales[OrderDate] to Date[Date]. 

### Cleanse and transform (Power Query)

1. **Remove empty rows/columns:** Home > Reduce Rows > Remove Blank Rows; remove entirely empty columns. 
2. **Trim and clean text:** Transform > Format > Trim and Clean for text fields (e.g., Country, Category). 
3. **Fix inconsistent categories:** Transform > Replace Values (e.g., “United Kngdom” → “United Kingdom”). 
4. **Handle errors:** Home > Keep Rows > Keep Errors to inspect; fix type issues or Replace Errors with null; then Remove Errors. 
5. **Split combined fields:** If a field contains “Category — Subcategory,” use Split Column > By Delimiter. 
6. **Derive fields:** Add Column > Custom Column, e.g., Revenue = Units * Unit Price (if not provided). 
7. **Filter rows:** Home > Keep Rows > Keep Range or Filter on Date to keep a focused period (e.g., last 24 months). 
8. **Remove duplicates:** Home > Remove Rows > Remove Duplicates on OrderID if duplicates exist. 
9. **Group for sanity checks:** Transform > Group By to compute total Revenue by Category; spot anomalies. 
10. **Document steps:** In the Applied Steps pane, rename steps with clear labels (right‑click > Rename). 

Then click **Close** & **Apply**.

### Measures (DAX) Examples

1. **Total Sales:**
    ```
    Total Sales = SUM(Sales[Revenue])
    ```
2. **Total Profit:**
    ```
    Total Profit = SUM(Sales[Profit])
    ```
3. **Profit Margin:**
    ```
    Profit Margin = DIVIDE([Total Profit], [Total Sales])
    ```
4. **Average Order Value:**
    ```
    AOV = DIVIDE([Total Sales], DISTINCTCOUNT(Sales[OrderID]))
    ```
5. **Sales YoY (if Date table is present):** 
    ```
    Sales YoY = [Total Sales] - CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date]))
    ```

### Visuals and filtering

1. **Define the question:** Choose one core question (e.g., “Which segment is driving profit growth in the last year?”). 
2. **Build key visuals:** Use a bar/column chart (Top Categories by Sales), line chart (Sales over Time), map or treemap (by Country/Segment), and a KPI card (Total Sales, Profit Margin). 
3. **Add slicers:** Add slicers for Date (relative date or between), Country, and Segment; set single select when appropriate. 
4. **Use filters properly:** Use Page filters for persistent constraints (e.g., exclude internal orders); avoid hard‑coding filters inside visuals unless necessary. 
5. **Sort and label:** Sort bars by value; add data labels only where they aid reading; keep units consistent. 
6. **Drill and tooltips:** Enable drill‑down on hierarchy visuals and add a tooltip page showing AOV and Margin for context. 
7. **Layout:** Arrange a Z‑pattern: top‑left KPI, top‑right trend, bottom visuals for breakdowns; keep white space. 

## Dashboard polish

1. **Titles and subtitles:** Write an action‑oriented title (e.g., “Consumer segment revenue up 12% YoY, but margin dips”). 
2. **Annotations:** Add short text boxes highlighting inflection points or outliers. 
3. **Bookmarks:** Create a “Default View” bookmark and a “Insight View” bookmark (e.g., UK + Consumer filtered). 
4. **Theme:** Apply a built‑in theme; ensure color contrast for accessibility; use one highlight color for the hero metric. 
5. **Performance check:** Interact with slicers; confirm visuals update quickly and correctly.

---

## Storytelling prompts and guidance

* **Audience:** Identify who your audience will be for the data story you are presenting, e.g. Business manager deciding where to focus next quarter on sale of products. 
* **Core question examples:** 
    * **Growth:** Which categories drove revenue growth in the last 12 months? 
    * **Profitability:** Where are margins strongest vs. weakest by segment and country? 
    * **Seasonality:** What seasonal patterns affect sales, and how should we plan inventory? 
* **Narrative arc:** 
    * **Beginning:** State the question and baseline metric (e.g., total sales and margin last year). 
    * **Middle:** Show comparisons (by segment/country/category) and highlight the drivers with annotations. 
    * **End:** Recommend one action (e.g., “Prioritise Subcategory A in the UK; monitor margin leakage in Consumer segment”). 
* **Quality checks:** 
    * *Consistency:* Numbers sum across visuals; filters don’t contradict titles. 
    * **Clarity:** Every visual answers a distinct sub‑question; remove any redundant chart. 
    * **Simplicity:** Ensure your dashboard is not cluttered. Make use of separate pages/tabs, but ensure they make sense and the order is correct.

---

# Power BI useful links and help

* [Useful Links](Useful_Links.md)