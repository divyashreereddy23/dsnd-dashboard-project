from pathlib import Path
from setuptools import setup, find_packages

cwd = Path(__file__).resolve().parent
requirements = (cwd / 'employee_events' / 'requirements.txt').read_text().split('\n')

setup_args = dict(
    name='employee_events',
    version='0.0',
    description="SQL Query API: Employee performance analysis package",
    long_description="A Python package for analyzing employee performance events and recruitment risk prediction.",
    packages=find_packages(),
    package_data={'': ['employee_events.db', 'requirements.txt']},
    install_requirements=requirements,
    author="Your Name",
    author_email="your.email@example.com",
    include_package_data=True,
    install_requires=[
        'pandas>=1.3.0',
        'numpy>=1.21.0',
    ],
    python_requires='>=3.7',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    )

if __name__ == "__main__":
    setup(**setup_args)