#!/usr/bin/env python3
import sys
import os

# Add main directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bugs.cli import main

if __name__ == '__main__':
    main()
