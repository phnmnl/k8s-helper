from distutils.core import setup

setup(
    name='k8s-helper',
    version='0.1.0',
    packages=['k8s'],
    url='https://github.com/phnmnl/k8s-helper',
    license='Apache 2.0',
    author='Pablo Moreno, Pierrick Roger Mele',
    author_email='phenomenal-h2020-users@googlegroups.com',
    description='CLI to send and wait for jobs to a Kubernetes cluster, '
                'requires a working kubectl (can connect to the desired K8s '
                'cluster) on the machine running this code.'
)