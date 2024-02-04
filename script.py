# script.py
import subprocess
import time
import webbrowser

def main():
    with open("/list.txt") as file:
        urls = file.read().splitlines()

    while True:
        for url in urls:
            subprocess.run(["docker", "stop", "web-container"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            subprocess.run(["docker", "rm", "web-container"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            subprocess.run(["docker", "run", "--name", "web-container", "-d", "-p", "80:80", "-e", "URL=" + url, "android-docker-image"])

            time.sleep(5)
            webbrowser.open(url)

if __name__ == "__main__":
    main()
