import json
import subprocess

def submit_job(params):
    # Placeholder for job submission logic
    print(f"Submitting job with params: {params}")
    result = subprocess.run(['sbatch', 'scripts/job_script.sh'], stdout=subprocess.PIPE)
    print(result.stdout.decode())

if __name__ == "__main__":
    with open('../data/job_params.json') as f:
        job_params = json.load(f)
    submit_job(job_params)
