#!/usr/bin/env python
#
# Last Change: Fri Jun 26, 2020 at 03:43 AM +0800

import sys
import yaml

from argparse import ArgumentParser
from pathlib import Path


#################################
# Parse arguments/configuration #
#################################

def parse_input():
    # Normalize input
    args = sys.argv[sys.argv.index('--args'):]
    parser = ArgumentParser(
        description='A data visualization server for burn-in.'
    )

    parser.add_argument(
        '--args',
        nargs='*',
        help='''
        not used. For bokeh compatibility only.
        '''
    )

    parser.add_argument(
        '--config-file',
        dest='configFile',
        action='append',
        help='''
        specify configuration file. Can be provided repeatedly.
        ''',
        type=str,
        default=list(),
        required=True
    )

    return parser.parse_args(args)


def parse_config(config_file):
    if Path(config_file).exists():
        with open(config_file) as cfg:
            parsed = yaml.safe_load(cfg)
            return parsed

    else:
        print('{}: configuration file does not exist.'.format(config_file))
        sys.exit(1)


################
# Channel list #
################

def get_channel_list(sensors_list):
    psu_channel_list = []
    temp_channel_list = []

    for sensor_spec in sensors_list:
        for name, spec in sensor_spec.items():
            if 'Fire' or 'Water' in name:
                pass
            else:
                if 'psuChannels' in spec.keys():
                    psu_channel_list += [
                        spec['displayName']+str(i) for i in spec['psuChannels']]
                else:
                    temp_channel_list.append(spec['displayName'])

    return psu_channel_list, temp_channel_list


#########
# Hooks #
#########
# NOTE: the logic is the following: on server start, we parse arguments and
# configuration files, and store desired variables to 'server_context'; these
# variables are passed to session when a session is created, and can be accessed
# by 'curdoc().some_variable'.

def on_server_loaded(server_context):
    args = parse_input()

    # NOTE: we assume all configuration files configure server identically, so
    # we'll just use the first one.
    srv_cfg = parse_config(args.configFile[0])
    setattr(server_context, 'server_config', srv_cfg['client'])

    psu_channel_list = []
    temp_channel_list = []

    for f in args.configFile:
        cfg = parse_config(f)
        p_list, t_list = get_channel_list(cfg['sensors'])
        psu_channel_list += p_list
        temp_channel_list += t_list

    setattr(server_context, 'psu_channel_list', psu_channel_list)
    setattr(server_context, 'temp_channel_list', temp_channel_list)


def on_session_created(session_context):
    setattr(session_context._document, 'server_config',
            session_context.server_context.server_config)

    setattr(session_context._document, 'psu_channel_list',
            session_context.server_context.psu_channel_list)
    setattr(session_context._document, 'temp_channel_list',
            session_context.server_context.temp_channel_list)
