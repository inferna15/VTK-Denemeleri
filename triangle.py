import vtk

points = vtk.vtkPoints()
points.InsertNextPoint(0.0, 0.0, 0.0)
points.InsertNextPoint(1.0, 0.0, 0.0)
points.InsertNextPoint(0.5, 1.0, 0.0)

triangle = vtk.vtkTriangle()
triangle.GetPointIds().SetId(0, 0)
triangle.GetPointIds().SetId(1, 1)
triangle.GetPointIds().SetId(2, 2)

triangles = vtk.vtkCellArray()
triangles.InsertNextCell(triangle)

trianglePolyData = vtk.vtkPolyData()
trianglePolyData.SetPoints(points)
trianglePolyData.SetPolys(triangles)

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(trianglePolyData)

# Aktör oluşturma
actor = vtk.vtkActor()
actor.SetMapper(mapper)

actor.GetProperty().SetColor(0.0, 1.0, 0.0) # Rengini kırmızı yapma

# Renderleyici oluşturma
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(0.1, 0.2, 0.4)

# Render penceresi oluşturma
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)

# Render penceresi etkileşimi oluşturma
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

# Görselleştirme
renderWindow.Render()
renderWindowInteractor.Start()