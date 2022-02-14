import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

requirements = ["paho-mqtt"]
version="0.1.2"
setuptools.setup(
    name="mqtt_chat"
  , install_requires=requirements
  , version=version
  , author="Zachary Chandler"
  , author_email="zachary.c.me@gmail.com"
  , description="light weight mqtt chat client"
  , license = "MIT"
  , long_description = long_description
  , long_description_content_type="text/markdown"
  , url="https://github.com/burnish3d/mqtt_chat"
  , package_dir={'': 'src'}
  , packages=["mqtt_chat"]
  , classifiers=[
        "Programming Language :: Python :: 3"
      , "License :: OSI Approved :: MIT License"]
  , python_requires=">=3.6"
  )