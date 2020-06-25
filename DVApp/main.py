#!/usr/bin/env python
#
# Last Change: Fri Jun 26, 2020 at 04:20 AM +0800

from math import floor

from bokeh.plotting import curdoc
from bokeh.palettes import Category20b

from elements import get_url, get_data_source
from elements import get_stream_plot


###########
# Helpers #
###########

def pick_colors(num, tot=20, palettes=Category20b[20]):
    gap = floor(tot/num)
    return [palettes[i*gap] for i in range(num)]


#########
# Setup #
#########

server_config = curdoc().server_config
psu_channels = curdoc().psu_channel_list
temp_channels = curdoc().temp_channel_list

# PSU streaming plot
psu_plot = get_stream_plot(
    title="MARATON current (click on legend to toggle channel)",
    name="psu_plot", sizing_mode="stretch_width",
    plot_width=900, plot_height=450
)

for name, color in zip(psu_channels, pick_colors(len(psu_channels))):
    url = get_url(**server_config, channel=name)
    src = get_data_source(url)
    psu_plot.line(source=src, x='time', y='data',
                  line_width=2, color=color, alpha=0.8,
                  legend_label=name)

psu_plot.legend.location = "top_left"
psu_plot.legend.click_policy = "hide"

# Temp streaming plot
temp_plot = get_stream_plot(
    title="Temperature current (click on legend to toggle channel)",
    name="temp_plot", sizing_mode="stretch_width",
    plot_width=900, plot_height=250
)

for name, color in zip(temp_channels, pick_colors(len(temp_channels))):
    url = get_url(**server_config, channel=name)
    src = get_data_source(url)
    temp_plot.line(source=src, x='time', y='data',
                   line_width=2, color=color, alpha=0.8,
                   legend_label=name)

temp_plot.legend.location = "top_left"
temp_plot.legend.click_policy = "hide"


##########
# Layout #
##########

app_name = 'UT Burn In @ UMD'
curdoc().title = app_name
curdoc().template_variables['app_name'] = app_name

curdoc().add_root(psu_plot)
curdoc().add_root(temp_plot)
