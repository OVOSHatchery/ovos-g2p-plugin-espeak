#!/usr/bin/env python3
from setuptools import setup


PLUGIN_ENTRY_POINT = 'ovos-g2p-espeak-plugin=ovos_g2p_espeak_plugin:EspeakPhonemesPlugin'
CONFIG_ENTRY_POINT = 'ovos-g2p-espeak-plugin.config=ovos_g2p_espeak_plugin:EspeakG2PConfig'
setup(
    name='ovos-g2p-espeak-plugin',
    version='0.0.1',
    description='A utterance2phoneme plugin ovos',
    url='https://github.com/OpenVoiceOS/ovos-g2p-espeak-plugin',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='GPL',
    packages=['ovos_g2p_espeak_plugin'],
    zip_safe=True,
    keywords='ovos plugin utterance phoneme',
    entry_points={'ovos.plugin.g2p': PLUGIN_ENTRY_POINT,
                  'ovos.plugin.g2p.config': CONFIG_ENTRY_POINT}
)
