#!/usr/bin/env python
#
# Last Change: Mon Aug 13, 2018 at 11:14 AM -0400

# from bokeh.layouts import column
# from bokeh.models import Button
# from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc

from bokeh.models.sources import AjaxDataSource
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


##########
# Layout #
##########

source = get_data_source('http://127.0.0.1:45678/get/CHANNEL1')
p = get_stream_plot('Stream')
p.circle(source=source, x='time', y='data')
p.x_range.follow = "end"
# p.x_range.follow_interval = 10

################
# App settings #
################

curdoc().add_root(p)
