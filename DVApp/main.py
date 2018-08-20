#!/usr/bin/env python
#
# Last Change: Mon Aug 20, 2018 at 12:18 AM -0400

# from bokeh.palettes import RdYlBu3
from bokeh.plotting import curdoc
from bokeh.models.widgets import Select
from bokeh.layouts import widgetbox

from elements import get_data_source
from elements import get_stream_plot

#########
# Setup #
#########

avaliable_channels = curdoc().channel_list
select = Select(
    title="Select channel:",
    value=avaliable_channels[0], options=avaliable_channels
)

server_config = curdoc().server_config
source = get_data_source(channel='RAND_UNIFORM_I1', **server_config)

channel_stream = get_stream_plot(
    title='Stream',
    name="channel_stream", sizing_mode="scale_width",
    plot_width=900, plot_height=300
)
channel_stream.circle(source=source, x='time', y='data')

channel_hist = get_stream_plot(
    title='hist',
    name="channel_hist", sizing_mode="scale_width",
    plot_width=400, plot_height=300
)
# channel_hist_data, channel_hist_edges = np.histogram(source.data['data'])
# channel_hist.vbar(x='data', source=source)

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
