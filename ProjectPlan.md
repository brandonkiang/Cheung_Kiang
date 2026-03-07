### **Overview**

Our project aims to examine the relationship between US universities and their athletics program. Our two datasets contain information about US universities and US university athletic programs, respectively. Through this analysis, we hope to better understand how characteristics of universities relate to their athletic programs and identify patterns across institutions.

Each team member will be responsible for cleaning one of the two datasets. This process will involve handling missing values, standardizing variable formats, and ensuring consistency across fields that will later be used for merging the datasets. After cleaning, the datasets will be integrated using a shared variable that identifies each university. This integration will allow us to combine institutional and athletics information into a single dataset for analysis.

Once the datasets are merged, we will explore the data using descriptive statistics and visualizations to identify patterns and relationships between university characteristics and athletic programs. We will also perform exploratory analyses to answer our research questions and evaluate any trends that emerge from the integrated dataset.

Although individual team members will complete specific tasks, the group will work collaboratively to interpret results, refine analyses, and ensure that our findings are clearly communicated. By the end of the project, we aim not only to answer our research questions but also to demonstrate proficiency in course concepts such as file organization, ethical data handling, data acquisition, data cleaning, and data integration.


### **Team**

Both members will collaborate on every step of the project, with tasks consisting of cleaning each respective dataset and conducting exploratory analysis.


### **Research Question**
1) Do colleges in the top quartile of academic selectivity (based on the incoming cohort's median ACT/SAT scores / acceptance rate) generate significantly different total athletic revenue than colleges in the bottom quartile?
2) How does the size of the incoming cohort moderate the relationship between total athletic recruiting expenses and total athletic revenue?

### **Datasets**

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


### **Timeline**

  - **Step 1**: Cleaning & Data Integration
    - Both datasets will be collected through CSV files downloaded through their respective websites and cleaned to only contains specific columns of interest. Each member will work on cleaning one particular dataset, while still providing advice on how to format the data as to render it useful. Following the cleaning process, we may consider merging the two datasets on the university ID variable such that each row represents a U.S. university and the columns provide descriptive statistics such as acceptance rate, SAT/ACT scores,  and athletics revenue/expenses, among others.

  - **Steps 2 & 3**: exploratory data management
    - Evaluate trends between athletics revenue/expenses and admission sizes/academic statistics. 

  - **Steps 4 & 5**: conduct data analysis to answer each research question (each person will do analysis on one research question)
    - Based on the trends identified in steps 2 and 3, conduct analyses that answer the respective research questions. Each member will work primarily on one research question but will collaborate to ensure the findings are thorough, in-depth, and fully answer the question of interest.
   
  - **Step 6**: Documentation write-up with evidence
    - Document the metadata so that the variables of interest are easy to understand. Both members will collaborate on documenting.

  - **Step 7**: Finalize report
    - Make sure all the metadata and instructions for reproducibility are clearly outlined. Provide steps for cleaning, integration, and exploratory analysis of data such that anyone with these instructions can understand the data and how our analyses/findings were discovered.

### **Constraints:** 
One limitation of the College Scorecard dataset is the lack of clarity regarding the time frame used for certain variables. It is sometimes unclear whether the reported values   represent a single academic year, a specific student cohort, or an aggregate across multiple years. This ambiguity may make it more difficult to interpret the results accurately or compare variables consistently across institutions. Additionally, since the athletic data is self-reported by institutions to demonstrate Title IX compliance, there may be an incentive for universities to boost participation numbers for female athletes. Additionally, there is no standardized categorization for how expenses and revenues are calculated between universities, so certain institutions may have varying calculations.


### **Gaps:** 
Our data does not contain information on the total university enrollment (only information on the size of the fall 2023 cohort).
