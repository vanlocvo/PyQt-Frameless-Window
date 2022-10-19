import setuptools


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="PyQt5-Frameless-Window",
    version="0.1.1",
    keywords="pyqt frameless",
    author="Huang Zhengzhi",
    author_email="1319158137@qq.com",
    description="A cross-platform frameless window based on pyqt5, support Win32, X11, Wayland and macOS.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/zhiyiYo/PyQt-Frameless-Window",
    packages=setuptools.find_packages(),
    install_requires=[
        "pywin32;platform_system=='Windows'",
        "xcffib;platform_system=='Linux'",
        "pyobjc;platform_system=='Darwin'",
        "PyCocoa;platform_system=='Darwin'",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)
