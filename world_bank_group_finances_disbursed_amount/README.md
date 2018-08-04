# World Bank Group Finances: Disbursed Amounts

## Case: What affects the amount disbursed by the World Bank for project loans?

## Summary:
Exploratory analysis of factors affecting the disbursed amount. We build a gradient boosted tree model. Feature importance is established using global `shap` values with the following features being the most important:

>- `repaid_to_ibrd` : the amount paid to IBRD
>- `due_to_ibrd` : the amount due to IBRD
>- `borrower_s_obligation` : the borrower's obligation

We investigate the different approaches towards effectively determining the most important features: `weights`, `cover`, and `gain`.