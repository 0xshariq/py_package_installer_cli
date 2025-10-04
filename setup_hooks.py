#!/usr/bin/env python3
"""
Setup hooks for package-installer-cli
"""
import subprocess
import sys
import os
from pathlib import Path

def post_install():
    """Post-installation hook to set up Node.js dependencies"""
    print("\n" + "="*60)
    print("Setting up package-installer-cli...")
    print("="*60)
    
    # Check if Node.js is available
    try:
        result = subprocess.run(["node", "--version"], capture_output=True, text=True)
        if result.returncode != 0:
            print("⚠️  Node.js not found. Please install Node.js from https://nodejs.org/")
            print("   The CLI will attempt to install dependencies on first run.")
            return
    except FileNotFoundError:
        print("⚠️  Node.js not found. Please install Node.js from https://nodejs.org/")
        print("   The CLI will attempt to install dependencies on first run.")
        return
    
    print(f"✅ Node.js found: {result.stdout.strip()}")
    
    # Check if npm is available
    try:
        result = subprocess.run(["npm", "--version"], capture_output=True, text=True)
        if result.returncode != 0:
            print("⚠️  npm not found. Please install npm.")
            return
    except FileNotFoundError:
        print("⚠️  npm not found. Please install npm.")
        return
    
    print(f"✅ npm found: {result.stdout.strip()}")
    print("\n📦 Dependencies will be installed on first use.")
    print("🚀 You can now use: pi --help")
    print("="*60 + "\n")

if __name__ == "__main__":
    post_install()