# Ansible Collection - kenmoini.hyperv

## Available Modules

- vhd
- vmswitch
- vmswitch_info

## Examples

### vhd

```yaml
- name: Create Virtual Switch bridged from Ethernet Adapter 1
  kenmoini.hyperv.vmswitch:
    name: VMNetwork
    state: present
    adapterName: Ethernet Adapter 1
    allowManagementOS: true

- name: Delete a Virtual Switch
  kenmoini.hyperv.vmswitch:
    name: VMNetwork
    state: absent

- name: Create an Internally routed Virtual Switch
  kenmoini.hyperv.vmswitch:
    name: natty
    state: present
    switchType: Internal

- name: Create a Private Virtual Switch
  kenmoini.hyperv.vmswitch:
    name: NoNet
    state: present
    switchType: Private
```

### vmswitch

```yaml
- name: Create Virtual Switch bridged from Ethernet Adapter 1
  kenmoini.hyperv.vmswitch:
    name: VMNetwork
    state: present
    adapterName: Ethernet Adapter 1
    allowManagementOS: true

- name: Delete a Virtual Switch
  kenmoini.hyperv.vmswitch:
    name: VMNetwork
    state: absent

- name: Create an Internally routed Virtual Switch
  kenmoini.hyperv.vmswitch:
    name: natty
    state: present
    switchType: Internal

- name: Create a Private Virtual Switch
  kenmoini.hyperv.vmswitch:
    name: NoNet
    state: present
    switchType: Private
```

### vmswitch_info

```yaml
- name: Get the information of a Virtual Switch called VMNetwork
  kenmoini.hyperv.vmswitch_info:
    name: VMNetwork
  register: r_vmswitch_info

- name: Print out the results
  debug:
    msg: "{{ r_vmswitch_info.json | from_json }}"
```