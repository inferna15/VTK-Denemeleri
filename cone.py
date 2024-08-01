import vtk

# Koni oluşturma
cone = vtk.vtkConeSource()
cone.SetHeight(3.0)
cone.SetRadius(1.0)
cone.SetResolution(50)

# Mapper oluşturma
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cone.GetOutputPort())

# Aktör oluşturma
actor = vtk.vtkActor()
actor.SetMapper(mapper)

actor.GetProperty().SetColor(1.0, 0.0, 0.0) # Rengini kırmızı yapma

# Renderleyici oluşturma
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(0.1, 0.2, 0.4)

cube2 = vtk.vtkCubeSource()
cube2.Update()

reader2 = vtk.vtkPNGReader()
reader2.SetFileName("icon.png")
reader2.Update()

texture2 = vtk.vtkTexture()
texture2.SetInputConnection(reader2.GetOutputPort())

mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputConnection(cube2.GetOutputPort())

actor2 = vtk.vtkActor()
actor2.SetMapper(mapper)
actor2.SetTexture(texture2)

renderer2 = vtk.vtkRenderer()
renderer2.AddActor(actor)
renderer2.SetBackground(0.4, 0.2, 0.1)

# Render penceresi oluşturma
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer2)
renderWindow.AddRenderer(renderer)


# Render penceresi etkileşimi oluşturma
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

# Görselleştirme
renderWindow.Render()
renderWindowInteractor.Start()