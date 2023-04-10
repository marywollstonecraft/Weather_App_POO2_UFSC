from Interface import *
from City_Data import *


tela_principal = TELA_PRINCIPAL()
tela_principal.mainloop()

def current_time(CITY='london'):
    geolocator = Nominatim(user_agent='geopiExercises')
    location= geolocator.geocode(CITY)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime('%I:%M %p')
    return current_time