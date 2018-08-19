#!/usr/bin/env python
#
# Last Change: Sun Aug 19, 2018 at 06:26 PM -0400

import yaml
import sys

from argparse import ArgumentParser
from pathlib import Path

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
select = Select(
    title="Select channel:",
    value="test", options=avaliable_channels
)

source = get_data_source(channel='RAND_UNIFORM_I', **options['client'])
channel_stream = get_stream_plot(
    title='Stream',
    name="channel_stream", sizing_mode="scale_width",
    plot_width=900, plot_height=300
)
channel_stream.circle(source=source, x='time', y='data')


##########
# Layout #
##########

app_name = 'UT Burn In @ UMD'
curdoc().title = app_name
curdoc().template_variables['app_name'] = app_name

select_layout = widgetbox(select,
                          name='select', sizing_mode='scale_width')
curdoc().add_root(select_layout)

curdoc().add_root(channel_stream)
