## Task Updates
As of the end of week 10, both datasets have already been collected through direct downloading as xlsx files from their corresponding websites.
They have also been attached to the GitHub repository as their own separate folders, with corresponding metadata and data documentation provided:
* [2023-24 College Scorecard Data (Raw)](https://github.com/brandonkiang/Cheung_Kiang/tree/3309e50c6e5b8c8a51a9bec2f0b9d9a187650789/23-24_College_Scorecard_Raw_Data)
* [2023-24 College Athletics Data (Raw)](https://github.com/brandonkiang/Cheung_Kiang/tree/3309e50c6e5b8c8a51a9bec2f0b9d9a187650789/US_23-24_College_Athletics)

Each team member was assigned to clean a dataset. Since both datasets contained extensive attributes (~3300 for scorecard data and ~169 for athletics data), we decided to clean and simplify the data prior to integration. We ultimately decided upon which columns to keep through careful deliberation of how they reflect our main research questions and their usefulness in that regard. The following are links to the folders containing the process used for cleaning each dataset and the final, cleaned CSV:
* [Cleaned College Scorecard Data](https://github.com/brandonkiang/Cheung_Kiang/tree/3309e50c6e5b8c8a51a9bec2f0b9d9a187650789/Cleaned_College_data)
* [Cleaned Athletics Data](https://github.com/brandonkiang/Cheung_Kiang/tree/3309e50c6e5b8c8a51a9bec2f0b9d9a187650789/Cleaned_Athletics_data)

In preparation for data integration in the following week, we began cleaning and standardizing the data to ensure proper mapping and record linkage. Standardization processes included renaming columns so that both datasets had corresponding column names for schema matching purposes. Additionally, we further explored data quality, checking for issues related to accuracy, completeness, consistency, and timeliness:
* **Accuracy:** There are no significant concerns regarding the accuracy of either dataset, as both datasets were extensively checked during the collection process. However, it is important to note that there is a possibility of incorrect reporting from the respective institutions and should be considered when determining conclusions for the research questions.
* **Completeness:** Within the admissions data, there were a total of 25 rows found to have missing values for the “OPEID” variable, affecting the ability to link based on the Office of Postsecondary Education identification code. Additionally, there seem to be signigicant missing values in some of our attributes of interest, which we will touch on later on. As for the athletics data, there are fewer concerns regarding column completeness as there are no null or missing values directly encoded. However, one thing our group did notice was that certain observations have total recruitment expenses and total student aid values of 0, which seems concerning regarding how realistic it is. It is possible that these values were encoded as 0 to represent missingness and will be considered as such moving forward.
* **Consistency:** There are no significant concerns regarding the consistency of either dataset. There seem to be no violations of schematic rules, and the formatting of data is consistent across observations.
* **Timeliness:** There are no concerns regarding the timeliness of the two datasets. Since both datasets reflect data from the 2023-2024 academic year, there should be no further updates in either dataset, given that this is a cross-sectional study, not a longitudinal one.

For our data integration workflow, we utilized the record linkage package to merge our two datasets. The two datasets were first blocked by the state variable, thus reducing the number of comparisons required in the record linkage process. We compared the two datasets on the institution name variable, using the Levenshtein method as our metric with a threshold of 0.85. Following the integration process, we dropped any duplicate institution rows and used the admissions dataset as our main reference for duplicate entries/conflicting results.

After this week, we are ready to perform Exploratory Data Analysis on our integrated data and begin analyzing the data to answer our research questions.

## Updated Timeline

### **Week 11: Data Integration (Due 04/05)**
In week 11, we built upon last week’s work by preparing the two datasets for data integration. To ensure proper integration, we first standardized the corresponding datasets to ensure proper matching. As mentioned in the previous week, we discovered some missingness with respect to the “OPEID” variable and thus decided to move against using direct merging/joining methods for our integration process. Instead, we opted to use the record linkage package within Python. To do so, we first blocked on the state variable to reduce the number of comparisons required in the record linkage process. After blocking, we compared institution name values across the two datasets using the levenshtein method and a threshold of 0.85. Once the integration was completed, we checked for potential duplicate values and conducted data fusion to sort out any conflicting values for certain rows. In our management of conflicting values, we used the admissions dataset as our reference due to its higher source integrity relative to the athletics dataset.

### **Week 12: Exploratory Data Analysis (Due 04/12)**
In this coming week, we will explore relationships between the two datasets through the newly created integration dataset. Through numerical analysis and the creation of visualizations, we hope to perform some exploratory analyses surrounding the relationships between various attributes, including the average standardized test scores of newly admitted students and their respective athletics program’s revenue. Through the calculation of summary statistics for various numeric variables such as their test scores and revenue/expenses, we aim to identify trends between universities as well as single out potential outliers that could later influence our analyses. Additionally, through the development of various visualizations, we aim to provide graphical depictions of the relationships between selective/competitive admission rates and athletic successes.

### **Week 13: Data Analysis (Due 04/19)**
Following our exploratory analysis, we will begin the actual analysis aspect of the project. Since we plan to identify the relationship between selective/prestigious institutions and the success of their athletic programs in terms or revenue generated, we will likely fit regression models. However, there is some flexibility with respect to model selection that may be considered as we get closer to this week. After fitting our regression models, we plan on further analyzing the relationship between our variables of interest through the use of numerical summaries and visualizations.

### **Week 14: Conclusions (Due 04/26)**
In the week prior to the deadline of the project, we will perform conclusions based on the analysis we conducted in the weeks prior. We hope to answer our two main research questions and discover any relationships between college admissions data and athletic success / revenue generation. This week, we will also further discuss potential limitations to our conclusions based on the quality of our data that may limit how general we can make our findings.

### **Week 15: Documentation Write-Up (Due 05/03)**
Following the generation of our conclusion, we will fine-tune our documentation to ensure everything is properly labeled and easy to understand. To ensure proper documentation, we aim to start fresh from a blank workspace and follow our detailed steps to ensure reproducibility. This includes ensuring the data collection, cleaning, processing, and analyzation processes are all consistent with what we wrote and discussed throughout the project.

### **Week 16: Finalize Report (Due 05/05)**
By the beginning of week 16 prior to the project deadline of May 5th, we aim to finalize any loose ends within the project. This will likely consist of ensuring our project accurately follows our data lifecycle and is reproducible.


## Changes
Based on the feedback received from milestone 2, we have updated the team member roles and responsibilities to properly distinguish what tasks each group member will be responsible for and aim to accomplish throughout the duration of the project as follows: 
* **Rachel:**
  * Roles, Responsibilities, Tasks: collect, clean, process, and analyze the college admissions data
    * Generate analyses through regression models that analyze the relationship between college admissions academic performance and athletic revenue
* **Brandon:**
  * Roles, Responsibilities, Tasks: collect, clean, process, and analyze the college athletics data
    * Integrate the two datasets through record linkage and deduplication.
    * Generate analyses and visualizations that analyze the relationship between incoming cohorts sizes and athletics program revenues/expenses

Note that while each individual will work primarily on their own dataset, they will still collaborate to ensure analyses and findings are accurate and informative. Additionally, some steps will require collaboration such as the data cleaning process to ensure the corresponding attributes are standardized and ready for integration.

Changing the timeline structure:
We changed the structure of the timeline to include week numbers and dates that properly detail when certain tasks are expected to be completed by. As opposed to simply being a sequence of steps, there are now specific date deadlines associated with the tasks to maintain structure and order throughout the project, ensuring the group is on top of all work and does not fall behind the weekly deadlines.


## Challenges
* The college scorecard data had ~6400 rows before integration, and significant amounts of missing values in some variables. After integration, there are ~2000 rows left (similar in size to the athletics data). However, there are still significant amounts of missing data (~1000) for some attributes (i.e., SAT and ACT score variables). Since our first research question depends on those attributes, we might consider formulating a different research question. Next week, we will try different methods of handling missing values. However, since over half the values are missing, we are not as optimistic.

* During the integration process, there were a few issues surrounding duplicate values that made the output seem to be larger than expected. To resolve this issue, we conducted data fusion and chose the admissions data to be of higher priority when considering duplicate values.



## Member Contributions
* **Rachel:** First, I collected 2023-2024 college data from https://collegescorecard.ed.gov/data/. Then, I imported the CSV into a Jupyter Notebook and, using the data dictionary, I selected the columns most relevant for answering our research questions. To prepare the data for integration, I cleaned it by renaming columns, mapping variables for readability, and converting them to lowercase for consistency. Lastly, I uploaded the Jupyter Notebook I used for cleaning and the cleaned CSV. For the milestone updates, I contributed to the timeline and wrote part of the challenges we faced.
* **Brandon:** In this milestone, I went through the process of collecting, cleaning, and integrating data for our project. First, I collected the raw 2024 college athletics data from https://ope.ed.gov/athletics/ as an excel file. After collecting the data, I conducted the cleaning process through OpenRefine, with major changes being the standardization of variables. For instance, I changed various variables to lowercase, trimmed whitespace, and renamed variables to match the casing/structure of the admissions dataset. Furthermore, I split the column detailing whether the college is public or private and the length of the university into two separate rows to match the structure of the admissions data. Finally, I reformatted the zip codes to ensure there was a hyphen included between the first 5 digits and the last 4 digits if applicable. Once the data was cleaned, I pulled the two cleaned datasets and integrated them through blocking and record linkage as mentioned above.
