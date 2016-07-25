from setuptools import setup

import tsuru_docker_service


github_url = "https://github.com/juliomfreitas/tsuru-docker-service"

setup(
    name="tsuru-docker-service",
    version=tsuru_docker_service.__version__,
    author=tsuru_docker_service.__author__,
    author_email=tsuru_docker_service.__email__,
    description="Easy to use manager of Tsuru's services (tsuru.io)",
    license="MIT",
    keywords="tsuru_docker_service",
    url=github_url,
    packages=['tsuru_docker_service', 'tests'],
    namespace_packages=['tsuru_docker_service'],
    package_dir={'tsuru_docker_service': 'tsuru_docker_service'},
    download_url="{}/tarball/master".format(github_url),
    tests_require=["nose"],
    test_suite='tests',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Flask",
        "Topic :: Utilities",
        "Environment :: Plugins",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
)
