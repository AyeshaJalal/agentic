import os
import sys

from streamlit.web import cli


def app():
    sys.argv = ["streamlit", "run", "src/agentic/main.py"]
    cli.main()

