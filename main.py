import subprocess
import os

def run_backend():
    backend_path = os.path.join(os.path.dirname(__file__), "kanban_backend")
    subprocess.Popen(["python", "manage.py", "runserver"], cwd=backend_path)

def run_frontend():
    frontend_path = os.path.join(os.path.dirname(__file__), "frontend", "kanban_desk")
    subprocess.Popen(["npm.cmd", "start"], cwd=frontend_path)

if __name__ == "__main__":
    print("=== KANBAN SYSTEM LAUNCH ===")
    run_backend()
    run_frontend()
