import vtk

# Bir context view oluştur
context_view = vtk.vtkContextView()
context_view.GetRenderer().SetBackground(1.0, 1.0, 1.0)  # Beyaz arka plan

# Bir chart (grafik) oluştur
chart = vtk.vtkChartXY()

# Chart'ı sahneye ekle
context_view.GetScene().AddItem(chart)

# Bir veri tablosu oluştur
table = vtk.vtkTable()

# X ve Y eksenleri için veri sütunları oluştur
arrX = vtk.vtkFloatArray()
arrX.SetName("X-Axis")
arrY = vtk.vtkFloatArray()
arrY.SetName("Y-Axis")

# Tabloya sütunları ekle
table.AddColumn(arrX)
table.AddColumn(arrY)

# Verileri ekle
num_points = 50
for i in range(num_points):
    x = i
    y = i * i
    arrX.InsertNextValue(x)
    arrY.InsertNextValue(y)

# Tablonun satır sayısını ayarla
table.SetNumberOfRows(num_points)

# Grafiğe bir veri serisi ekle
line = chart.AddPlot(vtk.vtkChart.LINE)
line.SetInputData(table, 0, 1)  # X = 0. sütun, Y = 1. sütun
line.SetColor(0, 255, 0, 255)  # Yeşil renk
line.SetWidth(2.0)

# Render penceresi ve etkileşim
context_view.GetRenderWindow().SetSize(800, 600)
context_view.GetRenderWindow().Render()
context_view.GetInteractor().Start()
