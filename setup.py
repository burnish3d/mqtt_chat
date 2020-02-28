import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
    name="mqtt_chat"
  , install_requires=["paho-mqtt"]
  , version="0.1"
  , author="Zachary Chandler"
  , author_email="chandlerzach@seattleu.edu"
  , description="goofy mqtt chat client"
  , long_description = long_description
  , long_description_content_type="text/markdown"
  , url="https://github.com/pypa/sampleproject"
  , packages=setuptools.find_packages()
  , classifiers=[
        "Programming Language :: Python :: 3"
      , "License :: OSI Approved :: MIT License"]
  , python_requires=">=3.6"
  )