# app.py
import subprocess

def greet(name):
    print(f"Hello, {name}!")

def run_command(cmd):
    subprocess.call(cmd, shell=True)  # Kerentanan Command Injection di sini

if __name__ == "__main__":
    name = input("Enter your name: ")  # Input tidak divalidasi
    greet(name)
    cmd = input("Enter a command to run: ")  # Input tidak divalidasi
    run_command(cmd)  # Potensi untuk injeksi perintah berbahaya
