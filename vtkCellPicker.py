import vtk

class CustomPicker(vtk.vtkCellPicker):
    def __init__(self):
        super().__init__()

    def Pick(self, selectionPos, renderer):
        super().Pick(selectionPos, renderer)
        
        # Eğer tıklanan bir nesne varsa
        if self.GetActor():
            picked_position = self.GetPickPosition()
            print(f"Picked Position: {picked_position[0]}, {picked_position[1]}, {picked_position[2]}")

            # Seçilen nesnenin türünü al
            actor = self.GetActor()
            print(f"Selected Actor: {actor.GetClassName()}")

            # Seçilen nesnenin rengini al
            property = actor.GetProperty()
            color = property.GetColor()
            print(f"Actor Color: R={color[0]} G={color[1]} B={color[2]}")

def main():
    # 3D görselleştirme nesnelerini oluştur
    cube_source = vtk.vtkCubeSource()
    cube_mapper = vtk.vtkPolyDataMapper()
    cube_mapper.SetInputConnection(cube_source.GetOutputPort())
    cube_actor = vtk.vtkActor()
    cube_actor.SetMapper(cube_mapper)

    # Küp rengini ayarla
    cube_actor.GetProperty().SetColor(1.0, 0.0, 0.0)  # Kırmızı renk

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
    
    # Fare tıklamalarını dinlemek için interactor'ı başlat
    render_window_interactor.Start()

if __name__ == "__main__":
    main()
