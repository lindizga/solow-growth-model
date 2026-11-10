Solow Growth Model
Overview
This project uses the Solow Growth Model to investigate how savings rates affect long-run capital accumulation and economic growth.

The model computes the steady-state level of capital per worker and compares outcomes under different savings rates.

Files
solow.py - main Python program
tests/test_solow.py - pytest tests
environment.yml - Mamba environment specification
submit.slurm - SLURM batch script
steady_state.csv - sample output
.github/workflows/tests.yml - GitHub Actions workflow
Creating the Environment
mamba env create -f environment.yml
mamba activate /home/lindizga/mamba-envs/solow-model
Running the Program
python solow.py
This generates:

steady_state.csv
Running Tests
pytest -v
Example output:

2 passed
Running on Great Lakes
Submit the batch job:

sbatch submit.slurm
Monitor jobs:

squeue -u lindizga
View accounting information:

sacct -j JOB_ID
Results
The Solow Growth Model predicts that higher savings rates lead to higher steady-state levels of capital per worker.

The simulation results support this prediction, demonstrating the positive relationship between savings and long-run capital accumulation.

AI and External Assistance
This project used Microsoft Copilot to assist with:

Mamba environment setup
Pytest test development
GitHub Actions configuration
Documentation development
Course lectures and Great Lakes documentation were also used as references.