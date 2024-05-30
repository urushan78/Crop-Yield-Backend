from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .prediction import predict_production_rf


@csrf_exempt
def predict_crop_production(request):
    if request.method == "POST":
        year = float(request.POST.get("year"))
        # print(f'year:{year}')
        latitude = float(request.POST.get("latitude"))
        longitude = float(request.POST.get("longitude"))
        precipitation = float(request.POST.get("precipitation"))
        temp_range = float(request.POST.get("temp_range"))
        surface_pressure = float(request.POST.get("surface_pressure"))
        specific_humidity = float(request.POST.get("specific_humidity"))
        relative_humidity = float(request.POST.get("relative_humidity"))
        area = float(request.POST.get("area"))
        crop_barley = int(request.POST.get("crop_barley"))
        crop_maize = int(request.POST.get("crop_maize"))
        crop_millet = int(request.POST.get("crop_millet"))
        crop_paddy = int(request.POST.get("crop_paddy"))
        crop_wheat = int(request.POST.get("crop_wheat"))

        prediction = predict_production_rf(
            [year,
            latitude,
            longitude,
            area,
            precipitation,
            temp_range,
            relative_humidity,
            surface_pressure,
            specific_humidity,
            crop_barley,
            crop_maize,
            crop_millet,
            crop_paddy,
            crop_wheat,]
        )
        response = {"prediction": prediction}
        return JsonResponse(response)
    else:
        return JsonResponse({"error": "Invalid request method"})
