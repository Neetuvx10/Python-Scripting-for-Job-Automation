import subprocess

def check_job_status(job_id):
    result = subprocess.run(['squeue', '--job', job_id], stdout=subprocess.PIPE)
    print(result.stdout.decode())

if __name__ == "__main__":
    job_id = input("Enter job ID: ")
    check_job_status(job_id)
