from setuptools import setup

setup(
    name="electrum-msc-server",
    version="0.9",
    scripts=['run_electrum_msc_server','electrum-msc-server'],
    install_requires=['plyvel','jsonrpclib', 'irc'],
    package_dir={
        'electrummscserver':'src'
        },
    py_modules=[
        'electrummscserver.__init__',
        'electrummscserver.utils',
        'electrummscserver.storage',
        'electrummscserver.deserialize',
        'electrummscserver.networks',
        'electrummscserver.blockchain_processor',
        'electrummscserver.server_processor',
        'electrummscserver.processor',
        'electrummscserver.version',
        'electrummscserver.ircthread',
        'electrummscserver.stratum_tcp',
        'electrummscserver.stratum_http'
    ],
    description="Mastercoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/testalt/electrum-server/",
    long_description="""Server for the Electrum Lightweight Mastercoin Wallet"""
)


