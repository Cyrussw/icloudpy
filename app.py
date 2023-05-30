from func import *

# Sistemi başlatırken temiz bir sayfa oluştur.
start()

# iCloud hesabınıza bağlı cihazları listeler.
viewDevices()

# Cihazın son konumunu harita şeklinde html dosyasında oluşturur isteğe bağlı olarak ses çalar.
get_device_location()

# Seçilen cihazda ses çalar.
playSound()

# iCloud hesabına kayıtlı kişileri listeler.
get_contacts()

# iCloud hesabına kayıtlı albümlerini listeler ve fotoğrafların adını tek tek listeler.
get_photo_albums()
