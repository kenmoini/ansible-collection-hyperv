#!/usr/bin/python
# -*- coding: utf-8 -*-

#########################################################################################################################################
# kenmoini.win_hyperv_vmswitch - Create/Delete Virtual Switches from a Windows Server running Hyper-V
#########################################################################################################################################

# this is a windows documentation stub. actual code lives in the .ps1
# file of the same name

DOCUMENTATION = '''
---
module: win_hyperv_vmswitch
version_added: "2.5"
short_description: Adds, deletes and performs configuration of Hyper-V Virtual Switch.
description:
    - Adds, deletes and performs configuration of Hyper-V Virtual Switch.
options:
  name:
    description:
      - Name of Virtual Switch
    required: true
  state:
    description:
      - State of Virtual Switch
    required: false
    choices:
      - present
      - absent
    default: present
  switchType:
    description:
      - Type of Virtual Switch
    required: false
    choices:
      - Internal
      - Private
    default: Internal
  adapterName:
    description:
      - Name of the physical adapter to be used for the Virtual Switch
    required: false
    default: null
  allowManagementOS:
    description:
      - Specifies whether the Virtual Switch can be managed by the Hyper-V Management Service. enabled|disabled
    required: false
    default: disabled
'''

EXAMPLES = '''
  # Create Virtual Switch bridged from Ethernet Adapter 1
  win_hyperv_vmswitch:
    name: VMNetwork
    state: present
    adapterName: Ethernet Adapter 1
    allowManagementOS: true

  # Delete a Virtual Switch
  win_hyperv_vmswitch:
    name: VMNetwork
    state: absent

  # Create an Internally routed Virtual Switch
  win_hyperv_vmswitch:
    name: natty
    state: present
    switchType: Internal

  # Create a Private Virtual Switch
  win_hyperv_vmswitch:
    name: NoNet
    state: present
    switchType: Private
'''

ANSIBLE_METADATA = {
    'status': ['preview'],
    'supported_by': 'community',
    'metadata_version': '1.1'
}
