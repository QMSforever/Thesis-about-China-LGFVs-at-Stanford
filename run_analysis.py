import subprocess
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def run_script(script_path):
    """Run a Python script and handle any errors."""
    try:
        logger.info(f"Running {script_path}...")
        subprocess.run(['python', script_path], check=True)
        logger.info(f"Successfully completed {script_path}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error running {script_path}: {str(e)}")
        raise

def main():
    """Run the complete analysis pipeline."""
    try:
        # Create necessary directories
        Path("data/raw").mkdir(parents=True, exist_ok=True)
        Path("data/processed").mkdir(parents=True, exist_ok=True)
        Path("results/tables").mkdir(parents=True, exist_ok=True)
        Path("results/figures").mkdir(parents=True, exist_ok=True)
        
        # Run data processing
        run_script("code/data_cleaning/01_data_processing.py")
        
        # Run main analysis
        run_script("code/analysis/01_main_analysis.py")
        
        # Run visualization
        run_script("code/visualization/01_visualization.py")
        
        logger.info("Analysis pipeline completed successfully!")
        
    except Exception as e:
        logger.error(f"Error in analysis pipeline: {str(e)}")
        raise

if __name__ == "__main__":
    main() 