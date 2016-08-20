from distutils.core import setup

setup(name='plusminus',
      version='0.1.0',
      description='',
      url='',
      author='Benedikt J. Daurer',
      author_email='benedikt@xray.bmc.uu.se',
      license='',
      package_dir={'plusminus':'plusminus'},
      package_data={'plusminus':['ui/*.ui', 'icons/*.svg', 'qss/*.qss']},
      packages=['plusminus', 'plusminus.ui'])
      
