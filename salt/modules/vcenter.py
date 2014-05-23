# -*- coding: utf-8 -*-
'''
Module for managing VMWare vCenter instances.

:depends:   - pyvmomi python module
:configuration: This module can be used by specifying the name of a
    configuration profile in the minion config, minion pillar,
    or master config.

    For example:

    .. code-blcok:: yaml

        my-vcenter-name:
            vcenter.address: 1.2.3.4
            vcenter.port: 443
            vcenter.username: myusername
            vcenter.password: mypassword

    Available actions:

    create_datacenter
    create_cluster
    join_host
    set_host_dns
    set_host_ntp
'''

HAS_LIBS = False
try:
    from pyVim.connect import SmartConnect
    HAS_LIBS = True
except ImportError:
    pass

__virtualname__ = 'vcenter'


def __virtual__():
    '''
    Only load this module if pyvmomi is installed on this minion.
    '''
    if HAS_LIBS:
        return __virtualname__
    return False


def _get_connection(instance):
    '''
    Return a vcenter connection.
    '''
    creds = __salt__['config.option'](instance)

    connection = SmartConnect(
        host=creds.get('vcenter.address'),
        user=creds.get('vcenter.username'),
        pwd=creds.get('vcenter.password'),
        port=creds.get('vcenter.port')
    )

    return connection

def create_datacenter(datacenter_name, instance=None):
    '''
    Create a datacenter inside of vmware vcenter.

    CLI Example:

        vcenter.create_datacenter <datacenter_name> instance=my-vcenter-name

    The following parameters are required:

    datacenter_name
        Name of the datacenter to be created.

    instance
        This refers to the configuration instance to use to connect to vcenter.
    '''

def create_cluster(cluster_name, instance=None):
    '''
    Create a cluster inside of vmware vcenter. By default the cluster will
    be created with the default HA and DRS settings enabled.

    CLI Example:

        vcenter.create_cluster <cluster_name> instance=my-vcenter-name

    The following parameters are required:

    cluster_name
        Name of the cluster to be created.

    instance
        This refers to the configuration instance to use to connect to vcenter.
    '''

def join_host(cluster_name, esx_address, esx_username, esx_password, instance):
    '''
    Join the given ESX host to the given cluster.

    CLI Example:

        vcenter.join_host <cluster_name> <esx_address> <esx_username> \
            <esx_password> instance=my-vcenter-name

    The following parameters are required:

    cluster_name
        Name of the cluster to join the host to.

    esx_address
        IP or hostname of the ESX host.

    esx_username
        A valid ESX username with permissions to change state.

    esx_password
        A valid ESX password for the given esx_username.

    instance
        This refers to the configuration instance to use to connect to vcenter.
    '''

def set_host_dns():
    '''
    Set DNS options for a given ESX host.
    '''

def set_host_ntp():
    '''
    Set NTP options for a given ESX host.
    '''