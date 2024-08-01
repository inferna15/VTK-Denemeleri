# Dört Yüzlü
import vtk
import math

points = vtk.vtkPoints()
points.InsertNextPoint(0.0, 0.0, 0.0)
points.InsertNextPoint(1.0, 0.0, 0.0)
points.InsertNextPoint(0.5, 0.0, math.sqrt(3) / 2)
points.InsertNextPoint(0.5, math.sqrt(3) / 2, math.sqrt(3) / 2)

faces = vtk.vtkCellArray()

faces.InsertNextCell(3)
faces.InsertCellPoint(0)
faces.InsertCellPoint(1)
faces.InsertCellPoint(3)

faces.InsertNextCell(3)
faces.InsertCellPoint(0)
faces.InsertCellPoint(2)
faces.InsertCellPoint(3)

faces.InsertNextCell(3)
faces.InsertCellPoint(0)
faces.InsertCellPoint(1)
faces.InsertCellPoint(2)

faces.InsertNextCell(3)
faces.InsertCellPoint(1)
faces.InsertCellPoint(2)
faces.InsertCellPoint(3)

polyData = vtk.vtkPolyData()
polyData.SetPoints(points)
polyData.SetPolys(faces)

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