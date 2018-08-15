#!/usr/bin/env python
#
# Last Change: Wed Aug 15, 2018 at 01:46 AM -0400

from bokeh.models.sources import AjaxDataSource
from bokeh.plotting import figure
from bokeh.models.formatters import DatetimeTickFormatter


###############
# Data source #
###############

def get_data_source(data_url, polling_interval=100):
    return AjaxDataSource(data_url=data_url, polling_interval=polling_interval)


########
# Plot #
########

def get_stream_plot(title, plot_height=300, plot_width=800):
    fig = figure(
        plot_height=plot_height, plot_width=plot_width,
        title=title, x_axis_type='datetime'
    )

    # Set figure styles
    fig.outline_line_width = 2

    # Set datetime style
    fig.xaxis.formatter = DatetimeTickFormatter(
        minutes=['%k:%M'],
        minsec=['%k:%M:%S']
    )
    # fig.xaxis.major_label_orientation = 1.5

    return fig
