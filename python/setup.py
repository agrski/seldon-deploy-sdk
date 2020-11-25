# coding: utf-8

"""
    Seldon-Deploy API.

    Documentation of Seldon-Deploy API.  # noqa: E501

    OpenAPI spec version: v1alpha1
    Contact: hello@seldon.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "seldon-deploy-sdk"
VERSION = "0.2.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23",
    "Authlib<=0.16.0",
]
    

setup(
    name=NAME,
    version=VERSION,
    description="Seldon-Deploy API.",
    author_email="hello@seldon.io",
    url="https://deploy.seldon.io",
    keywords=["Swagger", "Seldon-Deploy API."],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Documentation of Seldon-Deploy API.  # noqa: E501
    """
)
