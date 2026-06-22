from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.db.models import Max
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import *


def login(request):
    return render(request,"login_index.html")
def logout(request):
    request.session['lid']=''
    return HttpResponse("<script>alert('Logout Success ');window.location='/myapp/login/'</script>")





def login_post(request):
    uname = request.POST['textfield']
    pswd = request.POST['textfield2']

    l=Login.objects.filter(username=uname,password=pswd)
    if l.exists():
        S = Login.objects.get(username=uname, password=pswd)
        request.session['lid']=S.id
        if S.type == 'admin':
            return HttpResponse("<script>alert('login ok');window.location='/myapp/admin_home/'</script>")
        elif S.type == 'doctor':
            return HttpResponse("<script>alert('login ok');window.location='/myapp/doctor_home/'</script>")
        elif S.type == 'user':
            return HttpResponse("<script>alert('login ok');window.location='/myapp/userhome/'</script>")
        else :
            return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")
    else :
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")



def admin_home(request):
    if request.session['lid']=='':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")
    return render(request,"admin/adminindex.html")

def admin_change_password(request):
    if request.session['lid']=='':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")
    return render(request,"admin/change_password.html")

def admin_change_password_post(request):
    cpswd = request.POST['textfield']
    npswd = request.POST['textfield2']
    confpswd = request.POST['textfield3']
    ch=Login.objects.get(id=request.session['lid'])
    if ch.password==cpswd:
        if npswd==confpswd:
            ch = Login.objects.filter(id=request.session['lid']).update(password=npswd)
            return HttpResponse("<script>alert('change password successfull');window.location='/myapp/login/'</script>")
        else:
            return HttpResponse("<script>alert('change password unsuccessfull');window.location='/myapp/admin_change_password/'</script>")

    else:
        return HttpResponse("<script>alert('password mismatched');window.location='/myapp/admin_change_password/'</script>")

def admin_view_review(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")

    data = Review.objects.all()
    return render(request,"admin/admin_view_review.html",{'data':data})

def admin_view_review_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    data = Review.objects.filter(date__range=[fromdate,todate])
    return render(request, "admin/admin_view_review.html", {'data': data})


def admin_view_rejected_doctor(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")

    data = Doctor.objects.filter(LOGIN__type='rejected')
    return render(request,"admin/admin_view_rejected_doctors.html",{'data':data})

def admin_view_rejected_doctor_post(request):
    search = request.POST['textfield']
    data = Doctor.objects.filter(LOGIN__type='rejected',name__icontains=search)
    return render(request, "admin/admin_view_rejected_doctors.html", {'data': data})


def admin_view_feedback(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")

    data = Feedback.objects.all()
    return render(request,"admin/admin_view_feedback.html",{'data':data})

def admin_view_feedback_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    data = Feedback.objects.filter(date__range=[fromdate, todate])
    return render(request,"admin/admin_view_feedback.html",{'data':data})

def rejected_doctors(request,id):
    Login.objects.filter(id=id).update(type='rejected')
    return HttpResponse("<script>alert(' doctor rejected successfully ');window.location='/myapp/admin_view_doctor/'</script>")



def admin_view_doctor(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")

    data = Doctor.objects.filter(LOGIN__type='pending')
    return render(request,"admin/admin_view_doctor.html",{'data':data})

def admin_view_doctor_post(request):
    search = request.POST['textfield']
    data = Doctor.objects.filter(LOGIN__type='pending',name__icontains=search)

    return render(request, "admin/admin_view_doctor.html", {'data': data})



def admin_view_approved_doctors(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")

    data = Doctor.objects.filter(LOGIN__type='doctor')
    return render(request,"admin/admin_view_approved_doctors.html",{'data':data})

def admin_view_approved_doctors_post(request):
    search = request.POST['textfield']
    data = Doctor.objects.filter(LOGIN__type='doctor',name__icontains=search)
    return render(request, "admin/admin_view_approved_doctors.html", {'data': data})


def approved_doctors(request,id):
    Login.objects.filter(id=id).update(type='doctor')
    return HttpResponse(
        "<script>alert('approved doctor successfull');window.location='/myapp/admin_view_doctor/'</script>")



################################################################


def doctor_change_password(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")

    return render(request,'doctor/change_password.html')

def doctor_change_password_post(request):
    cpswd = request.POST['textfield']
    npswd = request.POST['textfield2']
    confpswd = request.POST['textfield3']
    ch = Login.objects.get(id=request.session['lid'])
    if ch.password == cpswd:
        if npswd == confpswd:
            ch = Login.objects.filter(id=request.session['lid']).update(password=npswd)
            return HttpResponse("<script>alert('change password successfull');window.location='/myapp/login/'</script>")
        else:
            return HttpResponse(
                "<script>alert('change password unsuccessfull');window.location='/myapp/admin_change_password/'</script>")

    else:
        return HttpResponse(
            "<script>alert('password mismatched');window.location='/myapp/admin_change_password/'</script>")


def doctor_add_schedule(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")

    return render(request,'doctor/doctor_add_schedule.html')

def doctor_add_schedule_post(request):
    fromtime=request.POST['fromtime']
    totime=request.POST['totime']
    date=request.POST['date']
    slot = request.POST['slot']

    sobj=Schedule()
    sobj.date=date
    sobj.from_time=fromtime
    sobj.to_time=totime
    sobj.slot=slot
    sobj.status='pending'
    sobj.DOCTOR=Doctor.objects.get(LOGIN__id=request.session['lid'])
    sobj.save()

    return HttpResponse(
        "<script>alert('Addedd Successfully');window.location='/myapp/doctor_home/'</script>")


def doctor_edit_profile(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")

    data=Doctor.objects.get(LOGIN_id=request.session['lid'])

    return render(request,'doctor/doctor_edit_profile.html',{'data':data})

def doctor_edit_profile_post(request):
    name=request.POST['textfield']
    email=request.POST['textfield2']
    contact=request.POST['textfield3']
    qualification=request.POST['textfield4']
    place=request.POST['textfield5']
    pin=request.POST['textfield6']
    post=request.POST['textfield7']
    gender=request.POST['RadioGroup1']





    sa=Doctor.objects.get(LOGIN__id=request.session['lid'])
    if 'imageField' in request.FILES:
        photo = request.FILES['imageField']

        from datetime import datetime
        dt = datetime.now().strftime('%Y%m%d%H%M%S') + 'jpg'
        fs = FileSystemStorage()
        fs.save(dt, photo)
        path = fs.url(dt)

        sa.name=name
        sa.email=email
        sa.contact=contact
        sa.qualification=qualification
        sa.place=place
        sa.pin=pin
        sa.post=post
        sa.photo=path
        sa.gender=gender
        sa.save()

    else:
        sa.name = name
        sa.email = email
        sa.contact = contact
        sa.qualification = qualification
        sa.place = place
        sa.pin = pin
        sa.post = post

        sa.gender = gender
        sa.save()
    return HttpResponse(
        "<script>alert('Edited Successfully');window.location='/myapp/doctor_view_profile/'</script>")

def doctor_edit_schedule(request,id):
    sd=Schedule.objects.get(id=id)
    return render(request,'doctor/doctor_edit_schedule.html',{"data":sd})

def doctor_edit_schedule_post(request):
    from_time = request.POST['from_time']
    to_time = request.POST['to_time']
    date = request.POST['date']
    slot = request.POST['slot']
    id=request.POST['id']

    sobj = Schedule.objects.get(id=id)
    sobj.date = date
    sobj.from_time = from_time
    sobj.to_time = to_time
    sobj.slot = slot
    sobj.save()

    return HttpResponse(
        "<script>alert('Editted Successfully');window.location='/myapp/doctor_home/'</script>")

def doctor_delete_schedule(request,id):
    Schedule.objects.filter(id=id).delete()
    return HttpResponse(
        "<script>alert('Deleted Successfully');window.location='/myapp/doctor_home/'</script>")


def doctor_signup(request):
    return render(request,'doctor/doctor_signup.html')

def doctor_signup_post(request):
    name=request.POST['name']
    email=request.POST['email']
    contact=request.POST['contact']
    qualification=request.POST['qualification']
    place=request.POST['place']
    pin=request.POST['pin']
    post=request.POST['post']
    photo=request.FILES['photo']
    gender=request.POST['gender']
    password=request.POST['password']
    confrimpsw=request.POST['confrimpsw']
    if password == confrimpsw:
        l=Login()
        l.username=email
        l.password=confrimpsw
        l.type='pending'
        l.save()

        from datetime import datetime
        dt=datetime.now().strftime('%Y%m%d%H%M%S')+'jpg'
        fs=FileSystemStorage()
        fs.save(dt,photo)
        path=fs.url(dt)

        sd=Doctor()
        sd.name=name
        sd.email=email
        sd.contact=contact
        sd.qualification=qualification
        sd.place=place
        sd.pin=pin
        sd.post=post
        sd.photo=path
        sd.gender=gender
        sd.LOGIN=l
        sd.save()
        return HttpResponse(
        "<script>alert('Registered Successfully');window.location='/myapp/login/'</script>")
    else:
        return HttpResponse(
            "<script>alert('password and confirm password not equal');window.location='/myapp/login/'</script>")


def doctor_view_appointment(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")

    data=Appointment.objects.filter(SCHEDULE__DOCTOR__LOGIN_id=request.session['lid'])
    return render(request,'doctor/doctor_view_appointment.html',{'data':data})

def doctor_view_appointment_post(request):
    f_date = request.POST['textfield']
    t_date = request.POST['textfield2']
    data = Appointment.objects.filter(SCHEDULE__DOCTOR__LOGIN_id=request.session['lid'],date__range=[f_date,t_date])
    return render(request, 'doctor/doctor_view_appointment.html', {'data': data})


def doctor_view_profile(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")

    data=Doctor.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'doctor/doctor_view_profile.html',{'data':data})


def doctor_view_schedule(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")

    sa=Schedule.objects.filter(DOCTOR__LOGIN__id=request.session['lid'])
    return render(request,'doctor/doctor_view_schedule.html',{"data":sa})

def doctor_view_schedule_post(request):
    f_date = request.POST['textfield']
    t_date = request.POST['textfield2']
    sa = Schedule.objects.filter(DOCTOR__LOGIN__id=request.session['lid'],date__range=[f_date,t_date])
    return render(request, 'doctor/doctor_view_schedule.html', {"data": sa})


# def pnpreidct(request):
#     import os
#     import tensorflow as tf
#     from django.core.files.storage import FileSystemStorage
#     from django.http import JsonResponse
#     from datetime import datetime
#     try:
#         # Validate the request contains a file
#         if "photo" not in request.FILES:
#             return JsonResponse({'status': 'error', 'message': 'No file uploaded'}, status=400)
#
#         file = request.FILES["photo"]
#
#         # Generate a unique filename
#         filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"  # Assuming it's an image, not a .wav file
#
#         # Save the uploaded file
#         fs = FileSystemStorage()
#         file_path = fs.save(filename, file)
#         full_path = fs.path(file_path)
#
#         # Disable TF warnings
#         os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#
#         # Load label file
#         label_file_path = "C:\\Users\\n8100\\PycharmProjects\\Pneumonia_detection\\myapp\\logsold\\output_labels.txt"
#         with open(label_file_path, "r") as f:
#             label_lines = [line.strip() for line in f.readlines()]
#
#         # Load model
#         model_path = "C:\\Users\\n8100\\PycharmProjects\\Pneumonia_detection\\myapp\\logsold\\output_graph.pb"
#         with tf.io.gfile.GFile(model_path, 'rb') as f:
#             graph_def = tf.compat.v1.GraphDef()
#             graph_def.ParseFromString(f.read())
#             tf.compat.v1.import_graph_def(graph_def, name='')
#
#         # Run prediction
#         with tf.compat.v1.Session() as sess:
#             softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
#
#             with tf.io.gfile.GFile(full_path, 'rb') as image_file:
#                 image_data = image_file.read()
#
#             predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})
#
#             # Get the highest confidence label
#             top_index = predictions[0].argmax()
#             result = label_lines[top_index]
#
#         return JsonResponse({'status': 'ok', 'res': result})
#
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': str(e)}, status=500)




def pnpreidct(request):

    files = request.FILES["photo"]

    from datetime import datetime
    fnam = ""+datetime.now().strftime("%Y%m%d_%H%M%S")+".wav"
    dd = ""+datetime.now().strftime("%Y%m%d_%H%M%S")+".jpg"

    fs=FileSystemStorage()
    ff=fs.save(fnam,files)
    fs.save(dd,files)
    p=fs.path(ff)

    fs = FileSystemStorage()
    ff = fs.save(dd, files)
    fs.save(dd, files)
    path = fs.url(ff)

    # from  base64 import  b64decode
    #
    # p="C:\\Users\\n8100\\PycharmProjects\\Pneumonia_detection\\media\\pnu\\" + fnam
    #
    # with open(p,"wb") as h:
    #
    #     h.write(b64decode(files))

    import os
    # Disable tensorflow compilation warnings
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    import tensorflow as tf
    # image_path = sys.argv[1]
    # image_path="C:\\Users\\ELCOT-Lenovo\\Documents\\images\\sign_dataset\\test\\A\\color_0_0016"
    # Read the image_data

    # with tf.io.gfile.GFile(model_path, 'rb') as f:
    # graph_def = tf.compat.v1.GraphDef()
    #             graph_def.ParseFromString(f.read())
    #             tf.compat.v1.import_graph_def(graph_def, name='')
    # image_data = tf.gfile.FastGFile(
    #     p, 'rb').read()

    image_data = tf.io.gfile.GFile(p, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
                   in tf.gfile.GFile("C:\\Users\\n8100\\PycharmProjects\\Pneumonia_detection\\myapp\\logsold\\output_labels.txt")]
    res=""
    # Unpersists graph from file
    with tf.gfile.FastGFile("C:\\Users\\n8100\\PycharmProjects\\Pneumonia_detection\\myapp\\logsold\\output_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')
    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor, \
                               {'DecodeJpeg/contents:0': image_data})
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            print('%s (score = %.5f)' % (human_string, score))
            res=human_string
            break
    b=Detection()
    b.date=datetime.now().today()
    b.file=path
    b.result=res
    b.APPOINTMENT_id=request.session['aid']
    b.save()

    return render(request,'doctor/doctor_xray_upload.html',{'data':res})

    # return HttpResponse(f"<script>alert('X - ray uploaded success Result is {res} ,Saved to result ');window.location='/myapp/doctor_view_appointment/'</script>")


    # return  JsonResponse(
    #     {
    #         'status':'ok',
    #         'res':res
    #     }
    # )






def doctor_xray__upload(request,id):
    request.session['aid']=id
    return render(request,'doctor/doctor_xray_upload.html')

def doctor_view_result(request,id):
    data=Detection.objects.filter(APPOINTMENT_id=id)
    return render(request,'doctor/doctor_view_result.html',{"data":data})











def doctor_home(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")
    return render(request,"doctor/doctorindex.html")


#####################################################user



def user_edit_profile(request):
    data = User.objects.get(LOGIN_id=request.session['lid'])

    return render(request, 'user/user_edit_profile.html', {'data': data})

def user_edit_profile_post(request):
    name = request.POST['textfield']
    email = request.POST['textfield2']
    contact = request.POST['textfield3']

    place = request.POST['textfield4']
    pin = request.POST['textfield5']
    post = request.POST['textfield6']
    age = request.POST['textfield7']
    gender = request.POST['RadioGroup1']

    sa = User.objects.get(LOGIN_id=request.session['lid'])
    if 'imageField' in request.FILES:
        photo = request.FILES['imageField']
        from datetime import datetime
        dt = datetime.now().strftime('%Y%m%d%H%M%S') + 'jpg'
        fs = FileSystemStorage()
        fs.save(dt, photo)
        path = fs.url(dt)
        sa.photo = path
        sa.save()

    sa.name = name
    sa.email = email
    sa.contact = contact

    sa.palce = place
    sa.pin = pin
    sa.post = post
    sa.age = age
    sa.gender = gender
    sa.save()
    return HttpResponse(
        "<script>alert('Edited Successfully');window.location='/myapp/user_view_profile/'</script>")


def user_sign_up(request):
    return render(request,"user/signup_index.html")

def user_sign_up_post(request):
    name = request.POST['name']
    print(name)
    email = request.POST['email']
    print(email)
    contact = request.POST['contact']
    print(contact)
    place = request.POST['place']
    print(place)
    pin = request.POST['pin']
    print(pin)
    post = request.POST['post']
    print(post)
    age = request.POST['age']
    print(age)
    photo = request.FILES['photo']
    gender = request.POST['gender']
    password = request.POST['password']
    confrimpsw = request.POST['confrimpasw']


    l = Login()
    l.username = email
    l.password = confrimpsw
    l.type='user'
    l.save()

    if password == confrimpsw:

        from datetime import datetime
        dt = datetime.now().strftime('%Y%m%d%H%M%S') + 'jpg'
        fs = FileSystemStorage()
        fs.save(dt, photo)
        path = fs.url(dt)

        sd = User()
        sd.name = name
        sd.email = email
        sd.contact = contact

        sd.palce = place
        sd.pin = pin
        sd.post = post
        sd.photo = path
        sd.age = age
        sd.gender = gender
        sd.LOGIN = l
        sd.save()

        return HttpResponse(
            "<script>alert('Registered Successfully');window.location='/myapp/login/'</script>")


def user_view_doctor(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")

    data = Doctor.objects.all()
    return render(request,"user/user_view_doctor.html",{'data':data})

def user_view_doctor_post(request):
    search=request.POST['search']
    data = Doctor.objects.filter(name__icontains=search)
    return render(request, "user/user_view_doctor.html", {'data': data})

def user_view_profile(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")

    data=User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'user/user_view_profile.html',{'data':data})

def user_view_profile_post(request):
    return

def user_send_feedback(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")

    return render(request,"user/user_send_feedback.html")

def user_send_feedback_post(request):
    feedback=request.POST['feedback']
    sa=Feedback()
    from datetime import datetime
    sa.date= datetime.now().today()
    sa.feedback = feedback
    sa.USER = User.objects.get(LOGIN_id=request.session['lid'])
    sa.save()
    return HttpResponse(
        "<script>alert('Feedback submitted Successfully');window.location='/myapp/userhome/'</script>")

def user_send_review_about_doctor(request,id):
    request.session['did']=id
    return render(request,"user/user_send_review_about_doctor.html")

def user_send_review_about_doctor_post(request):
    review = request.POST['textfield']
    sa = Review()
    from datetime import datetime
    sa.date = datetime.now().today()
    sa.feedback = review
    sa.USER = User.objects.get(LOGIN_id=request.session['lid'])
    sa.DOCTOR_id = request.session['did']
    sa.save()
    return HttpResponse(
        "<script>alert('Review submitted Successfully');window.location='/myapp/userhome/'</script>")


def user_view_appointment(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")

    data=Appointment.objects.filter(USER__LOGIN=request.session['lid'])
    return render(request,"user/user_view_appointment.html",{"data":data})

def user_view_appointment_post(request):
    f_date=request.POST['textfield']
    t_date=request.POST['textfield2']
    data = Appointment.objects.filter(USER__LOGIN=request.session['lid'],date__range=[f_date,t_date])
    return render(request, "user/user_view_appointment.html", {"data": data})


def user_view_result(request,id):
    data=Detection.objects.filter(APPOINTMENT_id=id)
    return render(request,"user/user_view_result.html",{'data':data})

def user_view_result_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")

    data = Detection.objects.filter(APPOINTMENT_id=id)
    return render(request, "user/user_view_result.html", {'data': data})


def user_view_schedule(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")

    sa = Schedule.objects.filter(status='pending')
    return render(request, 'user/user_view_schedule.html', {"data": sa})


def user_view_schedule_post(request):
    f_date=request.POST['textfield']
    t_date=request.POST['textfield2']
    sa = Schedule.objects.filter(status='pending',date__range=[f_date,t_date])
    return render(request, 'user/user_view_schedule.html', {"data": sa})


def userhome(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")

    return render(request,"user/userindex.html")


def book_appointment(request,id):
    schedule = Schedule.objects.get(id=id)
    aa=Appointment.objects.filter(SCHEDULE__id=id,USER__LOGIN__id=request.session['lid'])
    if aa.exists():
        return HttpResponse(
            "<script>alert('Already Booked');window.location='/myapp/userhome/'</script>"
        )
    # Check if slots are available
    if int(schedule.slot) <= 0:
        return HttpResponse(
            "<script>alert('No slots available');window.location='/myapp/userhome/'</script>"
        )
    sa = Appointment()
    sa.date = datetime.now().today()
    sa.SCHEDULE_id = id
    sa.USER = User.objects.get(LOGIN_id=request.session['lid'])
    last_token = Appointment.objects.filter(SCHEDULE_id=id).aggregate(Max('tocken'))['tocken__max']
    sa.tocken = (int(last_token) + 1) if last_token is not None else 1
    sa.save()
    schedule.slot -= 1

    schedule.save()

    return HttpResponse(
        "<script>alert('Appointement submitted Successfully');window.location='/myapp/userhome/'</script>")




def user_change_password(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('login failed');window.location='/myapp/login/'</script>")

    return render(request,'user/change_password.html')

def user_change_password_post(request):
    cpswd = request.POST['textfield']
    npswd = request.POST['textfield2']
    confpswd = request.POST['textfield3']
    ch = Login.objects.get(id=request.session['lid'])
    if ch.password == cpswd:
        if npswd == confpswd:
            ch = Login.objects.filter(id=request.session['lid']).update(password=npswd)
            return HttpResponse("<script>alert('change password successfull');window.location='/myapp/login/'</script>")
        else:
            return HttpResponse(
                "<script>alert('change password unsuccessfull');window.location='/myapp/user_change_password/'</script>")

    else:
        return HttpResponse(
            "<script>alert('password mismatched');window.location='/myapp/user_change_password/'</script>")



def check_session(request):
    is_authenticated = request.session["lid"]
    if is_authenticated=="":
        is_authenticated="no"
    else:
        is_authenticated="ok"

    return JsonResponse({'is_authenticated': is_authenticated})