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

faces = vtk.vtkCellArray()

# Ön Yüz
faces.InsertNextCell(4)
faces.InsertCellPoint(0)
faces.InsertCellPoint(1)
faces.InsertCellPoint(2)
faces.InsertCellPoint(3)

# Sol Yüz
faces.InsertNextCell(4)
faces.InsertCellPoint(0)
faces.InsertCellPoint(1)
faces.InsertCellPoint(5)
faces.InsertCellPoint(4)

# Sağ Yüz
faces.InsertNextCell(4)
faces.InsertCellPoint(2)
faces.InsertCellPoint(3)
faces.InsertCellPoint(7)
faces.InsertCellPoint(6)

# Alt Yüz
faces.InsertNextCell(4)
faces.InsertCellPoint(1)
faces.InsertCellPoint(2)
faces.InsertCellPoint(6)
faces.InsertCellPoint(5)

# Üst Yüz
faces.InsertNextCell(4)
faces.InsertCellPoint(0)
faces.InsertCellPoint(3)
faces.InsertCellPoint(7)
faces.InsertCellPoint(4)

# Arka Yüz
faces.InsertNextCell(4)
faces.InsertCellPoint(4)
faces.InsertCellPoint(5)
faces.InsertCellPoint(6)
faces.InsertCellPoint(7)

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