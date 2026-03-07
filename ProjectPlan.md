### **Overview**

Our project aims to examine the relationship between U.S. universities and their athletics program. Our two datasets contain information about U.S. universities and U.S. university athletic programs, respectively. Through this analysis, we hope to better understand how characteristics of universities relate to their athletic programs and identify patterns across institutions.

Each team member will be responsible for cleaning one of the two datasets. This process will involve handling missing values, standardizing variable formats, and ensuring consistency across fields that will later be used for merging the datasets. After cleaning, the datasets will be integrated using a shared variable that identifies each university. This integration will allow us to combine institutional and athletics information into a single dataset for analysis.

Once the datasets are merged, we will explore the data using descriptive statistics and visualizations to identify patterns and relationships between university characteristics and athletic programs. We will also perform exploratory analyses to answer our research questions and evaluate any trends that emerge from the integrated dataset.

Although individual team members will complete specific tasks, the group will work collaboratively to interpret results, refine analyses, and ensure that our findings are clearly communicated. By the end of the project, we aim not only to answer our research questions but also to demonstrate proficiency in course concepts such as file organization, ethical data handling, data acquisition, data cleaning, and data integration.

### **Team**

Both members will collaborate on every step of the project, with tasks consisting of cleaning data, conducting exploratory analysis, and generating visualizations to interpret trends and relationships between U.S. univeristy admissions statistics and their respective athletics programs.

### **Research Questions**
1) Do colleges in the top quartile of academic selectivity (based on the incoming cohort's median ACT/SAT scores / acceptance rate) generate significantly different total athletic revenue than colleges in the bottom quartile?
2) How does the size of the incoming cohort moderate the relationship between total athletic recruiting expenses and total athletic revenue?

### **Datasets**

Note: The two datasets will be linked on the "unitid" variable, which represent the university ID. Alternatively, datasets can also be linked on the university name, given they are formatted the same in the two respective datasets.

**1) U.S. University Admissions Data**

This dataset contains information on all US universities, including institutional characteristics, costs, and student outcomes. 

- **License**: Public Domain

- **Copyright**: No copyright restrictions or licensing fees

- **Terms of Use**: No License required. Commercial use and redistribution 

- **Privacy and Confidentiality**: To protect student privacy, the data reported in the College Scorecard dataset is aggregated across institutions and student populations. Individual student records are not included, and sensitive information that could identify specific individuals is either excluded or summarized. In some cases, values may be suppressed or omitted when the number of observations is too small to ensure anonymity.

- **Consent**: Mandated public disclosure (Public Domain)

- **Citation**: U.S. Department of Education. (n.d.). College Scorecard data. College Scorecard. https://collegescorecard.ed.gov/data/

**2) U.S. Athletics Data**

This dataset contains 2023-2024 athletics information for all U.S. universities. Variables from this dataset include information detailing athletics recruiting expenses, total   revenue generated, and total participants per team. We plan to use the information from this dataset to examine the relationship between U.S. university athletics and general      student body characteristics.

- **License**: Public Domain

- **Copyright**: No copyright restrictions or licensing fees. Users are free to reproduce, modify, and distribute the data.

- **Terms of Use**: No License required. Commercial use and redistribution are permitted.

- **Privacy and Confidentiality**: The dataset is aggregated at the institutional level and provides totals for participants, coaching staff, and revenues/expenses, but does not   contain names or any unique identifiers. FERPA compliant.

- **Consent**: Mandated public disclosure (Public Domain)

- **Citation**: U.S. Department of Education, Office of Postsecondary Education. Equity in Athletics Data Analysis (EADA). [Year of Data]. Available at:                         https://ope.ed.gov/athletics/

### **Timeline**: 

We aim to follow the DataONE Data lifecycle discussed in lecture consisting of the planning, collection, description, preservation, integration, and analyzation of data.

  - **Step 1**: Data Collection and Cleaning
    - Both datasets will be collected as CSV files downloaded through their respective websites and cleaned to only contains specific columns of interest. Cleaning methods that will be considered include standardizing the variables and their content such that they are easy to interpret and understand We will handle missing values in the context of its missingness and collaborate to discuss whether ignoring, dropping, or imputation is the most advisable strategy. Each member will work on cleaning one particular dataset, while still providing support and insight on how to format the data as to render it useful.
    - Note that while the two datasets are both formatted as CSVs, they have distinct schemas that render them unique yet integratable.
    - During this process, we will document exactly how the data is collected and cleaned and provide proper documentation as to ensure its reproducibility with respect to our workflow. Additionally, information regarding the ethical, legal, and policy constraints with respect to the two datasets will be identified and logged to ensure we respect the terms of use, licenses, and copyright laws. We will ensure that we abide by all restricitons and properly cite the data we utilize in this project.
   
  - **Step 2**: Data Integration
    - Following the cleaning process, the two datasets will be merged by the "unitid" variable that uniquely identifies each university institution. This merging process will likely be conducted using the Pandas library within Python.
   
  - **Step 3**: Exploratory Data Management
    - Once the data has been merged, we will aim to evaluate trends between athletics revenue/expenses and admission sizes/academic statistics. Using visualizations and various descriptive statistics, we aim to generate findings regarding the relationship between university admissions and their athletics programs. This process will be a collaborative effort with both members pitching in ideas on how to interpret the findings.

  - **Step 4**: Data Analysis
    - Based on the trends identified in step 3, we will conduct analyses that answer the respective research questions. Each member will work primarily on one research question but will collaborate to ensure the findings are thorough, in-depth, and fully answer the question of interest. This step serves as an extension to step 3.
   
  - **Step 5**: Documentation write-up with evidence
    - Document the metadata so that the variables of interest are easy to understand. The goal of this step is to ensure that anyone who looks at our project and the corresponding metadata will be able to confidently understand not only the goal of the proejct, but also understand the workflow, analysis, and how everything came together. Both members will collaborate on documenting.

  - **Step 6**: Finalize report
    - Make sure all the metadata and instructions for reproducibility are clearly outlined. Provide steps for cleaning, integration, and exploratory analysis of data such that anyone with these instructions can understand the data and how our analyses/findings were discovered.

### **Constraints:** 
One limitation of the College Scorecard dataset is the lack of clarity regarding the time frame used for certain variables. It is sometimes unclear whether the reported values   represent a single academic year, a specific student cohort, or an aggregate across multiple years. This ambiguity may make it more difficult to interpret the results accurately or compare variables consistently across institutions. Additionally, since the athletic data is self-reported by institutions to demonstrate Title IX compliance, there may be an incentive for universities to boost participation numbers for female athletes. Additionally, there is no standardized categorization for how expenses and revenues are calculated between universities, so certain institutions may have varying calculations for their expenses and revenue that may skew results.

### **Gaps:** 
Our data does not contain information on the total university enrollment (only information on the size of the fall 2023 cohort). Therefore, the athletics data may not reflect the entire student body and only the incoming freshmen cohort.
