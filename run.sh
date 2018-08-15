#!/bin/sh
#
# Last Change: Wed Aug 15, 2018 at 01:57 AM -0400

# NOTE: we could use '--args' flag to pass-thru arguments to boken app.
bokeh serve DVApp --address 0.0.0.0 --port 56789 --allow-websocket-origin=* \
    --args "$@"
