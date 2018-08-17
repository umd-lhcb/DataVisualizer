#!/usr/bin/env python
#
# Last Change: Thu Aug 16, 2018 at 11:49 PM -0400

import yaml
import sys

from argparse import ArgumentParser
from pathlib import Path

# from bokeh.layouts import column
# from bokeh.palettes import RdYlBu3
from bokeh.plotting import curdoc
from bokeh.models.widgets import Select
from bokeh.layouts import widgetbox
from bokeh.layouts import column

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

avaliable_channels = ["test", "two"]
select = Select(title="Select channel:", value="test", options=avaliable_channels)

source = get_data_source(
    'http://' + options['client']['host'] + ':' + str(options['client']['port']) + '/get/CHANNEL1')
p = get_stream_plot('Stream')
p.circle(source=source, x='time', y='data')
p.x_range.follow = "end"


##########
# Layout #
##########

layout = column([widgetbox(select), p], name='layout')

curdoc().add_root(layout)

curdoc().template_variables['stats_names'] = ['users', 'new_users', 'time', 'sessions', 'sales']
curdoc().template_variables['stats'] = {
    'users'     : {'icon': 'user',        'value': 11200, 'change':  4   , 'label': 'Total Users'},
    'new_users' : {'icon': 'user',        'value': 350,   'change':  1.2 , 'label': 'New Users'},
    'time'      : {'icon': 'clock-o',     'value': 5.6,   'change': -2.3 , 'label': 'Total Time'},
    'sessions'  : {'icon': 'user',        'value': 27300, 'change':  0.5 , 'label': 'Total Sessions'},
    'sales'     : {'icon': 'dollar-sign', 'value': 8700,  'change': -0.2 , 'label': 'Average Sales'},
    }
