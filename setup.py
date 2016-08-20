from distutils.core import setup

setup(name='plusminus',
      version='0.1.0',
      description='A graphical interface for manual image classification (plus or minus)',
      url='https://github.com/daurer/plusminus',
      author='Benedikt J. Daurer',
      author_email='benedikt@xray.bmc.uu.se',
      license='MIT license',
      package_dir={'plusminus':'plusminus'},
      package_data={'plusminus':['ui/*.ui', 'icons/*.svg', 'qss/*.qss']},
      packages=['plusminus', 'plusminus.ui'])
