#!/usr/bin/env python
#
# Last Change: Fri Jun 26, 2020 at 03:59 AM +0800

from math import floor

from bokeh.plotting import curdoc
from bokeh.palettes import Viridis256

from elements import get_url, get_data_source
from elements import get_stream_plot


###########
# Helpers #
###########

def pick_colors(num):
    gap = floor(256/num)
    return [Viridis256[i*gap] for i in range(num)]


#########
# Setup #
#########

server_config = curdoc().server_config
psu_channels = curdoc().psu_channel_list
temp_channels = curdoc().temp_channel_list

# PSU streaming plots
psu_plot = get_stream_plot(
    title="MARATON current (click on legend to toggle channel)",
    name="psu_plot", sizing_mode="scale_width",
    plot_width=900, plot_height=600
)

for name, color in zip(psu_channels, pick_colors(len(psu_channels))):
    url = get_url(**server_config, channel=name)
    src = get_data_source(url)
    psu_plot.line(source=src, x='time', y='data',
                  line_width=2, color=color, alpha=0.8,
                  legend_label=name)

psu_plot.legend.location = "top_left"
psu_plot.legend.click_policy = "hide"


##########
# Layout #
##########

app_name = 'UT Burn In @ UMD'
curdoc().title = app_name
curdoc().template_variables['app_name'] = app_name

curdoc().add_root(psu_plot)
