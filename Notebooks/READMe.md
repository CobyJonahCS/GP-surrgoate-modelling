# Airfoil Self-Noise Prediction

Predicting scaled sound pressure level (SSPL) from aerodynamic and
geometric airfoil parameters using linear, tree-based, and probabilistic
machine-learning models.

## Overview

The goal of this project is to predict airfoil self-noise using the
NASA Airfoil Self-Noise dataset and compare models with different levels
of complexity.

The project progresses from an interpretable linear baseline to nonlinear
machine-learning approaches:

- Multiple Linear Regression
- Linear Regression with selected interaction terms
- XGBoost Regression
- Gaussian Process Regression

Alongside point-prediction accuracy, Gaussian Process Regression is used
to explore uncertainty quantification.

## Dataset

The dataset contains 1,503 experimental observations.


Input features:

    f: Frequency in Hertzs [Hz].
    alpha: Angle of attack (AoA, α), in degrees [°].
    c: Chord length, in meters [m].
    U_infinity: Free-stream velocity, in meters per second [m/s].
    delta: Suction side displacement thickness (𝛿), in meters [m].

Output:

    SSPL: Scaled sound pressure level, in decibels [dB].


Source: NASA / UCI Airfoil Self-Noise Dataset.  https://www.kaggle.com/datasets/fedesoriano/airfoil-selfnoise-dataset

## Exploratory Data Analysis

EDA was used to investigate:

- feature distributions and skewness
- correlations with SSPL
- nonlinear relationships
- possible interaction effects


The strongest linear relationships with SSPL were observed for frequency
and displacement thickness.

EDA also suggested interactions between:

- frequency and free-stream velocity
- frequency and angle of attack
- angle of attack and displacement thickness

## Experimental Setup

a 70 30 train test split was used along with a random state of 1000.

Min-Max scaling was used consistently throughout the project.

Five-fold cross-validation was performed on the training data to assess
model stability while keeping the test set untouched for final evaluation.

Performance was evaluated using:

- R2
- MAE
- MSE
- RMSE

## Models

### 1. Multiple Linear Regression

A simple interpretable baseline using the five original predictors.

Residual analysis showed systematic structure, suggesting that the
relationship between the aerodynamic variables and SSPL could not be
fully represented by a linear model.

### 2. Linear Regression with Interactions

Three interaction terms identified during EDA were added:

`frequency × velocity`

`frequency × angle of attack`

`angle of attack × displacement thickness`

The interaction model improved performance moderately but structured
residual patterns remained.

### 3. XGBoost Regression

XGBoost was used to capture nonlinear relationships between targets and features.

Hyperparameters were optimized using Bayesian optimization with
five-fold cross-validation on the training set.

XGBoost produced the strongest point-prediction performance.

### 4. Gaussian Process Regression

Gaussian Process Regression was used as a probabilistic nonlinear model.

An RBF-based kernel was used to model nonlinear relationships while
predictive standard deviations were used to quantify uncertainty.

In addition to conventional regression metrics, uncertainty was assessed
using:

- 95% predictive intervals
- empirical coverage
- calibration curves

## Results

XGBoost achieved the highest predictive accuracy, while Gaussian Process
Regression achieved comparable nonlinear performance while additionally
providing observation-specific uncertainty estimates.

## References

NASA / UCI Airfoil Self-Noise Dataset

Sabri, K., Ferroudji, H. & Gaceb, M. (2026).
Data-Driven Prediction and Metaheuristic Optimization of Airfoil
Self-Noise Using Machine Learning Algorithms.