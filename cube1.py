import vtk

cube = vtk.vtkCubeSource()
cube.Update()

reader = vtk.vtkPNGReader()
reader.SetFileName("icon.png")
reader.Update()

texture = vtk.vtkTexture()
texture.SetInputConnection(reader.GetOutputPort())

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cube.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.SetTexture(texture)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(0.1, 0.2, 0.4)

rendererWindow = vtk.vtkRenderWindow()
rendererWindow.AddRenderer(renderer)

renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(rendererWindow)

# Event ekleme kısmı
'''

def onLeftClick(obj, event):
    actor.GetProperty().SetColor(1.0, 0.0, 0.0)
    rendererWindow.Render()

def onRightClick(obj, event):
    actor.GetProperty().SetColor(0.0, 1.0, 1.0)
    rendererWindow.Render()

renderWindowInteractor.AddObserver("LeftButtonPressEvent", onLeftClick)
renderWindowInteractor.AddObserver("RightButtonPressEvent", onRightClick)

'''

rendererWindow.Render()
renderWindowInteractor.Start()


    