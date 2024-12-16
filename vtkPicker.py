import vtk

class CustomPicker(vtk.vtkCellPicker):
    def __init__(self):
        super().__init__()

    def Pick(self, selectionPos, renderer):
        super().Pick(selectionPos, renderer)
        if self.GetActor():
            picked_position = self.GetPickPosition()
            print(f"Picked Position: {picked_position[0]}, {picked_position[1]}, {picked_position[2]}")

def main():
    # 3D görselleştirme nesnelerini oluştur
    cube_source = vtk.vtkCubeSource()
    cube_mapper = vtk.vtkPolyDataMapper()
    cube_mapper.SetInputConnection(cube_source.GetOutputPort())
    cube_actor = vtk.vtkActor()
    cube_actor.SetMapper(cube_mapper)

    # Renderer ve RenderWindow
    renderer = vtk.vtkRenderer()
    render_window = vtk.vtkRenderWindow()
    render_window.AddRenderer(renderer)

    # RenderWindowInteractor
    render_window_interactor = vtk.vtkRenderWindowInteractor()
    render_window_interactor.SetRenderWindow(render_window)

    # Picker sınıfını kullanarak seçim işlemi
    picker = CustomPicker()
    render_window_interactor.SetPicker(picker)

    # Küp nesnesini sahneye ekle
    renderer.AddActor(cube_actor)
    renderer.SetBackground(0.1, 0.2, 0.4)  # Arka plan rengini mavi yap

    # Render işlemi başlat
    render_window.Render()
    render_window_interactor.Start()

if __name__ == "__main__":
    main()
