import vtk

fileName = "C:/Users/fatil/OneDrive/Masaüstü/python-vtk/icon.png"

reader = vtk.vtkPNGReader()
reader.SetFileName(fileName)
reader.Update()

imageActor = vtk.vtkImageActor()
imageActor.SetInputData(reader.GetOutput())

renderer = vtk.vtkRenderer()
renderer.AddActor(imageActor)
renderer.SetBackground(0.1, 0.2, 0.4)

renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)

renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

renderWindow.Render()
renderWindowInteractor.Start()