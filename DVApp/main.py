#!/usr/bin/env python
#
# Last Change: Tue Aug 28, 2018 at 11:58 PM -0400

# from bokeh.palettes import RdYlBu3
from bokeh.plotting import curdoc
from bokeh.models.widgets import Select
from bokeh.models.glyphs import VBar
from bokeh.layouts import widgetbox

from elements import get_url, get_data_source
from elements import get_stream_plot


###############
# Interaction #
###############

def update_single_channel(attr, old, new):
    channel_stream.title.text = new
    url = get_url(**curdoc().server_config, channel=new)
    timeseries_source.data_url = url


#########
# Setup #
#########

# Select box
avaliable_channels = curdoc().channel_list
select = Select(
    title="Select channel:",
    value=avaliable_channels[0], options=avaliable_channels
)
select.on_change('value', update_single_channel)

# Single channel time-series streaming
timeseries_url = get_url(**curdoc().server_config, channel=select.value)
timeseries_source = get_data_source(timeseries_url)
channel_stream = get_stream_plot(
    title=select.value,
    name="channel_stream", sizing_mode="scale_width",
    plot_width=900, plot_height=300
)
channel_stream.circle(source=timeseries_source,
                      x='time', y='data')

# Single channel histogram
hist_url = get_url(**curdoc().server_config, channel=select.value,
                   entry='stats/hist')
hist_source = get_data_source(hist_url, polling_interval=1000*60*5)
channel_hist = get_stream_plot(
    title='hist',
    name="channel_hist", sizing_mode="scale_width",
    plot_width=400, plot_height=300
)
hist_glyph = VBar(x="hist", top="freq")
channel_hist.add_glyph(hist_source, hist_glyph)

# Overall histogram
overall_hist = get_stream_plot(
    title='hist',
    name="overall_hist", sizing_mode="scale_width",
    plot_width=400, plot_height=300
)


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
curdoc().add_root(channel_hist)
curdoc().add_root(overall_hist)
