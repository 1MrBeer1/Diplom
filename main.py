import subprocess
import threading
import os
import time
import sys

BACKEND_DIR = os.path.join(os.getcwd(), "kanban_backend")
FRONTEND_DIR = os.path.join(os.getcwd(), "kanban_frontend")
DOCKER_FILE = os.path.join(os.getcwd(), "docker-compose.yml")
VENV_PYTHON = os.path.join(os.getcwd(), ".venv", "Scripts", "python.exe")


def run_docker_db():
    print("🐘 Запуск PostgreSQL через Docker...")
    os.chdir(os.path.dirname(DOCKER_FILE))
    subprocess.run(["docker", "compose", "up", "-d"], check=True)



def run_backend():
    os.chdir(BACKEND_DIR)
    subprocess.run([VENV_PYTHON, "manage.py", "runserver", "127.0.0.1:8000"], check=True)

def run_frontend():
    os.chdir(FRONTEND_DIR)
    subprocess.run(["npm.cmd", "start"], check=True)



def main():
    print("=== KANBAN SYSTEM LAUNCH ===")

    # 1. Docker
    run_docker_db()
    time.sleep(2)

    # 2. Backend и Frontend
    backend_thread = threading.Thread(target=run_backend)
    frontend_thread = threading.Thread(target=run_frontend)

    backend_thread.start()
    time.sleep(5)  # ждём поднятия Django
    frontend_thread.start()

    backend_thread.join()
    frontend_thread.join()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Остановка проекта...")
        subprocess.run(["docker", "compose", "down"])
        sys.exit(0)
