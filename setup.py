from setuptools import setup, find_packages

version = '2.1.dev0'

setup(name='uvc.menus',
      version=version,
      description="",
      long_description="""\
""",
      # Get strings from http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[],
      keywords="",
      author="",
      author_email="",
      url="",
      license="",
      package_dir={'': 'src'},
      packages=find_packages('src'),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'grok',
          'grokcore.component',
          'grokcore.security',
          'martian',
          'zope.browserpage',
          'zope.security',
      ])
