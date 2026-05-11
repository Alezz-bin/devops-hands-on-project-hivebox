from fastapi import FastAPI
import requests
from datetime import datetime, timezone, timedelta

app = FastAPI()

# 1. تعريف الثوابت
VERSION = "1.0.0"
# رابط جلب الصناديق التي تقيس درجة الحرارة
OPEN_SENSE_MAP_URL = "https://api.opensensemap.org/boxes?phenomenon=temperature"

@app.get("/")
def read_root():
    """الترحيب الأساسي"""
    return {"message": "Welcome to HiveBox API"}

@app.get("/version")
def read_version():
    """المتطلب الأول: إرجاع نسخة التطبيق"""
    return {"version": VERSION}

@app.get("/temperature")
def read_temperature():
    """المتطلب الثاني: حساب متوسط درجة الحرارة لآخر ساعة"""
    try:
        response = requests.get(OPEN_SENSE_MAP_URL, timeout=10)
        response.raise_for_status() # التأكد من أن الـ API الخارجي يعمل
        data = response.json()
    except (requests.exceptions.Timeout, requests.exceptions.RequestException) as e:
        return {"error": "Could not fetch data from openSenseMap", "details": str(e)}

    temperatures = []
    now = datetime.now(timezone.utc)
    one_hour_ago = now - timedelta(hours=1)

    for box in data:
        sensors = box.get('sensors', [])
        for sensor in sensors:
            # التحقق من أن الحساس يقيس الحرارة
            title = sensor.get('title', '').lower()
            unit = sensor.get('unit', '')
            
            if 'temp' in title or unit == '°C':
                last_m = sensor.get('lastMeasurement')
                
                # صمام الأمان: التأكد أن القراءة عبارة عن قاموس (Dictionary)
                if isinstance(last_m, dict):
                    value = last_m.get('value')
                    created_at_str = last_m.get('createdAt')
                    
                    if value and created_at_str:
                        try:
                            # تحويل التاريخ القادم من الـ API إلى كائن datetime
                            # ملاحظة: Z تعني توقيت UTC
                            m_time = datetime.fromisoformat(created_at_str.replace("Z", "+00:00"))
                            
                            # شرط الساعة الواحدة:
                            if m_time >= one_hour_ago:
                                temperatures.append(float(value))
                        except (ValueError, TypeError):
                            continue # تجاهل القراءات غير الصحيحة

    # حساب المتوسط
    if not temperatures:
        return {
            "message": "No temperature data found in the last hour",
            "average_temperature": 0,
            "sensors_count": 0
        }
    
    average_temp = sum(temperatures) / len(temperatures)
    
    return {
        "average_temperature": round(average_temp, 2),
        "sensors_count": len(temperatures),
        "period": "last_1_hour"
    }