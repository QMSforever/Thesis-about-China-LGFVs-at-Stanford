import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import logging
from scipy import stats

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Define paths
DATA_DIR = Path("../../data")
PROCESSED_DATA_DIR = DATA_DIR / "processed"
RESULTS_DIR = Path("../../results")
FIGURES_DIR = RESULTS_DIR / "figures"

def plot_parallel_trends(df, outcome_var):
    """Plot parallel trends for a given outcome variable."""
    logger.info(f"Creating parallel trends plot for {outcome_var}...")
    
    # Create figure
    plt.figure(figsize=(10, 6))
    
    # Plot trends for each group
    for group in ['high_sensitivity', 'low_sensitivity']:
        group_data = df[df[group] == 1]
        plt.plot(group_data.groupby('year')[outcome_var].mean(), 
                label=f"{'High' if group == 'high_sensitivity' else 'Low'} Sensitivity")
    
    plt.axvline(x=2014, color='r', linestyle='--', label='Policy Change')
    plt.title(f'Parallel Trends: {outcome_var}')
    plt.xlabel('Year')
    plt.ylabel(outcome_var)
    plt.legend()
    
    # Save plot
    plt.savefig(FIGURES_DIR / f"parallel_trends_{outcome_var}.png")
    plt.close()

def plot_event_study(df, outcome_var):
    """Plot event study results."""
    logger.info(f"Creating event study plot for {outcome_var}...")
    # TODO: Implement event study plotting
    pass

def plot_heterogeneity(df, outcome_var):
    """Plot heterogeneity analysis results."""
    logger.info(f"Creating heterogeneity plot for {outcome_var}...")
    
    # Create figure
    plt.figure(figsize=(12, 6))
    
    # Plot by region
    plt.subplot(1, 2, 1)
    sns.boxplot(x='is_coastal', y=outcome_var, data=df)
    plt.title(f'{outcome_var} by Region')
    
    # Plot by sensitivity
    plt.subplot(1, 2, 2)
    sns.boxplot(x='high_sensitivity', y=outcome_var, data=df)
    plt.title(f'{outcome_var} by Sensitivity')
    
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / f"heterogeneity_{outcome_var}.png")
    plt.close()

def plot_robustness_checks(df, outcome_var):
    """Plot robustness check results."""
    logger.info(f"Creating robustness check plots for {outcome_var}...")
    # TODO: Implement robustness check plotting
    pass

def create_summary_tables(df):
    """Create summary statistics tables."""
    logger.info("Creating summary statistics tables...")
    
    # Create summary statistics
    summary_stats = df.describe()
    
    # Save to CSV
    summary_stats.to_csv(RESULTS_DIR / "tables" / "summary_statistics.csv")
    
    # Create correlation matrix
    corr_matrix = df.corr()
    corr_matrix.to_csv(RESULTS_DIR / "tables" / "correlation_matrix.csv")

def main():
    """Main visualization pipeline."""
    try:
        # Create figures directory if it doesn't exist
        FIGURES_DIR.mkdir(parents=True, exist_ok=True)
        
        # Load data
        df = pd.read_parquet(PROCESSED_DATA_DIR / "analysis_sample.parquet")
        
        # Define outcome variables
        outcomes = [
            'bond_issuance_volume',
            'yield_spread',
            'credit_rating',
            'roa',
            'total_assets'
        ]
        
        # Create summary tables
        create_summary_tables(df)
        
        # Create plots for each outcome
        for outcome in outcomes:
            # Parallel trends
            plot_parallel_trends(df, outcome)
            
            # Event study
            plot_event_study(df, outcome)
            
            # Heterogeneity
            plot_heterogeneity(df, outcome)
            
            # Robustness checks
            plot_robustness_checks(df, outcome)
        
        logger.info("Visualization completed successfully!")
        
    except Exception as e:
        logger.error(f"Error in visualization: {str(e)}")
        raise

if __name__ == "__main__":
    main() 