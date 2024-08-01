import vtk

points = vtk.vtkPoints()
points.InsertNextPoint(0.0, 1.0, 0.0)
points.InsertNextPoint(0.0, 0.0, 0.0)
points.InsertNextPoint(1.0, 0.0, 0.0)
points.InsertNextPoint(1.0, 1.0, 0.0)
points.InsertNextPoint(0.0, 1.0, 1.0)
points.InsertNextPoint(0.0, 0.0, 1.0)
points.InsertNextPoint(1.0, 0.0, 1.0)
points.InsertNextPoint(1.0, 1.0, 1.0)

lines = vtk.vtkCellArray()

line = vtk.vtkLine()
line.GetPointIds().SetId(0, 0)
line.GetPointIds().SetId(1, 1)
lines.InsertNextCell(line)

line = vtk.vtkLine()
line.GetPointIds().SetId(0, 1)
line.GetPointIds().SetId(1, 2)
lines.InsertNextCell(line)

line = vtk.vtkLine()
line.GetPointIds().SetId(0, 2)
line.GetPointIds().SetId(1, 3)
lines.InsertNextCell(line)

line = vtk.vtkLine()
line.GetPointIds().SetId(0, 3)
line.GetPointIds().SetId(1, 0)
lines.InsertNextCell(line)

line = vtk.vtkLine()
line.GetPointIds().SetId(0, 0)
line.GetPointIds().SetId(1, 4)
lines.InsertNextCell(line)

line = vtk.vtkLine()
line.GetPointIds().SetId(0, 1)
line.GetPointIds().SetId(1, 5)
lines.InsertNextCell(line)

line = vtk.vtkLine()
line.GetPointIds().SetId(0, 2)
line.GetPointIds().SetId(1, 6)
lines.InsertNextCell(line)

line = vtk.vtkLine()
line.GetPointIds().SetId(0, 3)
line.GetPointIds().SetId(1, 7)
lines.InsertNextCell(line)

line = vtk.vtkLine()
line.GetPointIds().SetId(0, 4)
line.GetPointIds().SetId(1, 5)
lines.InsertNextCell(line)

line = vtk.vtkLine()
line.GetPointIds().SetId(0, 5)
line.GetPointIds().SetId(1, 6)
lines.InsertNextCell(line)

line = vtk.vtkLine()
line.GetPointIds().SetId(0, 6)
line.GetPointIds().SetId(1, 7)
lines.InsertNextCell(line)

line = vtk.vtkLine()
line.GetPointIds().SetId(0, 7)
line.GetPointIds().SetId(1, 4)
lines.InsertNextCell(line)

polyData = vtk.vtkPolyData()
polyData.SetPoints(points)
polyData.SetLines(lines)

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(polyData)

actor = vtk.vtkActor()
actor.SetMapper(mapper)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)

renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)

renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

renderWindow.Render()
renderWindowInteractor.Start()