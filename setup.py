from setuptools import find_packages, setup

setup(
    name='tkd_gym',
    version='1.0.0',
    packages=find_packages(),  # 自动寻找所包含的文件夹
    include_package_data=True,  # 包含其他文件夹，如静态文件和模板文件所在的文件夹
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
