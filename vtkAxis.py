#!/usr/bin/env python3

import math

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingContextOpenGL2
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkChartsCore import (
    vtkAxis,
    vtkChart,
    vtkChartXY
)
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonCore import (
    vtkCharArray,
    vtkFloatArray
)
from vtkmodules.vtkCommonDataModel import vtkTable
from vtkmodules.vtkViewsContext2D import vtkContextView


def main():
    colors = vtkNamedColors()

    # Set up a 2D scene, add an XY chart to it.
    view = vtkContextView()
    view.GetRenderWindow().size = (640, 480)
    view.GetRenderWindow().window_name = 'AreaPlot'

    chart = vtkChartXY(title='Area Plot')
    chart.title_properties.font_size = 36
    chart.title_properties.color = colors.GetColor3d('Banana')

    chart.GetAxis(0).title_properties.font_size = 24
    chart.GetAxis(0).title_properties.color = colors.GetColor3d('orange')
    chart.GetAxis(0).label_properties.color = colors.GetColor3d('beige')
    chart.GetAxis(0).label_properties.font_size = 18

    chart.GetAxis(1).title_properties.font_size = 24
    chart.GetAxis(1).title_properties.color = colors.GetColor3d('orange')
    chart.GetAxis(1).label_properties.color = colors.GetColor3d('beige')
    chart.GetAxis(1).label_properties.font_size = 18

    view.scene.AddItem(chart)

    # Create a table with some points in it...
    table = vtkTable()

    arr_x = vtkFloatArray(name='X Axis')
    table.AddColumn(arr_x)

    arr_c = vtkFloatArray(name='Cosine')
    table.AddColumn(arr_c)

    arr_s = vtkFloatArray(name='Sine')
    table.AddColumn(arr_s)

    arr_s2 = vtkFloatArray(name='Sine2')
    table.AddColumn(arr_s2)

    arr_s3 = vtkFloatArray(name='Sine3')
    table.AddColumn(arr_s3)

    arr1 = vtkFloatArray(name='One')
    table.AddColumn(arr1)

    valid_mask = vtkCharArray(name='ValidMask')
    table.AddColumn(valid_mask)

    # Test charting with a few more points...
    num_points = 69
    inc = 7.5 / (num_points - 1)
    table.number_of_rows = num_points
    for i in range(0, num_points):
        table.SetValue(i, 0, i * inc + 0.01)
        table.SetValue(i, 1, math.cos(i * inc) + 0.01)
        table.SetValue(i, 2, math.sin(i * inc) + 0.01)
        table.SetValue(i, 3, math.sin(i * inc) + 0.5)
        table.SetValue(i, 4, math.sin(i * inc) * math.sin(i * inc) + 0.01)
        table.SetValue(i, 5, 1.0)

        val = chr(0) if 30 < i < 40 else chr(1)
        valid_mask.SetValue(i, val)

    # Add multiple line plots, setting the colors etc.
    color3d = colors.GetColor3d('tomato')
    area = chart.AddPlot(vtkChart.AREA)
    area.SetInputData(table)
    area.SetInputArray(0, 'X Axis')
    area.SetInputArray(1, 'Sine')
    area.SetInputArray(2, 'Sine2')
    area.SetValidPointMaskName('ValidMask')
    area.brush.color_f = (color3d.red, color3d.green,color3d.blue, 0.6)

    chart.GetAxis(vtkAxis.LEFT).SetLogScale(True)

    # Render the scene.
    view.GetRenderer().background = colors.GetColor3d('SlateGray')
    view.GetRenderWindow().multi_samples = 0
    view.GetRenderWindow().Render()
    view.GetInteractor().Initialize()
    view.GetInteractor().Start()


if __name__ == '__main__':
    main()