import vtk

# 1. Volume verisini yükleyin (örneğin, DICOM okuma)
reader = vtk.vtkDICOMImageReader()
reader.SetDirectoryName("C:\\Users\\fatil\\Documents\\Belgeler\\Dicoms\\Snow dcm")  # DICOM dizin yolu
reader.Update()

extent = reader.GetDataExtent()

# 2. ExtractVOI ile bir bölgeyi çıkartın
# VOI: [xmin, xmax, ymin, ymax, zmin, zmax] şeklinde tanımlanır
extractVOI = vtk.vtkExtractVOI()
extractVOI.SetInputConnection(reader.GetOutputPort())
extractVOI.SetVOI(extent[0], extent[1], extent[2], extent[3], extent[4], extent[5])  # Örnek: [xmin, xmax, ymin, ymax, zmin, zmax]
extractVOI.Update()

# 3. Mapper ve aktör oluşturun
volumeMapper = vtk.vtkSmartVolumeMapper()
volumeMapper.SetInputConnection(extractVOI.GetOutputPort())

# 4. Görüntüleme için renk haritası ve opaklık
color = vtk.vtkColorTransferFunction()
color.AddRGBPoint(0, 0.0, 0.0, 0.0)
color.AddRGBPoint(50, 1.0, 0.0, 0.0)
color.AddRGBPoint(100, 0.0, 1.0, 0.0)
color.AddRGBPoint(200, 0.0, 0.0, 1.0)

opacity = vtk.vtkPiecewiseFunction()
opacity.AddPoint(0, 0.0)
opacity.AddPoint(50, 0.1)
opacity.AddPoint(100, 0.3)
opacity.AddPoint(200, 1.0)

transform = vtk.vtkTransform()

# 5. Volume aktörü oluşturun
volume = vtk.vtkVolume()
volume.SetMapper(volumeMapper)
volume.GetProperty().SetColor(color)
volume.GetProperty().SetScalarOpacity(opacity)
volume.SetUserTransform(transform)
volume.SetPosition(-(extent[1] + extent[0]) / 4, -(extent[3] + extent[2]) / 4, -(extent[5] + extent[4]) / 4)

# 6. Renderer ve render window oluşturun
renderer = vtk.vtkRenderer()
renderer.AddVolume(volume)

renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)

renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

value = extent[1]

def func(obj, event):
    global value
    key = obj.GetKeySym()

    print(key)
    if key == "x":
        for value in range(360):
            transform.RotateX(1)
            renderWindow.Render()
    if key == "y":
        for value in range(360):
            transform.RotateY(1)
            renderWindow.Render()

    if key == "z":
        for value in range(360):
            transform.RotateZ(1)
            renderWindow.Render()

    if key == "m":
        for value in range(60):
            transform.RotateY(1)
            renderWindow.Render()

    if key == "Return":
        for value in range(extent[0], extent[1], 5):
            extractVOI.SetVOI(value, extent[1], extent[2], extent[3], extent[4], extent[5])
            extractVOI.Update()
            renderWindow.Render()
        for value in range(extent[1], extent[0], -5):
            extractVOI.SetVOI(value, extent[1], extent[2], extent[3], extent[4], extent[5])
            extractVOI.Update()
            renderWindow.Render()

renderWindowInteractor.AddObserver("KeyPressEvent", func)

# 7. Render işlemini başlatın
renderWindow.Render()
renderWindowInteractor.Start()
