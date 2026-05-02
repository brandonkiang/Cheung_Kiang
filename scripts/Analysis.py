import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_selector
import seaborn as sns
import os

if not os.path.exists("visualizations"):
    os.makedirs("visualizations")

df = pd.read_csv("cleaned_data/integrated_data.csv")

X_vars = df[["institution_type"]]
Y_num_vars = df["W-L%"]

categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, make_column_selector(dtype_include=['object', 'category']))
    ])

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestRegressor(random_state=42))
])

param_grid = {
    'classifier__n_estimators': [10, 50, 100],
    'classifier__max_depth': [None, 5, 10],
    'classifier__min_samples_split': [2, 5]
}

grid_search1 = GridSearchCV(pipeline, param_grid, scoring='neg_mean_squared_error')
grid_search1.fit(X_vars, Y_num_vars)

df["preds1"] = grid_search1.predict(X_vars)

X_vars2 = df[["num_undergrad", "SAT_reading75", "SAT_math75", "ACT_median75", "admission_rate"]]
Y_num_vars = df["W-L%"]

pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('classifier', RandomForestRegressor(random_state=42))
])

param_grid = {
    'classifier__n_estimators': [10, 50, 100],
    'classifier__max_depth': [None, 5, 10],
    'classifier__min_samples_split': [2, 5]
}

grid_search2 = GridSearchCV(pipeline, param_grid, scoring='neg_mean_squared_error')
grid_search2.fit(X_vars2, Y_num_vars)

df["preds2"] = grid_search2.predict(X_vars2)

sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

sns.boxplot(ax=axes[0], x='institution_type', y='W-L%', data=df,
            hue='institution_type', palette="Set2", legend=False)
axes[0].set_title('Distribution of W-L% by Institution Type')
axes[0].set_xlabel('Institution Type')
axes[0].set_ylabel('W-L%')

sns.scatterplot(ax=axes[1], x=df['W-L%'], y=df['preds2'], alpha=0.4, color='teal')
axes[1].plot([0, 1], [0, 1], 'r--', lw=2) 
axes[1].set_title('Model 2: Actual vs Predicted W-L%\n(Predictors: Academic & Enrollment Stats)')
axes[1].set_xlabel('Actual W-L%')
axes[1].set_ylabel('Predicted W-L%')

plt.tight_layout()
plt.savefig('visualizations/analysis_visualizations.png')