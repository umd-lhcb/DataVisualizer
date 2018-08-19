#!/usr/bin/env python
#
# Last Change: Sun Aug 19, 2018 at 02:54 AM -0400

import yaml
import sys

from argparse import ArgumentParser
from pathlib import Path

# from bokeh.layouts import column
# from bokeh.palettes import RdYlBu3
from bokeh.plotting import curdoc
from bokeh.models.widgets import Select
from bokeh.layouts import widgetbox

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
channel_detail_title = 'Recent data from channel: '
select = Select(title=channel_detail_title, value="test", options=avaliable_channels)

source = get_data_source(
    'http://' + options['client']['host'] + ':' + str(options['client']['port']) + '/get/CHANNEL1')
p = get_stream_plot('Stream')
p.circle(source=source, x='time', y='data')
p.x_range.follow = "end"


##########
# Layout #
##########

app_name = 'UT Burn In @ UMD'
curdoc().title = app_name
curdoc().template_variables['app_name'] = app_name

select_layout = widgetbox(select, name='select')

curdoc().add_root(select_layout)
