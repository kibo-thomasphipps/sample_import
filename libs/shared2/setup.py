from setuptools import setup, find_packages


setup(
  
    name="shared2",
    version="0.1.0",
    description="A sample Python package",
    author="Your Name",       
    package_dir={"": "src"},  # tell setuptools that packages are under 'src'
    packages=find_packages(where="src"),  # find packages under 'src'
    install_requires=[]
    
   
)