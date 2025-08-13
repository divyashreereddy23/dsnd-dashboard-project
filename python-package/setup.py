from pathlib import Path
from setuptools import setup, find_packages

cwd = Path(__file__).resolve().parent
requirements = (cwd / 'employee_events' / 'requirements.txt').read_text().split('\n')

setup_args = dict(
    name='employee_events',
    version='0.0',
    description='SQL Query API',
    packages=find_packages(),
    package_data={'': ['employee_events.db', 'requirements.txt']},
    install_requirements=requirements,
    )

if __name__ == "__main__":
    setup(**setup_args)

from setuptools import setup, find_packages

setup(
    name="employee_events",
    version="1.0.0",
    description="A Python package for analyzing employee performance events",
    long_description="This package provides tools for querying and analyzing employee performance data from a SQLite database. Perfect for HR and management dashboards!",
    author="Data Science Team",
    author_email="datascience@company.com",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'employee_events': ['*.db'],  # Include the database file
    },
    install_requires=[
        'sqlite3',  # This is built into Python, but good to list
    ],
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
