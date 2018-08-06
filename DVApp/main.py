#!/usr/bin/env python
#
# Last Change: Mon Aug 06, 2018 at 02:06 PM -0400


from random import random

from bokeh.layouts import column
from bokeh.models import Button
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc


# # create a plot and style its properties
# p = figure(x_range=(0, 100), y_range=(0, 100), toolbar_location=None)
# p.border_fill_color = 'black'
# p.background_fill_color = 'black'
# p.outline_line_color = None
# p.grid.grid_line_color = None

# # add a text renderer to our plot (no data yet)
# r = p.text(x=[], y=[], text=[], text_color=[], text_font_size="20pt",
           # text_baseline="middle", text_align="center")

# i = 0

# ds = r.data_source


# # create a callback that will add a number in a random location
# def callback():
    # global i

    # # BEST PRACTICE --- update .data in one step with a new dict
    # new_data = dict()
    # new_data['x'] = ds.data['x'] + [random()*70 + 15]
    # new_data['y'] = ds.data['y'] + [random()*70 + 15]
    # new_data['text_color'] = ds.data['text_color'] + [RdYlBu3[i % 3]]
    # new_data['text'] = ds.data['text'] + [str(i)]
    # ds.data = new_data

    # i = i + 1


# # add a button widget and configure with the call back
# button = Button(label="Press Me")
# button.on_click(callback)

# # put the button and plot in a layout and add to the document
# curdoc().add_root(column(button, p))

from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

data = {'x_values': [1, 2, 3, 4, 5],
        'y_values': [6, 7, 2, 3, 6]}

source = ColumnDataSource(data=data)

p = figure()
p.circle(x='x_values', y='y_values', source=source)

# Add elements to the app layout
curdoc().add_root(p)
