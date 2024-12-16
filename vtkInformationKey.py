import vtk

# vtkInformation nesnesi oluştur
info = vtk.vtkInformation()

# Integer ve String anahtarları tanımla
integer_key = vtk.vtkInformationIntegerKey.MakeKey("MyIntegerKey", "ExampleGroup")
string_key = vtk.vtkInformationStringKey.MakeKey("MyStringKey", "ExampleGroup")

# Bilgi ekle
info.Set(integer_key, 42)  # Integer değeri ekle
info.Set(string_key, "Hello VTK!")  # String değeri ekle

# Bilgiye erişim
if info.Has(integer_key):
    int_value = info.Get(integer_key)
    print(f"MyIntegerKey: {int_value}")

if info.Has(string_key):
    string_value = info.Get(string_key)
    print(f"MyStringKey: {string_value}")

# Anahtarı kaldır
info.Remove(integer_key)

# Anahtarın kaldırıldığını kontrol et
if not info.Has(integer_key):
    print("MyIntegerKey has been removed.")