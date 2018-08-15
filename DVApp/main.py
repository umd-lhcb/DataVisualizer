#!/usr/bin/env python
#
# Last Change: Wed Aug 15, 2018 at 02:07 AM -0400

import yaml
import sys

from argparse import ArgumentParser
from pathlib import Path

# from bokeh.layouts import column
# from bokeh.models import Button
# from bokeh.palettes import RdYlBu3
from bokeh.plotting import curdoc

from elements import get_data_source
from elements import get_stream_plot


#################################
# Parse arguments/configuration #
#################################

def parse_input():
    parser = ArgumentParser(
        description='A data visualization server for burn-in.'
    )

    parser.add_argument(
        '--config-file',
        dest='configFile',
        help='''
        specify configuration file.
        ''',
        type=str,
        default='DVApp.yml'
    )

    return parser.parse_args()


def parse_config(config_file):
    if Path(config_file).exists():
        with open(config_file) as cfg:
            parsed = yaml.load(cfg)
        return parsed

    else:
        print('{}: configuration file does not exist.'.format(config_file))
        sys.exit(1)


#########
# Setup #
#########

args = parse_input()
options = parse_config(args.configFile)
print(options)


##########
# Layout #
##########

source = get_data_source('http://' + options['client']['host'] + ':' +
                         str(options['client']['port']) + '/get/CHANNEL1')
p = get_stream_plot('Stream')
p.circle(source=source, x='time', y='data')
p.x_range.follow = "end"
# p.x_range.follow_interval = 10

curdoc().add_root(p)
