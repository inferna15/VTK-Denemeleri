#include <vtkSmartPointer.h>
#include <vtkRenderer.h>
#include <vtkRenderWindow.h>
#include <vtkRenderWindowInteractor.h>
#include <vtkCubeSource.h>
#include <vtkPolyDataMapper.h>
#include <vtkActor.h>
#include <vtkCellPicker.h>
#include <vtkProperty.h>
#include <vtkInteractorStyleTrackballCamera.h>
#include <vtkNamedColors.h>
#include <iostream>

// CustomPicker sınıfı
class CustomPicker : public vtkCellPicker
{
public:
    static CustomPicker* New();
    vtkTypeMacro(CustomPicker, vtkCellPicker);

    CustomPicker() {}

    // 'Pick' fonksiyonunu doğru şekilde geçersiz kılmak
    bool Pick(double selectionPos[3], vtkRenderer* ren) override
    {
        // Önceki pick işlemini çağırıyoruz
        bool picked = vtkCellPicker::Pick(selectionPos, ren);

        if (picked && this->GetActor())
        {
            // Tıklanan pozisyonu al
            double* pickedPosition = this->GetPickPosition();
            std::cout << "Picked Position: " 
                      << pickedPosition[0] << ", "
                      << pickedPosition[1] << ", "
                      << pickedPosition[2] << std::endl;

            // Tıklanan aktörü al ve türünü yazdır
            vtkActor* actor = this->GetActor();
            std::cout << "Selected Actor: " << actor->GetClassName() << std::endl;

            // Rengi al
            vtkProperty* property = actor->GetProperty();
            double* color = property->GetColor();
            std::cout << "Actor Color: R=" << color[0] << " G=" << color[1] << " B=" << color[2] << std::endl;
        }

        return picked;
    }
};

vtkStandardNewMacro(CustomPicker);

int main()
{
    // Küp kaynağını oluştur
    vtkSmartPointer<vtkCubeSource> cubeSource = vtkSmartPointer<vtkCubeSource>::New();
    vtkSmartPointer<vtkPolyDataMapper> cubeMapper = vtkSmartPointer<vtkPolyDataMapper>::New();
    cubeMapper->SetInputConnection(cubeSource->GetOutputPort());
    vtkSmartPointer<vtkActor> cubeActor = vtkSmartPointer<vtkActor>::New();
    cubeActor->SetMapper(cubeMapper);

    // Küp aktörüne renk ekle
    cubeActor->GetProperty()->SetColor(1.0, 0.0, 0.0); // Kırmızı

    // Renderer ve RenderWindow oluştur
    vtkSmartPointer<vtkRenderer> renderer = vtkSmartPointer<vtkRenderer>::New();
    vtkSmartPointer<vtkRenderWindow> renderWindow = vtkSmartPointer<vtkRenderWindow>::New();
    renderWindow->AddRenderer(renderer);

    // RenderWindowInteractor oluştur
    vtkSmartPointer<vtkRenderWindowInteractor> renderWindowInteractor = vtkSmartPointer<vtkRenderWindowInteractor>::New();
    renderWindowInteractor->SetRenderWindow(renderWindow);

    // Özel picker nesnesi
    vtkSmartPointer<CustomPicker> picker = vtkSmartPointer<CustomPicker>::New();
    renderWindowInteractor->SetPicker(picker);

    // Küp aktörünü sahneye ekle
    renderer->AddActor(cubeActor);
    renderer->SetBackground(0.1, 0.2, 0.4); // Arka plan rengi

    // Etkileşimi başlat
    renderWindow->Render();
    renderWindowInteractor->Start();

    return 0;
}
