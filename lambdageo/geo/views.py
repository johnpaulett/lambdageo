from datetime import datetime
from django.db.models import Count
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from geo.models import Building, Device, Measurement

@csrf_exempt
def upload(request):
    # only accept POSTS
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])


    # check the session for an existing Device
    device = request.session.get('device', None)
    if device is None:
        # otherwise, create the Device
        device = Device.objects.create(
            user_agent=request.META['HTTP_USER_AGENT']
        )
        # hold onto the Device across requests
        request.session['device'] = device

    m = Measurement(
        device = device,
        ip = request.META['REMOTE_ADDR'],
        datetime = datetime.now()
    )

    #'The location can be WKT, e.g. 'POINT (-90.402347 38.565116)'
    # or GeoJSON, e.g. '{"type":"Point", "coordinates":[97.03125, 39.7265625]}'
    m.location = request.raw_post_data

    # save the the database
    m.save()

    return HttpResponse('thanks')



def index(request):
    buildings = Building.objects.all()

    # all devices, ordered by the number of associated measurements
    devices = Device.objects.annotate(
        num_measurements=Count('measurement')
    ).order_by('-num_measurements')

    return render(request, 'index.html', {
        'buildings': buildings,
        'devices': devices,
    })




def building_detail(request, building_id):
    building = Building.objects.get(id=building_id)

    measurements = Measurement.objects.distance(
        building.poly
    ).order_by('distance')

    inside_measurements = Measurement.objects.filter(
        location__contained=building.poly
    )

    return render(request, 'building_detail.html', {
        'building': building,
        'inside_measurements': inside_measurements,
        'measurements': measurements,
    })

