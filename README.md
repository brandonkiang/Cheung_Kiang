# Predicting College Athletic Success Using Academic Selectivity

## Contributors
* Brandon Kiang (bkiang2)
* Rachel Cheung (rcheu2)

## Summary

## Data profile
### College Basketball Dataset
The structure of the college basketball dataset is a CSV file represented in a tabular format, with rows representing unique combinations of colleges and years and columns representing descriptive statistics regarding the college team’s success/performance in that given year. 

As previously mentioned, the college basketball dataset contains information regarding college basketball team performance in a given season. Teams with an “ncaa” label located next to their name represent colleges that made the NCAA March Madness tournament in that given season and is often used to represent a rather successful season, as a tournament berth technically deems them as a top 64 team in the country. The specific contents of the dataset with respect to the descriptive variables vary slightly in what they analyze. For instance, there are some variables that depict performance baselines, such as the variables that depict raw win and loss counts, as well as the overall win percentage. However, there are also some contextual metrics that measure the team’s strength of schedule (`SOS`) to provide some context as to how difficult their scheduling was with respect to the opponent's records. This can be used to help contextualize team performance in a given season. 

The combined dataset covers five academic seasons from 2019–20 to 2023–24, spanning both men's and women's NCAA Division I programs. The inclusion of both genders is a notable feature, as it enables gender-disaggregated analysis of how institutional factors relate to athletic success across two distinct competitive landscapes. Each individual season table contains several hundred schools, reflecting the full population of Division I programs active in that year rather than a sample, which eliminates concerns about sampling bias. The data is clean and consistently structured across years and genders, as Sports Reference applies uniform column definitions and calculation methods across all seasons.

The men's dataset is stored within the project repository at [data/cbb_records_2019_2024.csv](https://github.com/brandonkiang/Cheung_Kiang/blob/main/data/cbb_records_2019_2024.csv) and the women's dataset at [data/wcbb_records_2019_2024.csv](https://github.com/brandonkiang/Cheung_Kiang/blob/main/data/wcbb_records_2019_2024.csv).

Sports Reference publishes its data for free public access for personal and educational use, though it retains copyright over the compiled statistics and their presentation. The statistics represent aggregated team-level performance rather than any individual player data, so there are no privacy concerns associated with this dataset, and no ethical clearance is required for its use.

As this dataset contains extensive information regarding college basketball program success, it can be effectively used in combination with academic data to relay information about college basketball performance. When combined with the college scorecard dataset, this college basketball dataset will be effective in providing detailed information regarding how successful a particular college was in a given year, using information such as win percentage and playoff successes.

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
