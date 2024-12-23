#include <vtkAutoInit.h>
VTK_MODULE_INIT(vtkRenderingOpenGL2);
VTK_MODULE_INIT(vtkRenderingContextOpenGL2);
VTK_MODULE_INIT(vtkInteractionStyle);

#include <vtkContextView.h>
#include <vtkContextScene.h>
#include <vtkContext2D.h>
#include <vtkPen.h>
#include <vtkBrush.h>
#include <vtkContextItem.h>
#include <vtkRenderWindow.h>
#include <vtkRenderWindowInteractor.h>
#include <vtkSmartPointer.h>

class CustomContextItem : public vtkContextItem {
public:
    static CustomContextItem* New() {
        return new CustomContextItem();
    }

    bool Paint(vtkContext2D* painter) override {
        painter->GetPen()->SetColor(0, 255, 0, 255);  // Yeşil
        painter->GetBrush()->SetColor(255, 0, 0, 255); // Kırmızı
        painter->DrawEllipse(100, 100, 50, 50); // Çizim
        return true;
    }
};

int main() {
    auto contextView = vtkSmartPointer<vtkContextView>::New();
    contextView->GetRenderWindow()->SetSize(800, 600);
    auto customItem = vtkSmartPointer<CustomContextItem>::New();
    contextView->GetScene()->AddItem(customItem);

    contextView->GetRenderWindow()->Render();
    contextView->GetInteractor()->Start();
    return 0;
}
