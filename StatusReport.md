# Status Report: MLS Player Performance and Salary Analysis
## Overview
Our project analyzes whether player salary in Major League Soccer relects measureable on field performance. We are integrating two public datasets: 2025 MLS player statistics from FBref and player compensation data from the MLS Players Association Salary Guide. The goal is to determine whether high paid players tend to produce stronger statistical outputs, identify which performance variables are most associated with compensation, and explore whether some players appear overpaid or underpaid relative to production. Since completing Milestone 2 we have made progress on data preparation and identified key challenges such as mismatched player names and differences in dataset formats.
This report outlines our progress on each planned task, updates our timeline, explains any changes to our project plan, and describes challenges we have encountered so far.

## Status of Planned Tasks
### 1. Finalize research questions
**Status: Complete**
We finalized our research questions from Milestone 2:
- Do higher-paid MLS players produce stronger performance statistics?
- Which performance metrics are most associated with salary?
- Are some players overpaid or underpaid?
- How efficiently do MLS teams convert salary into performance?

These questions remain unchanged and clearly align with our datasets.

## 2. Clean and Preprocessing data
**Status: In Progress**
We began loading both datasets into Python using Pandas.
- The salary dataset is easier to load and clean
- The FBref dataset requires more formatting depending on the table
We have succesfully inspected columns and confirmed key variables. We have completed the cleaning & preprocessing in Python and our processed datasets can be found here: (LINK HERE). However, we want to use the new tool shown in class "OpenRefine" to redo our preprocessing to double check our work with another platform.
