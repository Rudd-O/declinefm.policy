from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='declinefm.policy',
      version=version,
      description="Decline to State policy package",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Manuel Amador (Rudd-O)',
      author_email='rudd-o@rudd-o.com',
      url='http://declinefm.com/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['declinefm'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
      ],
      extras_require={
          'test': ['plone.app.testing'],
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
