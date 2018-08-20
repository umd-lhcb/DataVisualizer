#!/usr/bin/env python
#
# Last Change: Mon Aug 20, 2018 at 01:38 PM -0400

from bokeh.models.sources import AjaxDataSource
from bokeh.plotting import figure
from bokeh.models.formatters import DatetimeTickFormatter


###############
# Data source #
###############

def get_url(host='localhost', port=45678, channel='CHANNEL1',
            entry='get', **kwargs):
    return 'http://{}:{}/{}/{}'.format(host, port, entry, channel)


def get_data_source(url, polling_interval=1000):
    return AjaxDataSource(data_url=url, polling_interval=polling_interval)


########
# Plot #
########

# COLOR_LHCB_LIGHT_BLUE = '#cae9eb'


def get_stream_plot(**kwargs):
    fig = figure(**kwargs)

    # Set figure styles
    fig.outline_line_width = 2

    FONT_NAME = 'monospace'
    fig.title.text_font = FONT_NAME
    fig.title.text_font_size = "12pt"

    fig.xaxis.major_label_text_font = FONT_NAME
    fig.xaxis.major_label_text_font_size = "10pt"

    fig.yaxis.major_label_text_font = FONT_NAME
    fig.yaxis.major_label_text_font_size = "10pt"

    # fig.border_fill_color = COLOR_LHCB_LIGHT_BLUE

    # Set datetime style
    fig.xaxis.formatter = DatetimeTickFormatter(
        minutes=['%k:%M'],
        minsec=['%k:%M:%S']
    )
    # fig.xaxis.major_label_orientation = 1.5

    # Make sure to follow latest data points
    fig.x_range.follow = "end"

    return fig
