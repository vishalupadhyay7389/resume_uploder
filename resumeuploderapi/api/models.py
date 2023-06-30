from django.db import models
from rest_framework import serializers

# Create your models here.
STATE_CHOICE = (
     ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
    ('Chandigarh','Chandigarh'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Nagaland','Nagaland'),
    ('Mizoram','Mizoram'),
    ('Uttarakhand','Uttarakhand'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Telangana','Telangana'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Rajasthan','Rajasthan'),
    ('Punjab','Punjab'),
    ('Goa','Goa'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Bihar','Bihar'),
    ('Puducherry','Puducherry'),
    ('Lakshadweep','Lakshadweep'),
    ('Ladakh ','Ladakh '),
    ('New Delhi ','New Delhi '),
    ('Daman and Diu','Daman and Diu'),
    ('Dadra and Nagar Haveli','Dadra and Nagar Haveli'),
    ('Raipur','Raipur'),
    ('Bhali','Bhali')
)

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(auto_now=False , auto_now_add=False)
    state = models.CharField(choices=STATE_CHOICE , max_length=50)
    gender = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    pImage = models.ImageField(upload_to='pimages' , blank=True)
    rdoc = models.FileField(upload_to='rdocs' , blank=True)

class ProfileSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'