import vtk
import logging

# Python logger yapılandırması
logging.basicConfig(level=logging.INFO, filename="log_output.txt", filemode="w",
                    format="%(levelname)s: %(message)s")

# Python logger örneği
logger = logging.getLogger("VTK Logger")

# Log örnekleri
logger.debug("Bu bir DEBUG mesajıdır (genelde gizlenir).")
logger.info("Bu bir INFO mesajıdır (genel bilgi).")
logger.warning("Bu bir WARNING mesajıdır (uyarı).")
logger.error("Bu bir ERROR mesajıdır (hata).")
logger.critical("Bu bir CRITICAL mesajıdır (kritik hata).")

# Performans zamanlayıcı örneği
timer = vtk.vtkTimerLog()
timer.StartTimer()

# Örnek bir işlem (bir küp oluştur ve güncelle)
cube_source = vtk.vtkCubeSource()
cube_source.Update()

timer.StopTimer()

# Zaman ölçümünü log'a yaz
elapsed_time = timer.GetElapsedTime()
logger.info(f"Küp oluşturma süresi: {elapsed_time:.4f} saniye")

print("Log işlemi tamamlandı. Log dosyası: 'log_output.txt'")
