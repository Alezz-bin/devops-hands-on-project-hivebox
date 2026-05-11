# pyrefly: ignore [missing-import]
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

# نحن نستخدم TestClient لمحاكاة مستخدم يطلب البيانات من الـ API
client = TestClient(app)

# --- اختبار بسيط (النسخة) ---
def test_read_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

# --- اختبار متقدم (درجة الحرارة) باستخدام الـ Mocking ---
def test_read_temperature_success():
    # "patch" هي خدعة لإيقاف طلب الإنترنت الحقيقي
    # وبدلاً من ذلك، نعطي الكود بيانات "وهمية" لنتأكد أنه يحسبها صح
    mock_data = [
        {
            "sensors": [
                {
                    "title": "Temperatur",
                    "unit": "°C",
                    "lastMeasurement": {
                        "value": "20.0",
                        "createdAt": "2026-05-11T14:00:00Z" # وقت حديث جداً
                    }
                },
                {
                    "title": "Temperatur",
                    "unit": "°C",
                    "lastMeasurement": {
                        "value": "30.0",
                        "createdAt": "2026-05-11T14:10:00Z"
                    }
                }
            ]
        }
    ]

    # هنا نقول للكود: "عندما تطلب requests.get، لا تذهب للإنترنت، بل خذ mock_data"
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = mock_data
        mock_get.return_value.status_code = 200

        response = client.get("/temperature")
        
        # التأكد من النتائج
        assert response.status_code == 200
        # المتوسط لـ 20 و 30 هو 25
        assert response.json()["average_temperature"] == 25.0
        assert response.json()["sensors_count"] == 2