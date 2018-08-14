#!/bin/sh
#
# Last Change: Tue Aug 14, 2018 at 04:21 PM -0400

# NOTE: we could use '--arg' flag to pass-thru arguments to boken app.

bokeh serve DVApp --address 0.0.0.0 --port 56789 --allow-websocket-origin=*
