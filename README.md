# Predicting College Athletic Success Using Academic Selectivity

## Contributors
* Brandon Kiang (bkiang2)
* Rachel Cheung (rcheu2)

## Summary

## Data profile
### College Basketball Dataset

### College Scorecard Dataset
The College Scorecard dataset is a multi-year panel dataset provided by the U.S. Department of Education, stored in CSV format. Each row represents a unique institution-year combination, meaning a single college or university appears multiple times across the dataset — once for each academic year it is observed. Columns capture a wide range of descriptive statistics for each institution in that year, covering institutional characteristics, admissions, enrollment, student demographics, financial aid, costs, and post-enrollment outcomes. The dataset is wide in format, with thousands of columns per observation, many of which contain missing values (coded as NaN) due to reporting limitations.

The dataset contains information on thousands of degree-granting postsecondary institutions across the United States. For the purposes of this project, the most relevant variables include institutional control type (public vs. private non-profit), undergraduate enrollment figures, and measures of academic selectivity such as admission rates and standardized test score distributions (SAT/ACT 75th percentiles). These variables serve as the primary institutional predictors used to investigate differences in college basketball success. The dataset also includes school identifiers, such as institution names, which serve as keys for merging with basketball performance data. Additional variables such as region, Carnegie classification, and degree programs offered provide supplementary context for characterizing institutions.

The College Scorecard spans multiple academic years, enabling longitudinal analysis of how institutional characteristics change over time and how those changes may correspond to shifts in athletic performance. The dataset is large in both dimensions, covering over 6,000 institutions annually across many years, but requires significant filtering and preprocessing for this project, as the analysis is limited to four-year institutions with active NCAA Division I basketball programs. Many columns are sparsely populated due to suppression policies designed to protect student privacy, particularly at smaller institutions, which necessitates careful handling of missing data. Despite these gaps, the variables directly relevant to this study, control type, enrollment size, and selectivity metrics, are consistently reported for the large, Division I–eligible institutions that form the analytical sample.

The dataset is located at [data/scorecard.csv](https://github.com/brandonkiang/Cheung_Kiang/blob/main/data/scorecard.csv) within the project repository.

The College Scorecard dataset is publicly available and published by the U.S. Department of Education under an open data policy, meaning there are no licensing restrictions on its use for research or educational purposes. The data is aggregated at the institution level rather than the individual student level, so there are no direct privacy concerns associated with its use in this project. This reflects the federal government's compliance with the Family Educational Rights and Privacy Act (FERPA), which governs the confidentiality of student education records. No additional ethical clearance is required to use this dataset, as it contains no personally identifiable information.

The College Scorecard dataset is central to both research questions guiding this project. For the first question, comparing basketball success rates between public and private institutions, the dataset provides the institutional control variable (`institution_type`) that classifies each school as public, private non-profit, or private for-profit, enabling direct group comparisons when merged with basketball outcome data. For the second question, examining how undergraduate enrollment size and academic selectivity predict basketball success, the dataset supplies the key predictor variables: undergraduate enrollment (`num_undergrad`) and admissions-related selectivity metrics such as admission rate (`admission_rate`) and standardized test score ranges. Together, these variables allow for the construction of a merged analytical dataset in which institutional characteristics drawn from the College Scorecard can be evaluated against measures of basketball program performance, directly operationalizing the predictors specified in both research questions.

## Data quality

## Data cleaning

## Findings

## Future work

## Challenges

## Reproducing

## References
