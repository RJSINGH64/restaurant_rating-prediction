def data_drift(self, base_df: pd.DataFrame, current_df: pd.DataFrame, report_key_name: str):
    """
    Check data drift between base and current datasets for both numerical and categorical features.

    Args:
        base_df (pd.DataFrame): The baseline dataset.
        current_df (pd.DataFrame): The current dataset to compare.
        report_key_name (str): Key name for storing the drift report.

    Returns:
        None: Saves the drift report in self.validation_error[report_key_name].
    """
    try:
        drift_report = dict()

        base_columns = base_df.columns
        current_columns = current_df.columns

        for base_column in base_columns:
            if base_column not in current_columns:
                logging.warning(f"Column {base_column} is not present in the current dataset.")
                continue
            
            base_data = base_df[base_column].dropna()
            current_data = current_df[base_column].dropna()

            # Handle numerical features
            if base_data.dtype in [np.float64, np.int64]:
                logging.info(f"Checking numerical column drift: {base_column}")
                ks_stat, ks_p_value = ks_2samp(base_data, current_data)

                drift_report[base_column] = {
                    "pvalues": float(ks_p_value),
                    "same_distribution": ks_p_value > 0.05,
                    "statistic": float(ks_stat),
                }

            # Handle categorical features
            elif base_data.dtype == 'object':
                logging.info(f"Checking categorical column drift: {base_column}")

                # Calculate category distributions
                base_dist = base_data.value_counts(normalize=True)
                current_dist = current_data.value_counts(normalize=True)

                # Create contingency table
                combined_categories = list(set(base_dist.index).union(set(current_dist.index)))
                contingency_table = pd.DataFrame({
                    "Base": [base_dist.get(cat, 0) for cat in combined_categories],
                    "Current": [current_dist.get(cat, 0) for cat in combined_categories]
                })

                # Chi-Square test
                chi2_stat, chi2_p_value, _, _ = chi2_contingency(contingency_table.T)

                # Add category-wise statistics
                category_drift = []
                for cat in combined_categories:
                    category_drift.append({
                        "Category": cat,
                        "Base_Freq": base_dist.get(cat, 0),
                        "Current_Freq": current_dist.get(cat, 0),
                    })

                drift_report[base_column] = {
                    "pvalues": float(chi2_p_value),
                    "same_distribution": chi2_p_value > 0.05,
                    "chi2_statistic": float(chi2_stat),
                    "category_drift": category_drift,
                }

        self.validation_error[report_key_name] = drift_report

    except Exception as e:
        raise SrcException(e, sys)
