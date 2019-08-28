import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import os
from csv_image_module import get_data_csv, cast_int_list, convert_to_rgb, unpack_array_green, unpack_array
import argparse

plotly.tools.set_credentials_file(username=os.environ['USER_PLOTLY'], api_key=os.environ['KEY_PLOTLY'])

parser = argparse.ArgumentParser(description='Graph the colors present in the image')

parser.add_argument('--csv-path', '--cp', dest='csv_path',
                    required=True, metavar='PATH',
                    help='Path of the csv')

parser.add_argument('--title', '--t', dest='title',
                    required=True, metavar='TITLE',
                    help='Title of graph')

args = parser.parse_args()
csv_path = args.csv_path
title_name = args.title

color_data, q_data = get_data_csv(csv_path)
q_data_int = cast_int_list(q_data)
arr_x, arr_y, arr_z, arr_colors = unpack_array(color_data)
arr_colors_rgb = convert_to_rgb(arr_colors)
print(len(arr_colors_rgb))
print(arr_colors_rgb[2])
print(len(color_data))


# Create trace, sizing bubbles by planet diameter
trace1 = go.Scatter3d(
    x = arr_x,
    y = arr_y,
    z = arr_z,
    text = arr_colors_rgb,
    mode = 'markers',
    marker = dict(
        sizemode = 'diameter',
        sizeref = 700,  # 7000 # info on sizeref: https://plot.ly/python/reference/#scatter-marker-sizeref
        size = q_data_int,
        color = arr_colors_rgb,
        )
)
data=[trace1]

# layout=go.Layout(width=800, height=800, title = 'color_distribution',
layout=go.Layout(width=800, height=800, title = title_name,
              scene = dict(xaxis=dict(title='R',
                                      titlefont=dict(color='Orange')),
                            yaxis=dict(title='G',
                                       titlefont=dict(color='rgb(220, 220, 220)')),
                            zaxis=dict(title='B',
                                       titlefont=dict(color='rgb(220, 220, 220)')),
                            bgcolor = 'rgb(20, 24, 54)'
                           )
             )

fig=go.Figure(data=data, layout=layout)
py.plot(fig, filename=title_name)
