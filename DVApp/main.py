#!/usr/bin/env python
#
# Last Change: Thu Aug 09, 2018 at 05:25 PM -0400


from random import random

from bokeh.layouts import column
# from bokeh.models import Button
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc

from bokeh.models.sources import AjaxDataSource

from bokeh.plotting import figure

###############
# Data source #
###############

def get_data_source(data_url, polling_interval=5000):
    return AjaxDataSource(data_url=data_url, polling_interval=polling_interval)


########
# Plot #
########

source = get_data_source('http://127.0.0.1:45678/get/CHANNEL1')
p = figure(plot_height=300, plot_width=800, background_fill_color="lightgrey",
           title="stream")
p.circle('time', 'data', source=source)
p.x_range.follow = "end"
p.x_range.follow_interval = 10

################
# App settings #
################

curdoc().add_root(p)
